from fastapi import APIRouter, HTTPException, status

from ..database import SessionDep
from ..models.user import User as UserModel
from ..schemas.user import User as UserSchema
from ..schemas.user import UserResponse
from ..utils import password

router = APIRouter(prefix="/user")


@router.post(
    "/register/", status_code=status.HTTP_201_CREATED, response_model=UserResponse
)
def register(user: UserSchema, db: SessionDep):

    hash_password = password.hash_password(user.password)
    user.password = hash_password

    new_user = UserModel(**user.model_dump())

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user
