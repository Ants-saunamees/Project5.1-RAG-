import asyncio
from ingestion.pipeline import ingest_department

async def main():
    for dept in ["engineering", "support", "hr"]:
        await ingest_department(dept)

asyncio.run(main())
