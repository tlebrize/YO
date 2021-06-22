from fastapi import Response, Cookie, Depends
from ...dependencies import login_required, Cache, get_cache

from .router import router


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
