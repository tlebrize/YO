from fastapi import Depends, Request, HTTPException
from bcrypt import hashpw, gensalt
from ..models import User
from .db import get_db, Connection
from .cache import get_cache, Cache


def get_hashed_password(plain_text_password):
    return hashpw(plain_text_password, gensalt())


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
