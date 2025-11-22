import os
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
#from .config import PDF_DIR, DB_DIR, get_embeddings
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

DB_DIR = "db2/"   # persistent chroma
PDF_DIR = "/Users/limin/Documents/Python/Journal_database"  # folder containing many PDFs

def get_embeddings():
    return OpenAIEmbeddings()

def ingest_pdfs():
    """Load, split, embed, and persist PDFs into Chroma."""
    loader = PyPDFDirectoryLoader(PDF_DIR)
    docs = loader.load()
    print(f"Loaded {len(docs)} documents from {PDF_DIR}")

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150
    )
    chunks = splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=DB_DIR,
    )
   
    print(f"Vector store saved to {DB_DIR}")
    return vectordb
#make the script importable as module as well as standalone script
if __name__ == "__main__":
    ingest_pdfs()
