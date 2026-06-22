from services.gpt_utils import generate_response


def summarize_legal_case(text: str):

    prompt = f"""
Summarize the following legal case.

Return the result in:

1. Case Facts
2. Legal Issues
3. Arguments
4. Judgment
5. Key Takeaways

Case:

{text}
"""

    return generate_response(prompt)