import aiohttp
from typing import Literal

async def make_request(method: Literal['GET', 'POST', 'PUT', 'DELETE'],
                        url: str,
                        data: dict = {},
                        json: dict = {},
                        ) -> dict | Literal[False]:
    async with aiohttp.ClientSession() as session:
        if method == 'GET':
            response = await session.get(url=url)
        elif method == 'POST':
            response = await session.post(url=url, data=data) if data else await session.post(url=url, json=json)
        elif method == 'DELETE':
            response = await session.delete(url=url)
        elif method == 'PUT':
            response = await session.put(url=url, data=data) if data else await session.put(url=url, json=json)

        if response.status in (200, 422):
            return await response.json()
        else:
            return False