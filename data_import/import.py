import json, re, sqlite3
from sql import create_tables, inserts, views, fts

URL_TO_ID = re.compile(r"https:\/\/player\.vimeo\.com\/video\/(?P<id>[0-9]*)")


def tojson(p):
    with open(p) as fd:
        return json.load(fd)


def extract_categories(episodes):
    categories_data = tojson("data_import/data/categories.json")

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


def init_db(cur):
    for statement in create_tables.statements:
        cur.execute(statement)


def insert_episodes(cur, episodes):
    foreign_keys = {
        "teacher": {},
        "duration": {},
        "level": {},
        "category": {},
        "series": {},
    }

    many_to_many = {
        "bodypart": {},
    }

    for uid, episode in episodes.items():

        for field in foreign_keys.keys():
            if not (episode[field] in foreign_keys[field].keys()):
                cur.execute(
                    inserts.SIMPLE_INSERT(field),
                    {"name": episode[field]},
                )
                cur.execute(inserts.GET_LAST_ID)
                relation_id = cur.fetchone()[0]

                foreign_keys[field][episode[field]] = relation_id
            else:
                relation_id = foreign_keys[field][episode[field]]

            episode[field] = relation_id

        for field, relations in many_to_many.items():
            for item in episode[field]:
                if not (item in many_to_many[field].keys()):
                    cur.execute(
                        inserts.SIMPLE_INSERT(field),
                        {"name": item},
                    )
                    cur.execute(inserts.GET_LAST_ID)
                    relation_id = cur.fetchone()[0]

                    many_to_many[field][item] = relation_id
                else:
                    relation_id = many_to_many[field][item]

                cur.execute(
                    inserts.INSERT_BODYPART_EPISODE_M2M,
                    {
                        f"{field}_id": relation_id,
                        "episode_id": uid,
                    },
                )

            episode.pop(field)

        cur.execute(
            inserts.EPISODE_INSERT,
            {
                "id": int(uid),
                **episode,
            },
        )


def enable_fts(cur):
    cur.execute(views.CREATE_FULL_EPISODE)
    cur.execute(fts.SETUP_EPISODE_FTS)
    cur.execute(fts.REBUILD_FTS)


def main():
    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()

    init_db(cur)
    episodes = extract_categories({})
    insert_episodes(cur, episodes)

    enable_fts(cur)

    con.commit()
    con.close()


main()
