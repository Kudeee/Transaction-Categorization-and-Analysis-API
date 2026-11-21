from fastapi import FastAPI
from sqlalchemy import text

from .database import SessionDep

app = FastAPI()


@app.get("/")
def healthCheck():
    return {"health": "ok"}
