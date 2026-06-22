from langchain_community.vectorstores import Chroma

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from services.rag.load_documents import (
    load_documents
)


def create_vector_store():

    docs = load_documents()

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma.from_documents(
        docs,
        embeddings,
        persist_directory="vector_db"
    )

    db.persist()

    return db