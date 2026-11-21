import datetime
from typing import Annotated

from fastapi import Depends
from sqlalchemy import TIMESTAMP, create_engine
from sqlalchemy.orm import DeclarativeBase, Session, sessionmaker

from .config import settings

SQL_DATABASE_URL = f"{settings.DATABASE_URL}"

engine = create_engine(SQL_DATABASE_URL)

SessionLocal = sessionmaker(autoflush=False, bind=engine)


class Base(DeclarativeBase):
    type_annotation_map = {datetime.datetime: TIMESTAMP(timezone=True)}  # noqa: RUF012


def get_session():
    with SessionLocal() as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
