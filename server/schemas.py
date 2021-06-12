from pydantic import root_validator
from tortoise.contrib.pydantic import pydantic_model_creator
from .models import Episode, User, Attributes


BaseEpisodeSchema = pydantic_model_creator(Episode, name="Episode")


class EpisodeSchema(BaseEpisodeSchema):
    @root_validator
    def flatten_attributes(cls, values):
        for attribute_name in map(str.lower, Attributes.types):
            if values.get(attribute_name):
                values[attribute_name] = values[attribute_name].name

        return values


UserSchema = pydantic_model_creator(User, name="User")
for attribute_name in Attributes.types:
    model = getattr(Attributes, attribute_name)
    schema = pydantic_model_creator(model, name=attribute_name)
    setattr(Attributes, f"{attribute_name}Schema", schema)
