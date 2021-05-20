GET = """
SELECT
    id,
    url,
    thumbnail,
    description,
    title,
    level,
    teacher,
    category,
    body_parts,
    duration,
    series
FROM full_episode
WHERE id = :id
"""

LIST = "SELECT %(fields)s FROM episode LIMIT %(limit)s OFFSET %(offset)s"

FILTER = """
SELECT %(fields)s
FROM episode
LEFT JOIN %(attribute)s ON %(attribute)s.id = episode.%(attribute)s_id
WHERE %(attribute)s.id = %(uid)s
"""

SEARCH = "SELECT * FROM episode_fts WHERE episode_fts MATCH :query ORDER BY rank"


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
        "url",
        "thumbnail",
        "description",
        "title",
        "level",
        "teacher",
        "category",
        "bodyparts",
        "duration",
        "series",
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

        async with self.db.execute(FILTER % options) as cursor:
            async for row in cursor:
                data.append({key: value for key, value in zip(self.LIST_FIELDS, row)})

        return data

    async def search(self, query: str):
        data = []

        options = {"query": f"{query}*"}

        async with self.db.execute(SEARCH, options) as cursor:
            async for row in cursor:
                data.append({key: value for key, value in zip(self.GET_FIELDS, row)})

        return data
