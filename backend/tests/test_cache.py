import pytest
from app.services.cache import TTLCache
@pytest.mark.asyncio
async def test_cache_reuses_value():
    calls=0
    async def factory():
        nonlocal calls;calls+=1;return calls
    cache=TTLCache[int](10);assert await cache.get_or_set('x',factory)==1;assert await cache.get_or_set('x',factory)==1;assert calls==1
