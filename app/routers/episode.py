from fastapi import APIRouter, Depends, Query
from typing import Optional
from ..models import Episode, Attribute
from ..dependencies import get_db, Connection

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


FILTER_CHOICES_REGEX = "|".join(Attribute.ATTRIBUTES_LIST)


@router.get("/filter/{attribute}/{uid}/")
async def filter(
    uid: int,
    attribute: str = Query(..., regex=FILTER_CHOICES_REGEX),
    db: Connection = Depends(get_db),
):
    return await Episode(db).filter(attribute, uid)


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
