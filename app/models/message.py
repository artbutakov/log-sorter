from datetime import datetime

import sqlalchemy as sa
from sqlalchemy import select, Select
from sqlalchemy.orm import Mapped, mapped_column

from app.config.connection import Base


class Message(Base):
    __tablename__ = 'message'

    pk_id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    created: Mapped[datetime] = mapped_column(sa.DateTime(timezone=False), index=True)
    id: Mapped[str] = mapped_column(sa.String(), nullable=True)
    int_id: Mapped[str] = mapped_column(sa.String(16), index=True)
    string: Mapped[str] = mapped_column(sa.String())
    status: Mapped[bool] = mapped_column(sa.Boolean(), default=False)

    @classmethod
    def get_by_int_id(cls, int_id: str) -> Select[tuple['Message']]:
        return select(cls).where(int_id == cls.int_id)
