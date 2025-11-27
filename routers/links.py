from fastapi import APIRouter
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_session
from schemas.link_schema import LinkCreate
from models.url_model import Link
from services.keygen import create_random_key

router = APIRouter()

@router.post("/")
async def link_create(link_data: LinkCreate,
                      session: AsyncSession = Depends(get_session)):

    key = create_random_key()

    new_link = Link(
        original_url = link_data.original_url,
        short_code = key
    )

    session.add(new_link)
    await session.commit()
    await session.refresh(new_link)
    return new_link