from fastapi import APIRouter, Depends
from ..models import Attribute
from ..dependencies import get_db, Connection

router = APIRouter(
    prefix="/attribute",
    tags=["attribute"],
)


@router.get("/")
async def get(db: Connection = Depends(get_db)):
    data = await Attribute(db).list()
    return data
