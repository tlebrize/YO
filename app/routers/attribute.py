from aiosqlite import Connection
from fastapi import APIRouter, Depends
from ..models import Attributes
from ..dependencies import get_db

router = APIRouter(
    prefix="/attribute",
    tags=["attribute"],
)


@router.get("/")
async def get(db: Connection = Depends(get_db)):
    data = await Attributes(db).list()
    return data
