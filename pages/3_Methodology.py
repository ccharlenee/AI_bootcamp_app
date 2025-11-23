import streamlit as st
from helper_functions.style import apply_custom_styles
from helper_functions.utility import check_password
from helper_functions.utility import login

apply_custom_styles()

#LOGIN FUNCTION
if "auth" not in st.session_state:
    login()
    st.stop()

# If admin
if st.session_state["auth"] == "admin":
    st.sidebar.success("👑 Admin Access")

# If normal user
elif st.session_state["auth"] == "user":
    st.sidebar.success("🙋 User Access")

#start write up here
st.title("Methodology")

st.write("Data sources: Journal articles are loaded on Google Cloud Bucket")
st.write("Methodology is as follows:")
st.write("Journal articles are ingested into Chromadatabase using PyPDF and text are split using RecursiveCharacterTextSplitter.")
st.write("A Chroma vector store of embeddings are generated for efficient retrieval.")
st.write("The Chroma vector store is converted into a retriever object to be queried.")
st.write("The prompt and additional context from users uses LLMs to generate a policy related summary for Singapore.")