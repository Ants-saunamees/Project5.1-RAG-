import chromadb
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "chroma_db")

client = chromadb.PersistentClient(path=DB_PATH)


# Create or load the collection
collection = client.get_or_create_collection(
    name="techcorp_docs",
    metadata={"hnsw:space": "cosine"}  # cosine similarity search
)

def store_chunk(chunk_id: str, text: str, embedding: list[float], metadata: dict):
    """
    Stores a single chunk in ChromaDB.
    """
    collection.add(
        ids=[chunk_id],
        documents=[text],
        embeddings=[embedding],
        metadatas=[metadata]
    )

print("INGESTION DB PATH:", DB_PATH)
