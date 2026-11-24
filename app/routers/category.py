from typing import Annotated

from fastapi import APIRouter, Depends

from ..database import SessionDep
from ..models.category import Category as CategoryModel
from ..schemas.category import Category as CategorySchema
from ..utils.oauth2 import get_current_user

router = APIRouter(prefix="/categories")


@router.get("", response_model=list[CategorySchema])
def get_categories(
    db: SessionDep, current_user: Annotated[int, Depends(get_current_user)]
):
    categories = db.query(CategoryModel).filter(
        CategoryModel.user_id == current_user.id  # pyright: ignore[reportAttributeAccessIssue]
    )

    return categories
