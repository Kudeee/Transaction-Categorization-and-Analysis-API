import datetime

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Categorization_Rule(Base):
    __tablename__ = "categorization_rules"

    id: Mapped[int] = mapped_column(primary_key=True)
    keyword: Mapped[str]
    match_type: Mapped[str]
    priority: Mapped[int]
    is_active: Mapped[bool]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("now()"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE")
    )

    owner: Mapped["User"] = relationship(back_populates="categorization_rules")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
    category: Mapped["Category"] = relationship(back_populates="categorization_rules")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
