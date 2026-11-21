import datetime
from decimal import Decimal

from sqlalchemy import ForeignKey, Numeric, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Transaction(Base):
    __tablename__ = "transactions"

    id: Mapped[int] = mapped_column(primary_key=True)
    transaction_date: Mapped[datetime.datetime]
    description: Mapped[str]
    amount: Mapped[Decimal] = mapped_column(Numeric(10, 2))
    reference: Mapped[str | None]
    fingerprint: Mapped[int]
    categorization_source: Mapped[str]
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("now()"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))
    import_id: Mapped[int] = mapped_column(ForeignKey("imports.id", ondelete="CASCADE"))
    category_id: Mapped[int] = mapped_column(
        ForeignKey("categories.id", ondelete="CASCADE")
    )

    category: Mapped["Category"] = relationship(back_populates="transactions")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
    imports: Mapped["Import"] = relationship(back_populates="transactions")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
    owner: Mapped["User"] = relationship(back_populates="transactions")  # noqa: F821, UP037  # pyright: ignore[reportUndefinedVariable]
