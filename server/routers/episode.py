from fastapi import APIRouter, Depends
from typing import Optional
from ..models import Episode
from ..dependencies import get_db, Connection

router = APIRouter(
    prefix="/episode",
    tags=["episode"],
)


@router.get("/")
async def list(
    db: Connection = Depends(get_db),
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
):

    data = await Episode(db).list(limit, offset)
    return {"count": len(data), "episodes": data}


@router.get("/search/")
async def search(
    query: str,
    db: Connection = Depends(get_db),
):
    data = await Episode(db).search(query)
    return {"count": len(data), "episodes": data}


@router.get("/{uid}/")
async def get(
    uid: int,
    db: Connection = Depends(get_db),
):
    return await Episode(db).get(uid)
