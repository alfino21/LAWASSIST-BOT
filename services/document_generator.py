from utils.gpt_utils import generate_response

def generate_document(doc_type: str, details: dict):
    prompt = f"Generate a {doc_type} using the following details: {details}"
    return generate_response(prompt)

