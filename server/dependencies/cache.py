from aiocache import caches, RedisCache

caches.set_config(
    {
        "default": {
            "cache": RedisCache,
            "endpoint": "0.0.0.0",
            "port": "6369",
            "serializer": {
                "class": "aiocache.serializers.JsonSerializer",
            },
        }
    }
)

Cache = RedisCache


async def get_cache():
    return caches.get("default")
