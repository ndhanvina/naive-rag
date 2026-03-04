from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE",1000))
CHUNK_OVERLAP = int(os.getenv("CHUNK_OVERLAP",100))
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "gemini-embedding-001")
LLM_MODEL = os.getenv("LLM_MODEL", "gemini-3-flash")
CHROMA_PERSIST_DIR = os.getenv("CHROMA_PERSIST_DIR", "indexes/chroma")
DATA_DIR = os.getenv("DATA_DIR", "data/raw")
RETRIEVER_K = int(os.getenv("RETRIEVER_K",4))