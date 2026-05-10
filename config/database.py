# src/config/database.py

import asyncpg

DB_USER = "postgres"
DB_PASSWORD = "RednasR112"
DB_NAME = "fastapi_app5_1"
DB_HOST = "localhost"
DB_PORT = 5432

async def get_db():
    return await asyncpg.connect(
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        host=DB_HOST,
        port=DB_PORT,
    )

