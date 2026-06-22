from services.gpt_utils import generate_response


def legal_advice(question: str):

    prompt = f"""
You are LawAssistBot.

Provide educational legal information.

Important:
- Do not claim to be a lawyer.
- Mention that professional legal advice may be required.
- Give practical next steps.

Question:
{question}
"""

    return generate_response(prompt)