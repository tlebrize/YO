from enum import Enum
from pydantic import BaseModel as BaseSchema
from fastapi import Depends

from .router import router
from ...models import User, Episode
from ...dependencies import login_required


class FavoriteStatusEnum(str, Enum):
    added = "added"
    removed = "removed"


class FavoriteStatusSchema(BaseSchema):
    status: FavoriteStatusEnum


@router.post("/{uid}/favorite/", response_model=FavoriteStatusSchema)
async def favorite(uid: int, user: User = Depends(login_required)):
    episode = await Episode.get(id=uid)
    if not await user.favorites.filter(id=uid).exists():
        await user.favorites.add(episode)
        status = "added"
    else:
        await user.favorites.remove(episode)
        status = "removed"

    return {"status": status}
