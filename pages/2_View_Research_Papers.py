import streamlit as st
import pandas as pd
import json
from helper_functions.style import apply_custom_styles
from google.cloud import storage

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

# Load service account from Streamlit secrets
service_account_info = st.secrets["gcp_service_account"]

# Initialize GCS client
client = storage.Client.from_service_account_info(service_account_info)

# Replace with your bucket name
bucket_name = "research_app"
bucket = client.bucket(bucket_name)

# Get all blobs (files) in the bucket
blobs = list(bucket.list_blobs())

# Extract file names
file_list = [blob.name for blob in blobs]

st.write("Found research documents:")
st.write(file_list)