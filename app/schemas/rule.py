from pydantic import BaseModel


class Rule(BaseModel):
    keyword: str
    match_type: str
    category: str
    priority: int
    is_active: bool

    user_id: int
    category_id: int
