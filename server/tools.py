import pydantic
from typing import Union
from pydantic import root_validator
from tortoise.contrib.pydantic.base import PydanticModel, _get_fetch_fields
from tortoise import Tortoise
from .settings import Settings


async def init_db():
    await Tortoise.init(db_url=Settings.DB_URL, modules={"models": ["server.models"]})


def from_model(model):
    def decorator(cls):
        cls.__config__.orig_model = model
        return cls

    return decorator


class BaseSchema(PydanticModel):
    @classmethod
    async def from_queryset(cls, queryset):
        fetch_fields = _get_fetch_fields(cls, queryset.model)
        return [
            cls.from_orm(obj) for obj in await queryset.prefetch_related(*fetch_fields)
        ]

    @classmethod
    async def from_tortoise_orm(cls, obj):
        fetch_fields = _get_fetch_fields(cls, obj.__class__)
        await obj.fetch_related(*fetch_fields)
        return super().from_orm(obj)

    @root_validator(pre=True)
    def flatten(cls, values):
        for name, value in values.items():
            if isinstance(value, dict) and value.get("flat"):
                values[name] = value["name"]
        return values


def flat(model):
    @from_model(model)
    class FlatSchema(BaseSchema):
        name: str
        flat = True

    return Union[FlatSchema, str]
