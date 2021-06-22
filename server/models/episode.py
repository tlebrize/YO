from __future__ import annotations

from tortoise.models import Model
from tortoise.manager import Manager
from tortoise import fields
from tortoise.queryset import QuerySet
from tortoise.expressions import F
from .attributes import Attributes


class EpisodesAttributes:
    pass


for attribute_name in Attributes.types:
    foreign_key = fields.ForeignKeyField(
        f"models.{attribute_name}",
        related_name="episodes",
        null=True,
    )
    setattr(EpisodesAttributes, attribute_name.lower(), foreign_key)


class Episode(Model, EpisodesAttributes):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=511)
    thumbnail = fields.CharField(max_length=511)
    title = fields.CharField(max_length=511)
    description = fields.TextField()

    favorites = fields.ManyToManyField("models.User")

    @classmethod
    async def list(cls, limit=None, offset=None) -> QuerySet[Episode]:
        limit = min(max(0, limit), 50) if limit else 50
        offset = offset or 0
        return cls.all().limit(limit).offset(offset)
