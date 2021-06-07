from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise.contrib.fastapi import register_tortoise

from .settings import Settings
from .models import Episode, EpisodeSchema


app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
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


@app.get("/episodes/", response_model=List[EpisodeSchema])
async def read_notes():
    return await Episode.all()
