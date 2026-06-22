from services.gpt_utils import generate_response

def analyze_legal_document(text):
    prompt = f"""
    Analyze this legal document.

    Return in the following format:

    1. Document Type
    2. Risk Score (0-100)
    3. Risk Level (Low / Medium / High)
    4. High Risk Clauses
    5. Missing Clauses
    6. Legal Issues
    7. Recommendations
    8. Summary

    Document:

    {text}
    """
    return generate_response(prompt)