from typing import List, Optional
from fastapi import APIRouter, Depends
from ..models import Episode
from ..schemas import EpisodeSchema

router = APIRouter(
    prefix="/episode",
    tags=["episode"],
)


@router.get("/")
async def list(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
    response_model=List[EpisodeSchema],
):
    return await EpisodeSchema.from_queryset(Episode.all())
