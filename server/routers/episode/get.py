from typing import List, Optional

from ...tools import BaseSchema
from ...models import Episode

from .router import router


class EpisodeSchema(BaseSchema):
    id: int
    url: str
    thumbnail: str
    title: str
    description: str


@router.get(
    "/",
    response_model=List[EpisodeSchema],
)
async def get(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
):
    return await EpisodeSchema.from_queryset(Episode.all())
