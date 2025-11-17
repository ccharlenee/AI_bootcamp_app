import streamlit as st
from helper_functions.style import apply_custom_styles

apply_custom_styles()

if st.session_state["auth"] != "admin":
    st.error("⛔ You do not have access to this page.")
    st.stop()

st.title("👑 Admin Dashboard")
st.write("Only admins can see this.")

# File uploader
uploaded_files = st.file_uploader(
    "Choose files to upload",
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True
)

# Folder to save uploaded files
upload_folder = "uploaded_docs"
os.makedirs(upload_folder, exist_ok=True)

if uploaded_files:
    for file in uploaded_files:
        file_path = os.path.join(upload_folder, file.name)
        with open(file_path, "wb") as f:
            f.write(file.getbuffer())
        st.success(f"✅ Uploaded {file.name}")

# Optional: show list of uploaded files
st.write("### Uploaded Files")
for f in os.listdir(upload_folder):
    st.write(f"- {f}")