from pydantic import BaseModel


class Summary(BaseModel):
    summary: str
    categorized_summary: str
