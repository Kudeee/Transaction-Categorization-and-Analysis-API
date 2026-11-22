from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class Transaction(BaseModel):
    description: str
    amount: Decimal
    reference: str | None
    categorization_source: str
    transaction_date: datetime

    import_id: int
    category_id: int
