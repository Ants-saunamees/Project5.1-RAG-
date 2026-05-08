import chromadb
from ingestion.embedder import embed_text
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "..", "chroma_db")

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection("techcorp_docs")

def retrieve(query: str, n_results: int = 5, department: str | None = None):
    # Embed the user question
    query_embedding = embed_text(query)

    # Optional metadata filter
    where = {"department": department} if department else {}

    # Query ChromaDB
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results,
        where=where
    )

    return results
