import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import subprocess

repo_url = "https://github.com/ccharlenee/AI_bootcamp_app.git"
clone_dir = "https://github.com/ccharlenee/AI_bootcamp_app.git"
DB_DIR = "https://github.com/ccharlenee/AI_bootcamp_app.git/db2/"   # persistent chroma

PDF_DIR = "/Users/limin/Documents/Python/Journal_database"  # folder containing many PDFs

def get_embeddings():
    return OpenAIEmbeddings()