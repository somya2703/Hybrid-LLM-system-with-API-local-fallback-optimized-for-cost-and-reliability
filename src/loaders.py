#from langchain.document_loaders import PyPDFLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from config.settings import CHUNK_SIZE, CHUNK_OVERLAP


def load_documents(pdf_paths):
    docs = []

    for pdf in pdf_paths:
        loader = PyPDFLoader(pdf)
        docs.extend(loader.load())

    splitter = CharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(docs)