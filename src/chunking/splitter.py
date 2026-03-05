from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter

def split_documents(document: list[Document], chunk_size: int, chunk_overlap: int) -> list[Document]:
    text_splitter = RecursiveCharacterTextSplitter(chunk_size = chunk_size, chunk_overlap = chunk_overlap)
    texts = text_splitter.split_documents(document)
    return texts