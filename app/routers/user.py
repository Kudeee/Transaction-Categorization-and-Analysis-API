from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError

from ..database import SessionDep
from ..models.user import User as UserModel
from ..schemas.user import User as UserSchema
from ..schemas.user import UserResponse
from ..utils import oauth2, password

router = APIRouter(prefix="/user")


@router.post(
    "/register/", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register(user: UserSchema, db: SessionDep):

    try:
        hash_password = password.hash_password(user.password)
        user.password = hash_password

        new_user = UserModel(**user.model_dump())

        db.add(new_user)
        db.commit()
        db.refresh(new_user)

        return new_user
    except IntegrityError:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="email already in use."
        )


@router.get("/me")
def get_current_user(current_user: Annotated[int, Depends(oauth2.get_current_user)]):
    return current_user
