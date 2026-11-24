from fastapi import FastAPI

from .routers import auth, category, user

app = FastAPI()

app.include_router(user.router)
app.include_router(auth.router)
app.include_router(category.router)


@app.get("/")
def healthCheck():
    return {"health": "ok"}
