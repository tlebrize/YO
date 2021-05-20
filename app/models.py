class Episode:
    list_fields = [
        "id",
        "url",
        "thumbnail",
        "title",
        "description",
    ]

    get_fields = [
        "id",
        "title",
        "level",
        "teacher",
        "category",
        "bodyparts",
    ]

    def __init__(self, db):
        self.db = db

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

    async def get(self, uid):
        async with self.db.execute(
            self.GET,
            {"id": uid},
        ) as cursor:
            row = await cursor.fetchone()
        return {key: value for key, value in zip(self.get_fields, row)}

    LIST = "SELECT %(fields)s FROM episode LIMIT %(limit)s OFFSET %(offset)s"

    async def list(self, limit=None, offset=None):
        limit = min(max(0, limit), 50) if limit else 50
        offset = offset or 0
        data = []

        async with self.db.execute(
            self.LIST
            % {
                "fields": ",".join(self.list_fields),
                "limit": limit,
                "offset": offset,
            }
        ) as cursor:
            async for row in cursor:
                data.append({key: value for key, value in zip(self.list_fields, row)})

        return data
