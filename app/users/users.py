from typing import Literal

from app.app import make_request
from endpoints import endpoints

async def registration(json) -> dict | Literal[False]:
    return (await make_request('POST', endpoints['registration'], json=json))