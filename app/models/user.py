import datetime

from sqlalchemy import text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(
        primary_key=True,
    )
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("now()"))

    imports: Mapped[List["Import"]] = relationship(back_populates="owner")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
    categories: Mapped[List["Category"]] = relationship(back_populates="owner")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
    categorization_rules: Mapped[List["Categorization_Rules"]] = relationship(  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
        back_populates="owner"
    )
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="owner")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
