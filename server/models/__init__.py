from .episode import Episode
from .user import User
from .attributes import Attributes

__all__ = [
    Episode,
    User,
    Attributes,
]

attributes_models = [
    getattr(Attributes, attribute_name) for attribute_name in Attributes.types
]


__models__ = __all__ + attributes_models
