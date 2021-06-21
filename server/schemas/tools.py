from tortoise.contrib.pydantic import pydantic_model_creator
from pydantic import root_validator


def pydantic_flattenable_model_creator(*args, to_flatten=None, **kwargs):
    model = pydantic_model_creator(*args, **kwargs)

    class FlattenableSchema(model):
        @root_validator(allow_reuse=True)
        def flatten_attributes(cls, values):
            for attribute_name in to_flatten or []:
                if values.get(attribute_name):
                    values[attribute_name] = values[attribute_name].name

            return values

    return FlattenableSchema


def exclude_fk_id(fks):
    fks_id = [f"{fk}_id" for fk in fks]
    return fks + fks_id
