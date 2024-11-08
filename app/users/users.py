from typing import Literal

from app.app import make_request
from endpoints import endpoints

async def registration(json: dict) -> dict | Literal[False]:
    return (await make_request('POST', endpoints['users'], json=json))

async def me(token: str) -> dict | Literal[False]:
    return (await make_request('GET', endpoints['users'], token=token))

async def become_trainer(token: str) -> dict | Literal[False]:
    return (await make_request('PUT', endpoints['trainer'], token=token))