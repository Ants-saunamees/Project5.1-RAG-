from rules.chunking_rules import CHUNKING_RULES

def chunk_text(text: str, department: str):
    rules = CHUNKING_RULES.get(department)
    size = rules["size"]
    overlap = rules["overlap"]

    chunks = []
    start = 0

    while start < len(text):
        end = start + size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap

    return chunks
