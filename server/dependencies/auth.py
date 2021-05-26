from uuid import uuid4
from bcrypt import hashpw, gensalt, checkpw
from fastapi import Depends, Request, HTTPException, Response
from ..models import User
from .db import get_db, Connection
from .cache import get_cache, Cache
from ..settings import Settings


def get_hashed_password(plain_text_password):
    return hashpw(plain_text_password, gensalt())


def check_password(plain_text_password, hashed_password):
    return checkpw(plain_text_password, hashed_password)


async def authenticate_user(db, username: str, password: str):
    user = await User(db).get(username, with_password=True)
    if not user:
        return False
    if not check_password(password, user["password"]):
        return False
    return user


async def get_current_user(
    session_id,
    cache: Cache = Depends(get_cache),
    db: Connection = Depends(get_db),
):
    username = await cache.get(session_id)
    return await User(db).get(username)


async def login_required(
    request: Request,
    cache: Cache = Depends(get_cache),
    db: Connection = Depends(get_db),
):
    session_id = request.cookies.get("session_id")
    if not session_id:
        raise HTTPException(status_code=401, detail="Not Authenticated.")
    user = await get_current_user(session_id, cache, db)
    if not user:
        raise HTTPException(status_code=401, detail="Not Authenticated.")
    return user


async def login(
    username,
    password,
    response: Response,
    db: Connection = Depends(get_db),
    cache: Cache = Depends(get_cache),
):
    user = await authenticate_user(db, username, password)
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
    return user


async def logout(
    session_id,
    response: Response,
    cache: Cache = Depends(get_cache),
):
    await cache.delete(session_id)
    response.delete_cookie("session_id", path="/")
