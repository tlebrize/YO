from tortoise.models import Model
from tortoise import fields


class Attributes:
    types = [
        "Category",
        "Duration",
        "Level",
        "Series",
        "Teacher",
        "Tag",
    ]


class AttributeBaseModel(Model):
    name = fields.CharField(max_length=255)
    id = fields.IntField(pk=True)


for attribute_name in Attributes.types:
    model = type(
        attribute_name,
        (AttributeBaseModel,),
        {},
    )
    setattr(Attributes, attribute_name, model)
