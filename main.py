import streamlit as st
from login_app import login
from client_page import show_client_page
from support_page import support_page


if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["username"] = ""
    st.session_state["role"] = ""


if not st.session_state["logged_in"]:
    login()  

else:
    st.sidebar.write(f"Logged in as: {st.session_state['username']} ({st.session_state['role']})")

   
    if st.sidebar.button("Logout"):
        st.session_state["logged_in"] = False
        st.session_state["username"] = ""
        st.session_state["role"] = ""
        st.experimental_rerun()  

   
    if st.session_state["role"] == "Client":
        show_client_page()
    elif st.session_state["role"] == "Support Team":
        support_page()
    else:
        st.error("Invalid role! Please log in again.")
