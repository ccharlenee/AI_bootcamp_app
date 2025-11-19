import streamlit as st
from helper_functions.style import apply_custom_styles
from google.cloud import storage
import json

apply_custom_styles()

if st.session_state["auth"] != "admin":
    st.error("⛔ You do not have access to this page.")
    st.stop()

st.title("👑 Admin Dashboard")
st.write("Only admins can see this.")

service_account_info = st.secrets["gcp_service_account"]

client = storage.Client.from_service_account_info(service_account_info)
bucket_name = "research_app"# <-- change to your bucket name
bucket = client.bucket(bucket_name)


# File uploader
uploaded_file = st.file_uploader(
    "Choose files to upload",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=False
)

if uploaded_file:
    # Create a blob name (filename)
    blob = bucket.blob(uploaded_file.name)

    # Upload file to GCS
    blob.upload_from_string(uploaded_file.getvalue())

    st.success(f"Uploaded successfully to: gs://{bucket_name}/{uploaded_file.name}")
