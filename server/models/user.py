GET = "SELECT %(fields)s FROM user WHERE username = :username"


class User:
    def __init__(self, db):
        self.db = db

    GET_FIELDS = ["id", "username", "password"]

    async def get(self, username, with_password=False):
        options = {"fields": ",".join(self.GET_FIELDS)}
        data = await self.db.get_one(
            GET % options,
            self.GET_FIELDS,
            {"username": username},
        )
        if not with_password:
            del data["password"]
        return data
