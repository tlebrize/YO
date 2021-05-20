from typing import AsyncGenerator, Optional
from fastapi import FastAPI, Depends
from aiosqlite import Connection, connect

from .models import Episode, Attributes

app = FastAPI()


async def get_db() -> AsyncGenerator[Connection, None]:
    async with connect("db.sqlite3") as db:
        yield db


@app.get("/episode/")
async def list(
    db: Connection = Depends(get_db),
    limit: Optional[int] = None,
    offset: Optional[int] = None,
):

    data = await Episode(db).list(limit, offset)

    return {"count": len(data), "episodes": data}


@app.get("/episode/{uid}/")
async def get(uid: int, db: Connection = Depends(get_db)):
    data = await Episode(db).get(uid)
    return data


@app.get("/attributes/")
async def get(db: Connection = Depends(get_db)):
    data = await Attributes(db).list()
    return data
