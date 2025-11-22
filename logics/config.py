import os
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
import subprocess

repo_url = "https://github.com/ccharlenee/AI_bootcamp_app.git"
clone_dir = os.path.join(os.getcwd(), "repo_clone2")

if not os.path.exists(clone_dir):
    subprocess.run(["git", "clone", repo_url, clone_dir])

DB_DIR = os.path.join(clone_dir, "db3")

PDF_DIR = "/Users/limin/Documents/Python/Journal_database"  # folder containing many PDFs

def get_embeddings():
    return OpenAIEmbeddings()