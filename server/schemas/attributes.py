from ..models import Attributes
from .tools import pydantic_flattenable_model_creator

for attribute_name in Attributes.types:
    model = getattr(Attributes, attribute_name)
    schema = pydantic_flattenable_model_creator(model, name=attribute_name)
    setattr(Attributes, f"{attribute_name}Schema", schema)
