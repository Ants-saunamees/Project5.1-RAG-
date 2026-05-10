from config.database import get_db

class MessagesRepository:

    async def save_message(self, session_id: str, role: str, content: str):
        db = await get_db()
        await db.execute(
            """
            INSERT INTO messages (session_id, role, content)
            VALUES ($1, $2, $3)
            """,
            session_id, role, content
        )
        await db.close()

    async def get_history(self, session_id: str, limit: int = 20):
        db = await get_db()
        rows = await db.fetch(
            """
            SELECT role, content
            FROM messages
            WHERE session_id = $1
            ORDER BY created_at ASC
            LIMIT $2
            """,
            session_id, limit
        )
        await db.close()
        return rows
