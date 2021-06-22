from fastapi import Depends

from .router import router
from ...models import User
from ...tools import BaseSchema, from_model
from ...dependencies import login_required


@from_model(User)
class UserSchema(BaseSchema):
    username: str
    id: int


@router.get("/me/", response_model=UserSchema)
async def me(user=Depends(login_required)):
    return UserSchema.from_orm(user)
