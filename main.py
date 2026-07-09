import streamlit as st

# --------------------------------------------------------
# Page Configuration
# --------------------------------------------------------

st.set_page_config(
    page_title="Pain Detection System",
    page_icon="🩺",
    layout="wide"
)

# --------------------------------------------------------
# Session Initialization
# --------------------------------------------------------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# --------------------------------------------------------
# Redirect
# --------------------------------------------------------

if st.session_state.logged_in:
    st.switch_page("pages/Dashboard.py")
else:
    st.switch_page("pages/Login.py")