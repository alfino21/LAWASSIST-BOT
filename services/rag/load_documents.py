from langchain_community.document_loaders import TextLoader

def load_documents():

    files = [
        "legal_docs/constitution.txt",
        "legal_docs/bns_sections.txt"
    ]

    documents = []

    for file in files:
        loader = TextLoader(file)
        documents.extend(loader.load())

    return documents