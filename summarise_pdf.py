import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

# ------------------------------
# CONFIGURATION
# ------------------------------

PDF_PATH = "/Users/limin/Documents/Python/brodie et al 2025 well connected earth.pdf"
OPENAI_MODEL = "gpt-4o-mini"

# ------------------------------
# 1. Load PDF
# ------------------------------

print("📄 Loading PDF...")
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

# ------------------------------
# 2. Split into chunks
# ------------------------------

print("✂️ Splitting document into chunks...")
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150
)
chunks = splitter.split_documents(docs)

# ------------------------------
# 3. Embeddings + Vectorstore
# ------------------------------

print("🔢 Creating embeddings and vector database...")
embeddings = OpenAIEmbeddings(model='text-embedding-3-small')

vectorstore = FAISS.from_documents(chunks, embeddings)
retriever = vectorstore.as_retriever(
    search_type="similarity",
    search_kwargs={"k": 5}
)

# ------------------------------
# 4. Build RAG pipeline (new LangChain 1.0 style)
# ------------------------------

llm = ChatOpenAI(model=OPENAI_MODEL, temperature=0)

prompt = ChatPromptTemplate.from_template("""
You are assisting a Singapore government policy analyst.

Generate a summary of the key results from the study in bullet points,
then use the results to product a policy-relevant summary for Singapore including:                                          

- Key findings
- Evidence strength
- Implications for Singapore's policy landscape
- Recommended actions for Singapore 
- Risks or limitations

Consider Singapore's: urban density and land constraints
                                                      
Context:
{context}

Question:
{question}
""")

rag_chain = (
    {
        "context": retriever,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
)

# ------------------------------
# 5. Generate policy summary
# ------------------------------

POLICY_PROMPT = """
Summarise this academic paper in a policy-relevant way.
"""

print("🧠 Generating policy summary...\n")
result = rag_chain.invoke(POLICY_PROMPT)

print("========== POLICY SUMMARY ==========\n")
print(result.content)
print("\n====================================")
