import datetime  # noqa: N999

from sqlalchemy import ForeignKey, text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..database import Base


class Import(Base):
    __tablename__ = "imports"

    id: Mapped[int] = mapped_column(primary_key=True)
    filename: Mapped[str]
    status: Mapped[str]
    total_rows: Mapped[int] = mapped_column(default=0)
    imported_rows: Mapped[int] = mapped_column(default=0)
    duplicate_rows: Mapped[int] = mapped_column(default=0)
    rejected_rows: Mapped[int] = mapped_column(default=0)
    created_at: Mapped[datetime.datetime] = mapped_column(server_default=text("now()"))

    user_id: Mapped[int] = mapped_column(ForeignKey("users.id", ondelete="CASCADE"))

    owner: Mapped["User"] = relationship(back_populates="imports")  # pyright: ignore[reportUndefinedVariable]  # noqa: F821, UP037
    transactions: Mapped["Transaction"] = relationship(back_populates="imports")  # pyright: ignore[reportUndefinedVariable]  # noqa: F821, UP037
