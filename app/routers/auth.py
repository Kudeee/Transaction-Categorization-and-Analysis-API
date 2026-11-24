from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm

from ..database import SessionDep
from ..models.user import User as UserModel
from ..schemas.auth import Token
from ..utils.oauth2 import create_access_token
from ..utils.password import verify_password

router = APIRouter()


@router.post("/login/", response_model=Token)
def login(
    user_credentials: Annotated[OAuth2PasswordRequestForm, Depends()], db: SessionDep
):
    user = (
        db.query(UserModel).filter(UserModel.email == user_credentials.username).first()
    )

    if not user:
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password"
        )

    if not verify_password(user_credentials.password, user.password):
        raise HTTPException(
            status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or passworda"
        )

    access_token = create_access_token({"id": user.id})
    return {"access_token": access_token, "token_type": "bearer"}
