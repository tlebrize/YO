LIST = """
SELECT %(attribute)s.id, name, count(*)
FROM %(attribute)s
LEFT JOIN episode ON episode.%(attribute)s_id = %(attribute)s.id
GROUP BY %(attribute)s.id
"""

GET = """
SELECT 
    episode.id,
    episode.description,
    episode.title,
    episode.thumbnail,
    episode.url
FROM %(attribute)s
LEFT JOIN episode ON episode.%(attribute)s_id = %(attribute)s.id
WHERE %(attribute)s.id = :id
"""

SERIES_LIST = """
SELECT 
series.name series,
episode.title,
duration.name duration,
episode.id,
episode.thumbnail
FROM series
LEFT JOIN episode ON series.id = episode.series_id
LEFT JOIN duration ON episode.duration_id = duration.id
GROUP BY episode.id
"""


class Attribute:
    def __init__(self, db):
        self.db = db

    ATTRIBUTES_LIST = [
        "category",
        "duration",
        "level",
        "series",
        "teacher",
        "tag",
    ]

    FILTER_CHOICES_REGEX = "|".join(ATTRIBUTES_LIST)

    GET_FIELDS = [
        "episode_id",
        "description",
        "title",
        "thumbnail",
        "url",
    ]

    SERIES_LIST_FIELDS = [
        "series",
        "title",
        "duration",
        "id",
        "thumbnail",
    ]

    async def list(self):
        data = {attr: [] for attr in self.ATTRIBUTES_LIST}
        fields = ["id", "name", "count"]

        for attribute in self.ATTRIBUTES_LIST:
            options = {"attribute": attribute}
            data[attribute] = await self.db.get_many(
                LIST % options,
                fields,
            )

        return data

    async def get(self, attribute, uid):
        if not attribute in self.ATTRIBUTES_LIST:
            raise Exception("invalid_input", {"attribute": attribute})

        options = {"attribute": attribute}
        args = {"id": uid}
        return await self.db.get_many(
            GET % options,
            self.GET_FIELDS,
            args,
        )

    async def series_list(self):
        return await self.db.get_many(SERIES_LIST, self.SERIES_LIST_FIELDS)
