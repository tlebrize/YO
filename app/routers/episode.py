from fastapi import APIRouter, Depends
from typing import Optional
from aiosqlite import Connection
from ..models import Episode
from ..dependencies import get_db

router = APIRouter(
    prefix="/episode",
    tags=["episode"],
)


@router.get("/")
async def list(
    db: Connection = Depends(get_db),
    limit: Optional[int] = None,
    offset: Optional[int] = None,
):

    data = await Episode(db).list(limit, offset)
    return {"count": len(data), "episodes": data}


@router.get("/{uid}/")
async def get(uid: int, db: Connection = Depends(get_db)):
    data = await Episode(db).get(uid)
    return data
