import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import subprocess

#repo_url = "https://github.com/ccharlenee/AI_bootcamp_app.git"
#clone_dir = os.path.join(os.getcwd(), "repo_clone2")

#if not os.path.exists(clone_dir):
#    subprocess.run(["git", "clone", repo_url, clone_dir])

#DB_DIR = os.path.join(clone_dir, "db3")

from chromadb import PersistentClient

#st.cache_resource
def get_chroma_client():
    # The path should point to the directory in your repo
    client = PersistentClient(path="https://github.com/ccharlenee/AI_bootcamp_app.git/db3")
    return client

client = get_chroma_client()

#PDF_DIR = "/Users/limin/Documents/Python/Journal_database"  # folder containing many PDFs

def get_embeddings():
    return OpenAIEmbeddings()