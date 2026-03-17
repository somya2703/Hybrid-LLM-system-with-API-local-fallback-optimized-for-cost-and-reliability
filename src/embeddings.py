#from langchain.embeddings import HuggingFaceEmbeddings
from langchain_community.embeddings import HuggingFaceEmbeddings
from src.logger import get_logger

logger = get_logger("embeddings")

def get_embeddings():

    logger.info("Loading sentence-transformer embedding model")

    model = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    return model