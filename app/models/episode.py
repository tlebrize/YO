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
        return await self.db.get_one(GET, self.GET_FIELDS, {"id": uid})

    async def list(self, limit=None, offset=None):
        limit = min(max(0, limit), 50) if limit else 50
        offset = offset or 0

        options = {
            "fields": ",".join(self.LIST_FIELDS),
            "limit": limit,
            "offset": offset,
        }

        return await self.db.get_many(
            LIST % options,
            self.LIST_FIELDS,
        )

    async def filter(self, attribute, uid):
        fields = ",".join(
            map(
                lambda f: f"episode.{f}",
                self.LIST_FIELDS,
            ),
        )

        options = {
            "fields": fields,
            "attribute": attribute,
            "uid": uid,
        }

        return await self.db.get_many(
            FILTER % options,
            self.LIST_FIELDS,
        )

    async def search(self, query: str):
        options = {"query": f"{query}*"}
        return await self.db.get_many(
            SEARCH % options,
            self.GET_FIELDS,
        )
