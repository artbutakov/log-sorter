from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from app.config.connection import Base


class Log(Base):
    __tablename__ = 'log'

    pk_id: Mapped[int] = mapped_column(sa.Integer, primary_key=True, autoincrement=True)
    created: Mapped[datetime] = mapped_column(sa.DateTime(timezone=False))
    int_id: Mapped[str] = mapped_column(sa.String(16), nullable=True)
    string: Mapped[str] = mapped_column(sa.String())
    address: Mapped[str] = mapped_column(sa.String(), nullable=True)

    __table_args__ = (
        sa.Index('log_address_idx', address, postgresql_using='HASH'),
    )
