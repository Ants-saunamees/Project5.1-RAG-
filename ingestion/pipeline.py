import uuid
from ingestion.loaders import load_department_docs
from ingestion.chunker import chunk_text
from ingestion.embedder import embed_text
from ingestion.store import store_chunk
import asyncio

async def ingest_department(department: str):
    for doc in load_department_docs(department):
        chunks = chunk_text(doc["text"], department)

        for chunk in chunks:
            embedding = embed_text(chunk)
            chunk_id = str(uuid.uuid4())

            store_chunk(
                chunk_id=chunk_id,
                text=chunk,
                embedding=embedding,
                metadata=doc["metadata"]
            )

    print(f"Finished ingesting department: {department}")

#asyncio.run(ingest_department("engineering"))
#asyncio.run(ingest_department("hr"))
#asyncio.run(ingest_department("support"))
