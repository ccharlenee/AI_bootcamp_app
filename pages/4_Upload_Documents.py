import streamlit as st
from helper_functions.utility import require_login
from helper_functions.style import apply_custom_styles

apply_custom_styles()

require_login()

if st.session_state["auth"] != "admin":
    st.error("⛔ You do not have access to this page.")
    st.stop()

st.title("👑 Admin Dashboard")
st.write("Only admins can see this.")