import aiosqlite

async def create() -> None:
    connection = await aiosqlite.connect('db.db')
    cursor = await connection.cursor()
    await cursor.execute(
'''CREATE TABLE IF NOT EXISTS users (
id INTEGER PRIMARY KEY,
auth_token TEXT
)
''')
    await connection.commit()