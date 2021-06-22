from uuid import uuid4
from fastapi import Depends, Response
from ...dependencies import Cache, get_cache
from ...tools import BaseSchema, from_model
from ...models import User
from ...settings import Settings

from .router import router


@from_model(User)
class LoginFormSchema(BaseSchema):
    username: str
    password: str


@from_model(User)
class UserSchema(BaseSchema):
    username: str
    id: int


@router.post(
    "/login/",
    response_model=UserSchema,
)
async def login(
    form: LoginFormSchema,
    response: Response,
    cache: Cache = Depends(get_cache),
):
    user = await User.authenticate(form.username, form.password)
    if not user:
        return False
    session_id = uuid4().hex
    response.set_cookie(
        "session_id",
        session_id,
        path="/",
        secure=not Settings.DEBUG,
        httponly=True,
        samesite="strict",
    )
    await cache.add(session_id, user.username)
    return UserSchema.from_orm(user)
