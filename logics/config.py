import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings

DB_DIR = "db/"   # persistent chroma
PDF_DIR = "/Users/limin/Documents/Python/Journal_database"  # folder containing many PDFs

def get_embeddings():
    return OpenAIEmbeddings()