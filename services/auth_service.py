import streamlit as st
from streamlit_cookies_manager import EncryptedCookieManager

from utils.constants import ROLES

# Setup cookie manager
cookies = EncryptedCookieManager(
    password="a_super_secret_password",  # Replace this with something secure!
    prefix="myapp_",  # Optional prefix to avoid conflicts
)

# Make sure cookies are ready
if not cookies.ready():
    st.stop()


def login():
    st.title("Login Page")

    # Default to first role if none selected
    default_index = (
        ROLES.index(st.session_state.role) if st.session_state.role in ROLES else 0
    )
    selected_role = st.selectbox("Select your role:", ROLES, index=default_index)

    if st.button("Login"):
        st.session_state.role = selected_role
        cookies["role"] = selected_role
        cookies.save()
        st.success(f"Logged in as: {selected_role}")
        st.rerun()


def logout():
    st.session_state.role = None
    cookies["role"] = ""  # Clear cookie
    cookies.save()
    st.success("Logged out successfully!")
    st.rerun()
