import os
import streamlit as st
from logics.retriever import load_retriever
from logics.prompt import create_single_pdf_chain
from logics.config import client 
from collections import defaultdict
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

# LOGIN FUNCTION
from helper_functions.utility import check_password
from helper_functions.utility import login

st.sidebar.title("Role")

if "auth" not in st.session_state:
    login()
    st.stop()

# If admin
if st.session_state["auth"] == "admin":
    st.sidebar.success("👑 Admin Access")

# If normal user
elif st.session_state["auth"] == "user":
    st.sidebar.success("🙋 User Access")


# Clear caches (optional)
st.cache_resource.clear()
st.cache_data.clear()

# Streamlit page config
st.set_page_config(
    layout="centered",
    page_title="Research summaries for policy makers"
)

st.title("Policy Summary")

#import shutil
#import os

#REPO_DIR = os.path.join(os.getcwd(), "repo_clone") # Path to the cloned repository

## Check if the repo folder exists and delete it
#if os.path.exists(REPO_DIR):
#    shutil.rmtree(REPO_DIR)
#    print(f"Deleted the existing cloned repo at {REPO_DIR}")
#else:
#    print(f"No existing repository found at {REPO_DIR}")

#if os.path.exists(DB_DIR):
#    st.write(f"✅ DB directory exists: {DB_DIR}")
#    st.write("Contents:", os.listdir(DB_DIR))
#else:
#    st.write(f"❌ DB directory NOT found: {DB_DIR}")

# Load Chroma DB
#vectordb = Chroma(
 #   persist_directory="DB_Dir",
 #   embedding_function=OpenAIEmbeddings()
#)

# Access stored metadata
#collection = vectordb._collection
#items = collection.get(include=["metadatas"])

# Extract unique PDF names
#pdfs = sorted(set([m.get("source") for m in items["metadatas"]]))

#st.write("\nPDFs stored in the Chroma DB:")
#st.write("----------------------------------")
#for p in pdfs:
#    print(p)

#st.write("\nTotal PDFs detected:", len(pdfs))
#st.write("Total chunks stored:", collection.count())

with st.form(key="form"):
    st.subheader("Enter your query here")
    user_prompt = st.text_area("Enter your prompt here", height=200)
    submit_button = st.form_submit_button("Generate summaries")

if submit_button:
    query = user_prompt

    # Validate input
    if not query:
        st.warning("Please enter a query before submitting.")
        st.stop()

    if not client:
        st.error("No papers found. Please ingest papers first.")
        st.stop()
    try:
        # Ensure that a collection is loaded (or check if the client is open)
        if not client.get_collection(collection_name) or not client.is_open():
            raise ValueError("Database is properly initialized or is missing.")
        
        if len(collection) == 0:
            raise ValueError("The database is empty. Please ingest papers before querying.")
    except Exception as e:
        st.error(f"Error initializing database: {e}")
        st.stop()

    # Retrieve relevant chunks
    with st.spinner("Retrieving relevant information..."):
        retriever = load_retriever()
        docs = retriever.invoke(query)

    if not docs:
        st.warning("No matching content found.")
        st.stop()

    # Group chunks by PDF
    pdf_chunks = defaultdict(list)
    for d in docs:
        # Ensure metadata exists
        pdf_name = os.path.basename(d.metadata.get("source", "Unknown.pdf"))
        pdf_chunks[pdf_name].append(d.page_content)

    # Create the summarization chain
    single_pdf_chain = create_single_pdf_chain()

    # Display summaries
    st.header("Summaries")
    for pdf_name, chunks in pdf_chunks.items():
        st.subheader(pdf_name)
        context = "\n\n".join(chunks)
        summary = single_pdf_chain({
            "context": context,
            "question": query
        })
        st.write(summary)


