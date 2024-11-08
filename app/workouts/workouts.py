from typing import Literal

from app.app import make_request
from endpoints import endpoints

async def create_workout(token: str, json: dict) -> dict | Literal[False]:
    return (await make_request('POST', endpoints['workouts'], json=json, token=token))
