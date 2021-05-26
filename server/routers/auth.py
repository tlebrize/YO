from fastapi import APIRouter, Depends, Response, Cookie
from pydantic import BaseModel
from ..dependencies import (
    login_required,
    login,
    Connection,
    Cache,
    get_cache,
    get_db,
    logout,
)

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


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
    user = await login(
        form.username,
        form.password,
        response=response,
        db=db,
        cache=cache,
    )
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
    await logout(
        session_id,
        response=response,
        cache=cache,
    )
    return {}
