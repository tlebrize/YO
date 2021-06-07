GET = "SELECT %(fields)s FROM full_episode WHERE id = :id"

LIST = "SELECT %(fields)s FROM episode LIMIT %(limit)s OFFSET %(offset)s"

SEARCH = """
SELECT %(fields)s
FROM episode_fts
WHERE episode_fts MATCH :query
ORDER BY rank
"""


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
        "tag",
    ]

    def __init__(self, db):
        self.db = db

    async def get(self, uid):
        options = {"fields": ",".join(self.GET_FIELDS)}
        return await self.db.get_one(
            GET % options,
            self.GET_FIELDS,
            {"id": uid},
        )

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

    async def search(self, query: str):
        options = {"fields": ",".join(self.GET_FIELDS)}
        args = {"query": f"{query}*"}

        return await self.db.get_many(
            SEARCH % options,
            self.GET_FIELDS,
            args,
        )
