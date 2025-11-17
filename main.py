# Set up and run this Streamlit App
import streamlit as st
import pandas as pd
# from helper_functions import llm
from helper_functions.utility import check_password
from helper_functions.utility import login
from logics.customer_query_handler import process_user_message
from helper_functions.style import apply_custom_styles

apply_custom_styles()


# region <--------- Streamlit App Configuration --------->
st.set_page_config(
    layout="centered",
    page_title="Research Papers App"
)
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
    
st.title("NParks Research Summary App")
st.write("Your role:", st.session_state["auth"])

form = st.form(key="form")
form.subheader("Enter your query on your research topic of interest")

#user_prompt = form.text_area("Enter your prompt here", height=200)

if form.form_submit_button("Submit"):
    
    st.toast(f"User Input Submitted - {user_prompt}")

    st.divider()

    response, course_details = process_user_message(user_prompt)
    
    st.write(response)

    st.divider()

    print(course_details)
    df = pd.DataFrame(course_details)
    df 
