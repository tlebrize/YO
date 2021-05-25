from bcrypt import hashpw, gensalt, checkpw
from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer
from ..models import User
from .db import get_db, Connection

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


def get_hashed_password(plain_text_password):
    return hashpw(plain_text_password, gensalt())


def check_password(plain_text_password, hashed_password):
    return checkpw(plain_text_password, hashed_password)


async def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Connection = Depends(get_db),
):
    ...
