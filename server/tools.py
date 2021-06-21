from tortoise import Tortoise
from .main import db_url


async def init_db():
    await Tortoise.init(db_url=db_url, modules={"models": ["server.models"]})
