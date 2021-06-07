from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from tortoise import Tortoise
from .routers import episode, attribute, auth
from .settings import Settings


await Tortoise.init(
    db_url="postgresql://yo_user:securepasswd@0.0.0.0:5432",
    modules={"models": ["models", "aerich.models"]},
)

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=Settings.ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(episode)
app.include_router(attribute)
app.include_router(auth)


@app.get("/")
def root():
    return {
        "search": f"{Settings.HOST}/episode/search/?query=yoga",
        "by attributes": f"{Settings.HOST}/attribute/",
    }
