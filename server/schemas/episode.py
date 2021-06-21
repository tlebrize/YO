from ..models import Episode
from .tools import pydantic_flattenable_model_creator, exclude_fk_id

EpisodeSchema = pydantic_flattenable_model_creator(Episode, name="Episode")
EpisodeSeriesSchema = pydantic_flattenable_model_creator(
    Episode,
    name="EpisodeSeries",
    to_flatten=["series", "duration"],
    exclude=exclude_fk_id(["tag", "level", "teacher", "category"]),
)
