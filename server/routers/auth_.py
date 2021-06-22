from uuid import uuid4
from pydantic import BaseModel
from typing import List, Optional
from fastapi import APIRouter, Depends, Response, Cookie
from ..settings import Settings
from ..models import User
from ..schemas import UserSchema
from ..dependencies import get_cache, login_required, Cache

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


class UserLoginForm(BaseModel):
    username: str
    password: str


@router.post(
    "/login/",
    response_model=UserSchema,
)
async def login(
    form: UserLoginForm,
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


@router.get("/me/")
async def me(user=Depends(login_required)):
    return user


@router.get("/logout/")
async def logout(
    response: Response,
    session_id: str = Cookie(None),
    _=Depends(login_required),
    cache: Cache = Depends(get_cache),
):
    await cache.delete(session_id)
    response.delete_cookie("session_id", path="/")
    return {}
