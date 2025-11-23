import os
import subprocess
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnableLambda
from logics.config import client, get_embeddings


def load_retriever(k=8):
    """
    LCEL-compatible retriever
    input: query string
    output: list of documents with metadata
    """
    vectordb = Chroma(
        client=client,
        embedding_function=get_embeddings(),
    )

    retriever = vectordb.as_retriever(search_kwargs={"k": k})

    def retrieve_docs(query:str):
        docs = retriever.invoke(query)
        return docs or []
    
    return RunnableLambda(retrieve_docs)
