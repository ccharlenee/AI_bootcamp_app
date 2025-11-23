import os
import subprocess
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnableLambda
from logics.config import get_embeddings
from logics.Ingest import DB_DIR


def load_retriever(k=8):
    """
    LCEL-compatible retriever
    input: query string
    output: list of documents with metadata
    """
    
    if not os.path.exists(DB_DIR):
        raise ValueError(f"Vector store not found in {DB_DIR}. Please ingest data first.")
    
    # Load the Chroma vector store from the temporary directory
    vectordb = Chroma(
        persist_directory=DB_DIR,
        embedding_function=get_embeddings(),  
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": k})

    def retrieve_docs(query:str):
        docs = retriever.invoke(query)
        return docs or []
    
    return RunnableLambda(retrieve_docs)
