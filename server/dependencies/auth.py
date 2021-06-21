from fastapi import Depends, Request, HTTPException
from bcrypt import hashpw, gensalt
from ..models import User
from .cache import get_cache, Cache


async def get_current_user(
    session_id,
    cache: Cache = Depends(get_cache),
):
    username = await cache.get(session_id)
    return await User.get(username=username)


async def login_required(
    request: Request,
    cache: Cache = Depends(get_cache),
):
    session_id = request.cookies.get("session_id")
    if not session_id:
        raise HTTPException(status_code=401, detail="Not Authenticated.")
    user = await get_current_user(session_id, cache)
    if not user:
        raise HTTPException(status_code=401, detail="Not Authenticated.")
    return user
