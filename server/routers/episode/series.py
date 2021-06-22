from typing import Optional, List

from .router import router
from ...tools import BaseSchema, from_model, flat
from ...models import Episode, Attributes


@from_model(Episode)
class EpisodeSeriesSchema(BaseSchema):
    id: int
    url: str
    thumbnail: str
    title: str
    description: str
    series: flat(Attributes.Series)
    duration: flat(Attributes.Duration)


@router.get(
    "/series/",
    response_model=List[List[EpisodeSeriesSchema]],
)
async def series(
    limit: Optional[int] = 3,
    offset: Optional[int] = 0,
):
    page = []
    series = await Attributes.Series.all().order_by("-id").limit(limit).offset(offset)

    for s in series:
        page.append(await EpisodeSeriesSchema.from_queryset(s.episodes.all()))
    return page
