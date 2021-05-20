LIST = """
SELECT %(attribute)s.id, name, count(*)
FROM %(attribute)s
LEFT JOIN episode ON episode.%(attribute)s_id = %(attribute)s.id
GROUP BY %(attribute)s.id
;

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
    ]

    async def list(self):
        data = {attr: [] for attr in self.ATTRIBUTES_LIST}
        fields = ["id", "name", "count"]

        for attribute in self.ATTRIBUTES_LIST:
            async with self.db.execute(LIST % {"attribute": attribute}) as cursor:
                async for row in cursor:
                    data[attribute].append(
                        {key: value for key, value in zip(fields, row)}
                    )

        return data
