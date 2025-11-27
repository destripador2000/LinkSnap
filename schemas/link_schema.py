from sqlmodel import SQLModel

class LinkCreate(SQLModel):
    original_url: str