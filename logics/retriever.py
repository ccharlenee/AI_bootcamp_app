import os
import subprocess
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnableLambda
from logics.config import DB_DIR, get_embeddings

def clone_repo():
    if not os.path.exists(CLONE_DIR):
        subprocess.run(["git", "clone", REPO_URL, CLONE_DIR])

def load_retriever(k=8):
    """
    LCEL-compatible retriever
    input: query string
    output: list of documents with metadata
    """
    vectordb = Chroma(
        persist_directory=DB_DIR,
        embedding_function=get_embeddings(),
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": k})

    def retrieve_docs(query:str):
        docs = retriever.invoke(query)
        return docs or []
    
    return RunnableLambda(retrieve_docs)
