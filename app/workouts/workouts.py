from typing import Literal

from app.app import make_request
from endpoints import endpoints

async def create_workout(token: str, json: dict) -> dict | Literal[False]:
    return (await make_request('POST', endpoints['workouts'], json=json, token=token))

async def get_workouts(token: str) -> dict | Literal[False]:
    return (await make_request('GET', endpoints['workouts'], token=token))

async def delete_workout(token: str, workout_id: str) -> dict | Literal[False]:
    return (await make_request('DELETE', endpoints['workouts'], token=token, json={"workout_id": workout_id}))