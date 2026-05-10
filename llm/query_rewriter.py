from llm.client import chat_with_llm

def rewrite_query(history, user_query):
    """
    Rewrites the user query into a standalone, explicit search query.
    """
    prompt = f"""
Rewrite the user's query into a standalone, explicit search query.
Use the conversation history to fill in missing context.
Return ONLY the rewritten query.

Conversation history:
{history}

User query:
{user_query}
"""

    rewritten = chat_with_llm(prompt)
    return rewritten.strip()
