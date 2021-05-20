from typing import AsyncGenerator
from aiosqlite import Connection, connect


async def wrapper(connection):
    async def get_many(query, fields, args=None):
        data = []
        async with connection.execute(query, args) as cursor:
            async for row in cursor:
                data.append({key: value for key, value in zip(fields, row)})
        return data

    connection.get_many = get_many

    async def get_one(query, fields, args=None):
        async with connection.execute(query, args) as cursor:
            row = await cursor.fetchone()
        if not row:
            raise Exception("not_found")
        return {key: value for key, value in zip(fields, row)}

    connection.get_one = get_one

    return connection


async def get_db() -> AsyncGenerator[Connection, None]:
    async with connect("db.sqlite3") as db:
        yield await wrapper(db)
