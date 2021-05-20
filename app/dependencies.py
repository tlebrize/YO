from typing import AsyncGenerator
from aiosqlite import Connection, connect


async def get_db() -> AsyncGenerator[Connection, None]:
    async with connect("db.sqlite3") as db:
        yield db
