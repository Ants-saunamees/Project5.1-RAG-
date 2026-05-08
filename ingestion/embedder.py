import requests

# The model you want to use for embeddings.
# "nomic-embed-text" is the best free local embedding model right now.
EMBED_MODEL = "nomic-embed-text"

def embed_text(text: str):
    """
    Sends text to Ollama and returns the embedding vector.
    """
    response = requests.post(
        "http://localhost:11434/api/embeddings",
        json={
            "model": EMBED_MODEL,
            "prompt": text
        }
    )

    data = response.json()

    # Ollama returns: { "embedding": [vector] }
    return data["embedding"]




