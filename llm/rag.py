from retrieval.retriever import retrieve
from llm.client import chat_with_llm  # your LLM wrapper

def generate_answer(question: str, department: str | None = None):
    # Step 1: Retrieve relevant chunks
    results = retrieve(question, n_results=5, department=department)

    chunks = results["documents"][0]  # Chroma returns nested lists

    # Step 2: Build context
    context = "\n\n".join(chunks)

    # Step 3: Build prompt
    prompt = f"""
Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't know based on the provided documents."

Context:
{context}

Question: {question}

Answer:
"""

    # Step 4: Call LLM
    return chat_with_llm(prompt)
