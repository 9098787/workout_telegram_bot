from typing import Literal

from app.app import make_request
from endpoints import endpoints

async def auth(username: str, password: str) -> str | Literal[False]:
    return (await make_request('POST', endpoints['auth'], data={'username': username, 'password': password}))
