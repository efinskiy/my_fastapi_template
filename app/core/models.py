from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import func
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import declared_attr


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)

    @declared_attr
    def __tablename__(self) -> str:
        return self.__name__.lower()


class User(Base):
    first_name: Mapped[str]
    second_name: Mapped[str]
    last_name: Mapped[str]
    phone_number: Mapped[str]

    telegram_id: Mapped[Optional[str]] = mapped_column(nullable=True)
    email: str

    notification_email: Mapped[bool] = mapped_column(default=False)
    notification_telegram: Mapped[bool] = mapped_column(default=False)

