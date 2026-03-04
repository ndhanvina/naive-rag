from langchain_community.document_loaders import PyPDFLoader
from langchain.schema import Document
import os

def load_pdfs(data_dir: str) -> list[Document]:
    documents = []
    for filename in os.listdir(data_dir):
        if filename.endswith(".pdf"):
            try:
                file_path = os.path.join(data_dir, filename)
                docs = PyPDFLoader(file_path).load()
                documents.extend(docs)
            except Exception as e:
                print(f"Error while loading the document: {e}")
    return documents