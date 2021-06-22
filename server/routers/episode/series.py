from typing import Optional, List
from pydantic import BaseModel as BasePySchema

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


class EpisodeSeriesContainerSchema(BasePySchema):
    next: Optional[str]
    data: List[List[EpisodeSeriesSchema]]


@router.get(
    "/series/",
    response_model=EpisodeSeriesContainerSchema,
)
async def series(
    limit: Optional[int] = 3,
    offset: Optional[int] = 0,
):
    data = []
    series = await Attributes.Series.all().order_by("-id").limit(limit).offset(offset)

    for s in series:
        data.append(await EpisodeSeriesSchema.from_queryset(s.episodes.all()))

    if await Attributes.Series.all().count() > offset + limit:
        next = f"/episode/series/?limit={limit}&offset={offset+limit}"
    else:
        next = None

    return {
        "next": next,
        "data": data,
    }
