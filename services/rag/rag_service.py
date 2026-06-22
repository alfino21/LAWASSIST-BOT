from services.rag.retriever import get_retriever
from services.gpt_utils import generate_response


def legal_rag_query(question):

    retriever = get_retriever()

    # langchain retriever API changed — use `invoke` for sync calls
    docs = retriever.invoke(question)

    context = "\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
Answer using ONLY the provided legal context.

Context:
{context}

Question:
{question}
"""

    return generate_response(prompt)