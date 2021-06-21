from tortoise import fields, models, run_async, Tortoise
from tortoise.contrib.pydantic import pydantic_model_creator


class Tag(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=20, unique=True)


class User(models.Model):
    id = fields.IntField(pk=True)
    username = fields.CharField(max_length=20, unique=True)
    tag = fields.ForeignKeyField(model_name="models.Tag")


Tortoise.init_models(["__main__"], "models")

UserBasicSchema = pydantic_model_creator(
    User,
    name="BasicUser",
    exclude=[
        "tag",
        # "tag_id",
    ],
)
UserSchema = pydantic_model_creator(User, name="User")


async def test():
    await Tortoise.init(db_url="sqlite://db.sqlite3", modules={"models": ["__main__"]})
    await Tortoise.generate_schemas()

    t = await Tag.create(name="foo")
    u = await User.create(username="bar", tag=t)

    user = await UserSchema.from_queryset(User.all())
    basic_user = await UserBasicSchema.from_queryset(User.all())

    print(user[0].json())
    print(basic_user[0].json())

    from tortoise.contrib.pydantic.base import _get_fetch_fields

    print(_get_fetch_fields(UserSchema, User))
    print(_get_fetch_fields(UserBasicSchema, User))


run_async(test())
