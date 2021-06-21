from ..models import User
from .tools import pydantic_flattenable_model_creator

UserSchema = pydantic_flattenable_model_creator(User, name="User")
