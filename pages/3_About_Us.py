import streamlit as st

# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="My Streamlit App"
)
# endregion <--------- Streamlit App Configuration --------->

st.title("About Us")

st.write("This is an app that allows users to facilitate search of NParks publication database to get a quick understanding of what has been done before")
st.write("It is built using Streamlit and Langchain with GPT-4o-mini as the LLM")
st.write("Developed by Charlene Ng and Cheong Limin as part of the AI Bootcamp Project")

with st.expander("How to use this App"):
    st.write("1. Enter your query in the text area.")
    st.write("2. Click the 'Submit' button.")
    st.write("3. The app will generate a text completion based on your prompt.")
