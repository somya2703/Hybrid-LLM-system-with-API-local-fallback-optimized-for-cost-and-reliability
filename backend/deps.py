from src.vectorstore import load_vectorstore, main as build_vectorstore
from src.logger import get_logger

logger = get_logger("deps")

vectorstore = None


def init_vectorstore():
    global vectorstore

    try:
        logger.info("Trying to load existing vectorstore...")
        vectorstore = load_vectorstore()

    except Exception as e:
        logger.warning(f"Vectorstore not found. Building new one... ({e})")

        build_vectorstore()
        vectorstore = load_vectorstore()

    logger.info("Vectorstore ready ✅")


def get_vectorstore():
    return vectorstore