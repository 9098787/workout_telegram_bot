import aiosqlite

async def get_users() -> list:
    connection = await aiosqlite.connect('db.db')
    cursor = await connection.cursor()
    await cursor.execute('SELECT user_id FROM users')
    return list(map(lambda x: x[0], (await cursor.fetchall())))

async def create_user(user_id: int, token: str) -> None:
    connection = await aiosqlite.connect('db.db')
    cursor = await connection.cursor()
    await cursor.execute('INSERT INTO users VALUES (?, ?)', (user_id, token))
    await connection.commit()

async def get_token(user_id: int) -> str:
    connection = await aiosqlite.connect('db.db')
    cursor = await connection.cursor()
    await cursor.execute('SELECT auth_token FROM users WHERE user_id = ?', (user_id, ))
    return (await cursor.fetchone())[0]