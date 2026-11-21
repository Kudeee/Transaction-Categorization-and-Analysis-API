import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Category(Base):
    __tablename__ = "categories"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("now()"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete=("CASCADE")))

    owner: Mapped["User"] = relationship(back_populates="categories")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
    categorization_rules: Mapped[List["Categorization_Rule"]] = relationship(  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
        back_populates="category"
    )
    transactions: Mapped[List["Transaction"]] = relationship(back_populates="category")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
