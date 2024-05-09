from sqlalchemy import select

from app.config.connection import session_maker
from app.models import Message, Log


def get_model_rows_containing(model, string: str):
    return select(model.created, model.string, model.int_id).where(model.string.contains(string))


def get_all_rows_containing(string: str):
    messages = get_model_rows_containing(Message, string)
    logs = get_model_rows_containing(Log, string)
    with session_maker() as session:
        return session.execute(messages.union(logs).order_by('int_id', 'created')).all()

