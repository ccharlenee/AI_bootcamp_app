import streamlit as st  
import random  
import hmac  
    
    # """  
    # This file contains the common components used in the Streamlit App.  
    # This includes the sidebar, the title, the footer, and the password check.  
    # """  
    
       
def check_password():  
    """Returns `True` if the user had the correct password."""  
    def password_entered():  
        """Checks whether a password entered by the user is correct."""  
        if hmac.compare_digest(st.session_state["password"], st.secrets["password"]):  
            st.session_state["password_correct"] = True  
            del st.session_state["password"]  # Don't store the password.  
        else:  
            st.session_state["password_correct"] = False  
    # Return True if the passward is validated.  
    if st.session_state.get("password_correct", False):  
        return True  
    # Show input for password.  
    st.text_input(  
        "Password", type="password", on_change=password_entered, key="password"  
    )  
    if "password_correct" in st.session_state:  
        st.error("😕 Password incorrect")  
    return False

def login():
    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Load secrets
        admin_user = st.secrets["credentials"]["admin_user"]
        admin_pass = st.secrets["credentials"]["admin_password"]
        user_user = st.secrets["credentials"]["user_user"]
        user_pass = st.secrets["credentials"]["user_password"]

        # Check admin login
        if username == admin_user and password == admin_pass:
            st.session_state["auth"] = "admin"
            st.success("Logged in as Admin!")
            st.rerun()

        # Check user login
        elif username == user_user and password == user_pass:
            st.session_state["auth"] = "user"
            st.success("Logged in as User!")
            st.rerun()

        else:
            st.error("❌ Incorrect username or password")

def require_login():
    if "logged_in" not in st.session_state or not st.session_state["logged_in"]:
        st.stop()     # stops the page from rendering