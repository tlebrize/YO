from pydantic import root_validator, BaseModel
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Episode, User, Attributes


def pydantic_flattenable_model_creator(*args, exclude=None, **kwargs):
    model = pydantic_model_creator(*args, exclude=exclude or (), **kwargs)

    class FlattenableSchema(model):
        @classmethod
        def to_flatten(cls):
            nonlocal exclude
            exclude = exclude or {}
            return set(map(str.lower, Attributes.types)) ^ set(exclude)

        @root_validator(allow_reuse=True)
        def flatten_attributes(cls, values):
            relations = cls.to_flatten()
            for attribute_name in relations:
                if values.get(attribute_name):
                    values[attribute_name] = values[attribute_name].name

            return values

    return FlattenableSchema


EpisodeSchema = pydantic_flattenable_model_creator(Episode, name="Episode")
EpisodeSeriesSchema = pydantic_flattenable_model_creator(
    Episode,
    name="Episode",
    # exclude=["tag"],
)


UserSchema = pydantic_model_creator(User, name="User")

for attribute_name in Attributes.types:
    model = getattr(Attributes, attribute_name)
    schema = pydantic_model_creator(model, name=attribute_name)
    setattr(Attributes, f"{attribute_name}Schema", schema)
