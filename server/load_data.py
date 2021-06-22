import json, re
from .models import Attributes, Episode

URL_TO_ID = re.compile(r"https:\/\/player\.vimeo\.com\/video\/(?P<id>[0-9]*)")


def tojson(p):
    with open(p) as fd:
        return json.load(fd)


def extract_categories(episodes):
    categories_data = tojson("data/categories.json")
    for C in categories_data:
        for S in C["series"]:
            E = S["serie"]["episodes"]
            for index, episode in enumerate(E):
                uid = URL_TO_ID.search(episode["url"])["id"]
                bodypart = episode.pop("bodyparts")
                episodes[uid] = {
                    **episode,
                    "url": f"https://player.vimeo.com/video/{uid}",
                    "category": C["name"],
                    "series": S["title"],
                    "series_index": index,
                    "bodypart": bodypart,
                }

    return episodes


async def insert_episodes(episodes):
    foreign_keys = {
        "teacher": {},
        "duration": {},
        "level": {},
        "category": {},
        "series": {},
        "tag": {},
    }

    attributes_models = {
        attribute_name: getattr(Attributes, attribute_name.capitalize())
        for attribute_name in foreign_keys.keys()
    }

    for uid, episode in episodes.items():

        for field in foreign_keys.keys():
            if not (episode[field] in foreign_keys[field].keys()):
                relation_id = (
                    await attributes_models[field].create(name=episode[field])
                ).id

                foreign_keys[field][episode[field]] = relation_id
            else:
                relation_id = foreign_keys[field][episode[field]]

            episode[f"{field}_id"] = relation_id
            del episode[field]

        await Episode.create(id=int(uid), **episode)


async def load_data():
    if Episode.all().exists():
        return 0
    episodes = extract_categories({})
    await insert_episodes(episodes)
    return await Episode.all().count()
