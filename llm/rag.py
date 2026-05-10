from retrieval.retriever import retrieve
from llm.client import chat_with_llm  # your LLM wrapper'
from llm.query_rewriter import rewrite_query
from api.messages_repository import MessagesRepository


def generate_answer(session_id: str, question: str, department: str | None = None):

    history = MessagesRepository.get_history(session_id)

    rewritten_q = rewrite_query(question)


    # Step 1: Retrieve relevant chunks
    results = retrieve(rewritten_q, n_results=5, department=department)

    chunks = results["documents"][0]  # Chroma returns nested lists

    # Step 2: Build context
    context = "\n\n".join(chunks)

    # Step 3: Build prompt
    prompt = f"""
Use ONLY the context below to answer the question.
If the answer is not in the context, say "I don't know based on the provided documents."

Context:
{context}

Question: {rewritten_q}

Answer:
"""

    # Step 4: Call LLM
    return chat_with_llm(prompt)
