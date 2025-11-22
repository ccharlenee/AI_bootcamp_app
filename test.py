from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# Load Chroma DB
vectordb = Chroma(
    persist_directory="db2/",
    embedding_function=OpenAIEmbeddings()
)

# Access stored metadata
collection = vectordb._collection
items = collection.get(include=["metadatas"])

# Extract unique PDF names
pdfs = sorted(set([m.get("source") for m in items["metadatas"]]))

print("\nPDFs stored in the Chroma DB:")
print("----------------------------------")
for p in pdfs:
    print(p)

print("\nTotal PDFs detected:", len(pdfs))
print("Total chunks stored:", collection.count())
