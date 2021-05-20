from fastapi import APIRouter, Depends, Query
from ..models import Attribute
from ..dependencies import get_db, Connection
from ..settings import HOST

router = APIRouter(
    prefix="/attribute",
    tags=["attribute"],
)


@router.get("/")
async def list(db: Connection = Depends(get_db)):
    data = await Attribute(db).list()
    for name, details in data.items():
        for attribute in details:
            attribute["link"] = f'{HOST}/attribute/{name}/{attribute["id"]}'

    return data


@router.get("/{attribute}/{uid}/")
async def get(
    uid: int,
    attribute: str = Query(..., regex=Attribute.FILTER_CHOICES_REGEX),
    db: Connection = Depends(get_db),
):
    data = await Attribute(db).get(attribute, uid)
    for episode in data:
        episode['details'] = f'{HOST}/episode/{episode["episode_id"]}/'

    return {"count": len(data), "episodes": data}
