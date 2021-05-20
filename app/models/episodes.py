GET = """
SELECT
    episode.id,
    episode.title,
    level.name,
    teacher.name,
    category.name,
    group_concat(bodypart.name, ",")
FROM episode
LEFT JOIN level ON level.id = episode.level_id
LEFT JOIN teacher ON teacher.id = episode.teacher_id
LEFT JOIN category ON category.id = episode.category_id
LEFT JOIN bodypart_episode ON bodypart_episode.episode_id = episode.id
LEFT JOIN bodypart ON bodypart.id = bodypart_episode.bodypart_id
WHERE episode.id = :id
"""

LIST = "SELECT %(fields)s FROM episode LIMIT %(limit)s OFFSET %(offset)s"

FILTER = """
SELECT %(fields)s
FROM episode
LEFT JOIN %(attribute)s ON %(attribute)s.id = episode.%(attribute)s_id
WHERE %(attribute)s.id = %(uid)s
"""

import logging


class Episode:
    LIST_FIELDS = [
        "id",
        "url",
        "thumbnail",
        "title",
        "description",
    ]

    GET_FIELDS = [
        "id",
        "title",
        "level",
        "teacher",
        "category",
        "bodyparts",
    ]

    def __init__(self, db):
        self.db = db

    async def get(self, uid):
        async with self.db.execute(GET, {"id": uid}) as cursor:
            row = await cursor.fetchone()

        return {key: value for key, value in zip(self.GET_FIELDS, row)}

    async def list(self, limit=None, offset=None):
        limit = min(max(0, limit), 50) if limit else 50
        offset = offset or 0
        data = []

        options = {
            "fields": ",".join(self.LIST_FIELDS),
            "limit": limit,
            "offset": offset,
        }

        async with self.db.execute(LIST % options) as cursor:
            async for row in cursor:
                data.append({key: value for key, value in zip(self.LIST_FIELDS, row)})

        return data

    async def filter(self, attribute, uid):
        fields = ",".join(
            map(
                lambda f: f"episode.{f}",
                self.LIST_FIELDS,
            ),
        )

        data = []
        options = {
            "fields": fields,
            "attribute": attribute,
            "uid": uid,
        }

        logging.error(FILTER % options)

        async with self.db.execute(FILTER % options) as cursor:
            async for row in cursor:
                data.append({key: value for key, value in zip(self.LIST_FIELDS, row)})

        return data
