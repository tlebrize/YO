from fastapi import FastAPI, Depends, Response, Cookie
from pydantic import BaseModel
from .routers import episode, attribute
from .settings import Settings
from .dependencies import (
    login_required,
    login,
    Connection,
    Cache,
    get_cache,
    get_db,
    logout,
)

app = FastAPI()

app.include_router(episode)
app.include_router(attribute)


@app.get("/")
def root():
    return {
        "search": f"{Settings.HOST}/episode/search/?query=yoga",
        "by attributes": f"{Settings.HOST}/attribute/",
    }


class LoginForm(BaseModel):
    username: str
    password: str


@app.post("/login/")
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


@app.get("/me/")
async def me(user=Depends(login_required)):
    return user


@app.get("/logout/")
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
