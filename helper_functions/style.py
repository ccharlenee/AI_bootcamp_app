import streamlit as st

def apply_custom_styles():
    
    st.markdown("""
        <style>
        /* Import Google Font */
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600&display=swap');

        /* Global font */
        html, body, [class*="css"] {
            font-family: 'Poppins', sans-serif !important;
            color: #222222;
        }

        /* Page Title */
        h1 {
            font-weight: 600 !important;
            letter-spacing: -0.5px;
            padding-bottom: 0.3rem;
        }

        h2, h3 {
            font-weight: 500 !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"] {
            background-color: #ffffff;
            border-right: 1px solid #ececec;
        }

        /* Buttons */
        .stButton>button {
            background-color: #ff385c !important;
            color: white !important;
            border-radius: 8px;
            padding: 0.6rem 1.2rem;
            font-weight: 500;
            border: none;
        }
        .stButton>button:hover {
            background-color: #e81e50 !important;
        }

        /* Inputs */
        input, textarea, select {
            border-radius: 8px !important;
        }

        /* Card Style */
        .card {
            padding: 1.2rem;
            background: #ffffff;
            border: 1px solid #ececec;
            border-radius: 12px;
            margin-bottom: 1rem;
        }

        /* Center helper */
        .center { text-align: center; }

        </style>
    """, unsafe_allow_html=True)