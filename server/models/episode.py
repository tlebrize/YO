from tortoise.models import Model
from tortoise import fields
from tortoise.contrib.pydantic import pydantic_model_creator


class Episode(Model):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=511)
    thumbnail = fields.CharField(max_length=511)
    title = fields.CharField(max_length=511)
    description = fields.TextField()


EpisodeSchema = pydantic_model_creator(Episode, name="Episode")
