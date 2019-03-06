from aiocache import caches
from aiocache.base import BaseCache
from .aggregatebase import AggregateBase
from typing import List

caches.set_config({
    'default': {
        'cache': "aiocache.SimpleMemoryCache",
        'serializer': {
            'class': "aiocache.serializers.JsonSerializer"
        }
    },
    'redis_alt': {
        'cache': "aiocache.RedisCache",
        'endpoint': "127.0.0.1",
        'port': 6379,
        'timeout': 1,
        'serializer': {
            'class': "aiocache.serializers.PickleSerializer"
        },
        'plugins': [
            {'class': "aiocache.plugins.HitMissRatioPlugin"},
            {'class': "aiocache.plugins.TimingPlugin"}
        ]
    }
})


class Repository:

    def __init__(self):
        self._cache: BaseCache = caches.get("default")

    async def add(self, key, value: AggregateBase):
        return await self._cache.add(key=key, value=value)

    async def get(self, key) -> AggregateBase:
        return await self._cache.get(key)

    async def clear(self) -> bool:
        return await self._cache.clear()

    async def multi_set(self, pairs) -> bool:
        await self._cache.multi_set(pairs=pairs)

    async def multi_get(self, keys) -> List[AggregateBase]:
        return await self._cache.multi_get(keys)

    async def delete(self, key) -> int:
        return await self._cache.delete(key)

    async def close(self):
        await self._cache.close()

    async def exists(self, key) -> bool:
        return await self._cache.exists(key)
