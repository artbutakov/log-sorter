import re
from datetime import datetime
from pathlib import Path

from app.config.connection import session_maker
from app.models import Message, Log


def get_regex_string(pattern: str, raw_string: str) -> str:
    regex = re.compile(pattern)
    output = regex.search(raw_string)
    return output.group() if output else None


def get_id(string: str) -> str:
    return string.rsplit('id=', 1)[-1].strip() if 'id=' in string else None


def get_int_id(string: str) -> str:
    return get_regex_string(r'1[a-zA-Z0-9]{5}-000[a-zA-Z0-9]{3}-[a-zA-Z0-9]{2}', string)


def sort_log(file_path: Path or str):
    with open(file_path, 'r', encoding='utf-8') as file:
        completed_status_lines = list()
        with session_maker() as session:
            for line in file:
                created = datetime.strptime(
                    get_regex_string(r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}', line),
                    '%Y-%m-%d %H:%M:%S',
                )
                int_id = get_int_id(line)
                log_message = line.removeprefix(f'{created} {int_id}').strip()
                if '<=' in line:
                    obj = Message(
                        created=created,
                        id=get_id(line),
                        int_id=int_id,
                        string=log_message,
                    )
                else:
                    obj = Log(
                        created=created,
                        int_id=int_id,
                        string=log_message,
                        address=get_regex_string(r'[a-zA-Z0-9._]*@[a-zA-Z0-9.-]*.(ru|com|net|cz|su|gs)', line),
                    )
                    if 'Completed' in line:
                        completed_status_lines.append(line)
                session.add(obj)
            for line in completed_status_lines:
                int_id = get_int_id(line)
                messages = session.execute(Message.get_by_int_id(int_id)).scalars().all()
                for message in messages:
                    message.status = True
            session.commit()
