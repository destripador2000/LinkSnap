from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from config.db import get_session
from schemas.link_schema import LinkCreate
from models.url_model import Link
from services.keygen import create_random_key
from sqlmodel import select
from fastapi.responses import RedirectResponse

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

@router.get("/{short_code}")
async def get_link_by_short_code(short_code: str,
                                 session: AsyncSession = Depends(get_session)):

    statement = select(Link).where(Link.short_code == short_code)
    result = await session.execute(statement)
    link_found = result.scalars().first()

    if link_found is None:
        raise HTTPException(status_code=404, detail="Link Not Found")

    return RedirectResponse(link_found.original_url)