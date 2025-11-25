from datetime import datetime
from typing import Optional
from sqlmodel import Field

# Creando tabla Link para almacenar los links que entrarán
class Link:
    __tablename__ = 'links'
    id: Optional[int] = Field(default=None, primary_key=True)
    original_url: str
    short_code: str = Field(unique=True, index=True)
    visit_count: int = Field(default=0)
    created_at: datetime = Field(default=datetime.now())