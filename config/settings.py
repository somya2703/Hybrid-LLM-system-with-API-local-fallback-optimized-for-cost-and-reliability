import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MODEL_PATH = os.path.join(BASE_DIR, "models", "tinyllama-1.1b-chat-v1.0-q4_k_m.gguf")

VECTOR_DB_PATH = os.path.join(BASE_DIR, "db", "faiss_index")
DATA_PATH = os.path.join(BASE_DIR, "dummy_data")

CHUNK_SIZE = 500
CHUNK_OVERLAP = 100
TOP_K_RESULTS = 3

OPENAI_MODEL = "gpt-4o-mini"  