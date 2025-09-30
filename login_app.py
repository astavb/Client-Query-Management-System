import streamlit as st

USER_CREDENTIALS = {
    "admin": {"password": "12345", "role": "Support Team"},
    "vijay": {"password": "vijay2728", "role": "Client"}
}

def login():
    st.title(" Login Page")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")
    role = st.selectbox("Select Role", ["Client", "Support Team"])

    if st.button("Login"):
        if (username in USER_CREDENTIALS and 
            USER_CREDENTIALS[username]["password"] == password and 
            USER_CREDENTIALS[username]["role"] == role):
            
            st.session_state["logged_in"] = True
            st.session_state["username"] = username
            st.session_state["role"] = role
            st.success(f"Welcome, {username}  ({role})")
        else:
            st.error("Invalid username, password, or role")
