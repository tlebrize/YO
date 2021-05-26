from collections import defaultdict
from fastapi import APIRouter, Depends, Query
from ..models import Attribute
from ..dependencies import get_db, Connection
from ..settings import Settings

router = APIRouter(
    prefix="/attribute",
    tags=["attribute"],
)


@router.get("/")
async def _list(db: Connection = Depends(get_db)):
    data = await Attribute(db).list()
    for name, details in data.items():
        for attribute in details:
            attribute["link"] = f'{Settings.HOST}/attribute/{name}/{attribute["id"]}'

    return data


@router.get("/series/")
async def series_list(db: Connection = Depends(get_db)):
    data = defaultdict(list)
    series_list = await Attribute(db).series_list()

    for series in series_list:
        data[series["series"]].append(series)

    return data


@router.get("/{attribute}/{uid}/")
async def get(
    uid: int,
    attribute: str = Query(..., regex=Attribute.FILTER_CHOICES_REGEX),
    db: Connection = Depends(get_db),
):
    data = await Attribute(db).get(attribute, uid)
    for episode in data:
        episode["details"] = f'{Settings.HOST}/episode/{episode["episode_id"]}/'

    return {"count": len(data), "episodes": data}
