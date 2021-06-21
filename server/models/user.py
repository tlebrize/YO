from __future__ import annotations

from typing import Optional
from bcrypt import hashpw, gensalt, checkpw
from tortoise.models import Model
from tortoise import fields


class User(Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=511)
    password = fields.CharField(max_length=511)

    @classmethod
    def get_hashed_password(cls, plain_text_password: str) -> str:
        return hashpw(plain_text_password, gensalt())

    @classmethod
    def check_password(
        cls,
        plain_text_password: str,
        hashed_password: str,
    ) -> str:
        return checkpw(plain_text_password, hashed_password)

    @classmethod
    async def authenticate(
        cls,
        username: str,
        password: str,
    ) -> Optional[User]:
        user = await User.get(username=username)
        if not user:
            return None
        if not cls.check_password(password, user.password):
            return None
        return user

    @classmethod
    async def create(cls, **kwargs) -> User:
        kwargs["password"] = cls.get_hashed_password(kwargs["password"])
        return await super().create(**kwargs)
