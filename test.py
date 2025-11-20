from langchain_community.vectorstores import Chroma
from logics.config import get_embeddings, DB_DIR

# Load existing Chroma vector store
vectordb = Chroma(
    persist_directory=DB_DIR,
    embedding_function=get_embeddings(),
)

# Check how many documents are stored
num_docs = len(vectordb.get(include=["documents"])["documents"])
print(f"Number of documents/chunks in vector store: {num_docs}")
