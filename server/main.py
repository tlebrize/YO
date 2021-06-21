from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from tortoise.contrib.fastapi import register_tortoise

from .settings import Settings

Tortoise.init_models(["server.models"], "models")
from .routers import episode, auth
from .load_data import load_data

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(episode)
app.include_router(auth)


@app.get("/load_data/")
async def load_data_view():
    await load_data()


db_url = "postgres://yo:securepasswd@0.0.0.0:5432/yo"

TORTOISE_ORM = {
    "connections": {"default": db_url},
    "apps": {
        "models": {
            "models": ["server.models", "aerich.models"],
            "default_connection": "default",
        },
    },
}

register_tortoise(
    app,
    db_url=db_url,
    modules={"models": ["server.models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)
