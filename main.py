import os
import streamlit as st
from logics.retriever import load_retriever
from logics.prompt import create_single_pdf_chain
from logics.config import DB_DIR 
from collections import defaultdict

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

    if not os.path.exists(DB_DIR):
        st.error("No papers found. Please ingest papers first.")
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


