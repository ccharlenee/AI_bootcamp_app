from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from logics.config import PDF_DIR, DB_DIR, get_embeddings

def ingest_pdfs():
    """Load, split, embed, and persist PDFs into Chroma."""
    loader = PyPDFDirectoryLoader(PDF_DIR)
    docs = loader.load()

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150
    )
    chunks = splitter.split_documents(docs)

    vectordb = Chroma.from_documents(
        documents=chunks,
        embedding=get_embeddings(),
        persist_directory=DB_DIR,
    )
    vectordb.persist()
    return vectordb