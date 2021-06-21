from tortoise.contrib.pydantic import pydantic_model_creator
from tortoise import Tortoise
from pydantic import root_validator
from .main import db_url


async def init_db():
    await Tortoise.init(db_url=db_url, modules={"models": ["server.models"]})
