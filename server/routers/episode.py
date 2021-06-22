from __future__ import annotations

from typing import List, Optional
from fastapi import APIRouter, Depends
from ..models import Episode, Attributes
from ..schemas import EpisodeSchema, EpisodeSeriesSchema

router = APIRouter(
    prefix="/episode",
    tags=["episode"],
)


@router.get(
    "/",
    response_model=List[EpisodeSchema],
)
async def list(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
):
    return await EpisodeSchema.from_queryset(Episode.all())


@router.get(
    "/series/",
    response_model=List[List[EpisodeSeriesSchema]],
)
async def get(
    limit: Optional[int] = 3,
    offset: Optional[int] = 0,
):
    page = []
    series = await Attributes.Series.all().order_by("-id").limit(limit).offset(offset)

    for s in series:
        page.append(await EpisodeSeriesSchema.from_queryset(s.episodes.all()))
    return page


@router.get(
    "/{uid}/",
    response_model=EpisodeSchema,
)
async def get(
    uid: int,
):
    return await EpisodeSchema.from_queryset_single(Episode.get(id=uid))
