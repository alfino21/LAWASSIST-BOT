from utils.gpt_utils import generate_response

def legal_advice(question: str) -> str:
    prompt = f"Provide basic legal advice (not as a lawyer) for the following question:\n\n{question}"
    return generate_response(prompt)
