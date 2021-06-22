from typing import List, Optional
from fastapi import Depends

from ...tools import BaseSchema, from_model, flat
from ...models import Episode, Attributes, User
from ...dependencies import user_optional

from .router import router


@from_model(Episode)
class EpisodeSchema(BaseSchema):
    id: int
    url: str
    thumbnail: str
    title: str
    description: str


class EpisodeDetailsSchema(EpisodeSchema):
    tag: flat(Attributes.Tag)
    series: flat(Attributes.Series)
    duration: flat(Attributes.Duration)
    category: flat(Attributes.Category)
    level: flat(Attributes.Level)
    teacher: flat(Attributes.Teacher)

    favorite: Optional[bool]


@router.get(
    "/",
    response_model=List[EpisodeSchema],
)
async def list(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0,
):
    return await EpisodeSchema.from_queryset(Episode.all())


@router.get("/{uid}/", response_model=EpisodeDetailsSchema)
async def details(
    uid: int,
    user: Optional[User] = Depends(user_optional),
):
    if user:
        episode = await Episode.is_favorite(user).get(id=uid)
    else:
        episode = await Episode.get(id=uid)

    print(user, episode)

    return await EpisodeDetailsSchema.from_tortoise_orm(episode)
