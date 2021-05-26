from uuid import uuid4
from fastapi import APIRouter, Depends, Response, Cookie
from pydantic import BaseModel
from bcrypt import checkpw
from ..models import User
from ..settings import Settings
from ..dependencies import (
    login_required,
    Connection,
    Cache,
    get_cache,
    get_db,
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


def check_password(plain_text_password, hashed_password):
    return checkpw(plain_text_password, hashed_password)


async def authenticate_user(db, username: str, password: str):
    user = await User(db).get(username, with_password=True)
    if not user:
        return False
    if not check_password(password, user["password"]):
        return False
    return user


class LoginForm(BaseModel):
    username: str
    password: str


@router.post("/login/")
async def login_view(
    form: LoginForm,
    response: Response,
    db: Connection = Depends(get_db),
    cache: Cache = Depends(get_cache),
):
    user = await authenticate_user(db, form.username, form.password)
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
    await cache.add(session_id, user["username"])
    return {"user": user["id"]}


@router.get("/me/")
async def me(user=Depends(login_required)):
    return user


@router.get("/logout/")
async def logout_view(
    response: Response,
    session_id: str = Cookie(None),
    _=Depends(login_required),
    cache: Cache = Depends(get_cache),
):
    await cache.delete(session_id)
    response.delete_cookie("session_id", path="/")
    return {}
