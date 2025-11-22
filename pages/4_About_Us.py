import streamlit as st
from helper_functions.style import apply_custom_styles

apply_custom_styles()

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

if "auth" not in st.session_state:
    login()
    st.stop()

# If admin
if st.session_state["auth"] == "admin":
    st.sidebar.success("👑 Admin Access")

# If normal user
elif st.session_state["auth"] == "user":
    st.sidebar.success("🙋 User Access")
    
st.title("About Us")

st.write("This is an app that facilitates users' search of NParks publication database to summarise previous research publications by NParks")
st.write("It is built using Streamlit and Langchain with GPT-4o-mini as the LLM")
st.write("Developed by Charlene Ng and Cheong Limin as part of the AI Bootcamp Project")

with st.expander("How to use this App"):
    st.write("1. Enter question on topic of interest the text area.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The app will generate a text completion based on your prompt.")
    st.write("4. Note that only admin users can upload documents to the database.")
