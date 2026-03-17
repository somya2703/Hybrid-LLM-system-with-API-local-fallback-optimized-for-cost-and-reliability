import os

from src.loaders import load_documents
from src.embeddings import get_embeddings
from src.logger import get_logger
from config.settings import VECTOR_DB_PATH, DATA_PATH

from langchain_community.vectorstores import FAISS

logger = get_logger("vectorstore")


def create_vectorstore(documents):

    embeddings = get_embeddings()

    logger.info("Creating FAISS vectorstore")

    vectorstore = FAISS.from_documents(
        documents,
        embeddings
    )

    vectorstore.save_local(VECTOR_DB_PATH)

    logger.info(f"Vectorstore saved to {VECTOR_DB_PATH}")

def load_vectorstore():

    if not os.path.exists(VECTOR_DB_PATH):
        raise RuntimeError(
            "Vectorstore not found. Run: python -m src.vectorstore"
        )

    logger.info("Loading FAISS vectorstore")

    embeddings = get_embeddings()

    vectorstore = FAISS.load_local(
        VECTOR_DB_PATH,
        embeddings,
        allow_dangerous_deserialization=True
    )

    return vectorstore

def main():

    logger.info("Starting vector database build")

    pdf_paths = [
        os.path.join(DATA_PATH, f)
        for f in os.listdir(DATA_PATH)
        if f.endswith(".pdf")
    ]

    if not pdf_paths:
        raise RuntimeError("No PDF files found in dummy_data/")

    logger.info(f"Found {len(pdf_paths)} PDFs")

    documents = load_documents(pdf_paths)

    create_vectorstore(documents)

    logger.info("Vector database build complete")


if __name__ == "__main__":
    main()