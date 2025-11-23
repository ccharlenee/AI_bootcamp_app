import streamlit as st
from helper_functions.style import apply_custom_styles
from helper_functions.utility import check_password
from helper_functions.utility import login
from pil import Image

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

blob = bucket.blob(https://storage.cloud.google.com/research_app_method/Methodology.drawio.png)
image_data = blob.download_as_bytes()
img = Image.open(io.BytesIO(image_data))

buffered = io.BytesIO()
img.save(buffered, format="PNG")
img_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")
img_src = f"data:image/png;base64,{img_base64}"
html_code = f'<img src="{img_src}" width="200" style="border-radius:10px;"/>'
st.markdown(html_code, unsafe_allow_html=True)
#st.image(image, use_container_width=True)