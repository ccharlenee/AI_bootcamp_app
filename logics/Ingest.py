import os
import io
import streamlit as st
from google.cloud import storage
from langchain_community.document_loaders import PyPDFDirectoryLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
#from .config import PDF_DIR, DB_DIR, get_embeddings
from langchain_openai import OpenAIEmbeddings
#from langchain.embeddings import OpenAIEmbeddings

# Load service account from Streamlit secrets
service_account_info = st.secrets["gcp_service_account"]

DB_DIR = "/tmp/db3/" 
bucket_name = "research_app"

def get_embeddings():
    return OpenAIEmbeddings()

def ingest_pdfs_from_gcs():
    """Load, split, embed, and persist PDFs into Chroma."""
    
    storage_client = storage.Client.from_service_account_info(service_account_info)
    
    bucket = storage_client.bucket("research_app")
   
    blobs = bucket.list_blobs()  # no prefix as not in subdirectory
    pdf_files = [blob.name for blob in blobs if blob.name.endswith(".pdf")]
    
    all_docs = []
    for pdf_file in pdf_files:
        blob = bucket.blob(pdf_file)
        file_contents = blob.download_as_bytes()

    loader = PyPDFLoader(io.BytesIO(file_contents))
    docs = loader.load()
    all_docs.extend(docs)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=150
    )
    chunks = splitter.split_documents(all_docs)

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
