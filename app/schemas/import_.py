from pydantic import BaseModel


class Import(BaseModel):
    filename: str
    rows_detected: int
    imported_transaction_count: int
    duplicate_count: int
    rejected_row_count: int
    import_status: str
