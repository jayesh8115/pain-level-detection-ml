import streamlit as st
import hashlib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="Login",
    page_icon="🔐",
    layout="centered"
)

# -----------------------------
# Custom CSS
# -----------------------------
st.markdown("""
<style>

.main{
    background-color:#F4F8FB;
}

.login-box{
    padding:30px;
    border-radius:15px;
    background:white;
    box-shadow:0px 5px 20px rgba(0,0,0,0.15);
}

h1{
    text-align:center;
    color:#1565C0;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# Helper Function
# -----------------------------
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# -----------------------------
# Session State
# -----------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

# -----------------------------
# Login Screen
# -----------------------------
st.title("🔐 Login")

st.write("Welcome to the AI Pain Level Detection System")

with st.form("login_form"):

    username = st.text_input(
        "Username",
        placeholder="Enter username"
    )

    password = st.text_input(
        "Password",
        type="password",
        placeholder="Enter password"
    )

    remember = st.checkbox("Remember Me")

    login_btn = st.form_submit_button("Login")

# -----------------------------
# Temporary Demo Login
# Replace with Database Later
# -----------------------------
demo_username = "admin"
demo_password = hash_password("admin123")

if login_btn:

    if username == "":
        st.error("Username cannot be empty.")

    elif password == "":
        st.error("Password cannot be empty.")

    else:

        if (
            username == demo_username
            and hash_password(password) == demo_password
        ):

            st.session_state.logged_in = True
            st.session_state.username = username

            st.success("Login Successful")

            if remember:
                st.info("Remember Me Enabled")

            st.balloons()

        else:

            st.error("Invalid Username or Password")

# -----------------------------
# After Login
# -----------------------------
if st.session_state.logged_in:

    st.success(
        f"Welcome, {st.session_state.username}"
    )

    col1, col2 = st.columns(2)

    with col1:

        if st.button("Go to Dashboard"):

            st.switch_page("pages/Dashboard.py")

    with col2:

        if st.button("Logout"):

            st.session_state.logged_in = False
            st.session_state.username = ""

            st.rerun()

# -----------------------------
# Footer
# -----------------------------
st.divider()

st.caption(
    "AI Pain Level Detection System | Secure Login "
)