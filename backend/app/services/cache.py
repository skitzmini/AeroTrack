import asyncio,time
from collections.abc import Awaitable,Callable
from typing import Generic,TypeVar
T=TypeVar('T')
class TTLCache(Generic[T]):
    def __init__(self,ttl:int=10):self.ttl=ttl;self._items:dict[str,tuple[float,T]]={};self._lock=asyncio.Lock()
    async def get_or_set(self,key:str,factory:Callable[[],Awaitable[T]])->T:
        async with self._lock:
            item=self._items.get(key)
            if item and time.monotonic()-item[0]<self.ttl:return item[1]
            value=await factory();self._items[key]=(time.monotonic(),value);return value
