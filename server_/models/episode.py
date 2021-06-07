from tortoise.models import Models
from tortoise import fields


class Episode(Models):
    id = fields.IntField(pk=True)
    url = fields.CharField(max_length=511)
    thumbnail = fields.CharField(max_length=511)
    title = fields.CharField(max_length=511)
    description = fields.TextField()
