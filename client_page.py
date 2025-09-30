
import streamlit as st
import mysql.connector


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="support_system"
    )


def save_query(email, mobile, heading, description):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO client_queries (email, mobile, query_heading, query_description) VALUES (%s, %s, %s, %s)"
    values = (email, mobile, heading, description)
    cursor.execute(sql, values)
    conn.commit()
    cursor.close()
    conn.close()


def show_client_page():
    st.title(" Client Support Page")

   
    if "email" not in st.session_state: st.session_state.email = ""
    if "mobile" not in st.session_state: st.session_state.mobile = ""
    if "query_description" not in st.session_state: st.session_state.query_description = ""
    if "query_heading" not in st.session_state: st.session_state.query_heading = "Storage Issue"

    
    st.session_state.email = st.text_input("Email", st.session_state.email)
    st.session_state.mobile = st.text_input("Mobile Number", st.session_state.mobile)
    st.session_state.query_heading = st.selectbox(
        "Query Heading", 
        ["Storage Issue", "Window Error", "Not Able to Login"], 
        index=["Storage Issue", "Window Error", "Not Able to Login"].index(st.session_state.query_heading)
    )
    st.session_state.query_description = st.text_area(
        "Query Description", st.session_state.query_description
    )

    
    col1, col2, col3 = st.columns(3)

   
    with col1:
        if st.button("Submit Query"):
            if st.session_state.email and st.session_state.mobile and st.session_state.query_description:
                save_query(
                    st.session_state.email, 
                    st.session_state.mobile, 
                    st.session_state.query_heading, 
                    st.session_state.query_description
                )
                st.success(" Your query has been submitted")
                
                st.session_state.query_description = ""
                st.session_state.query_heading = "Storage Issue"
            else:
                st.error(" Please fill all the fields")

    
    with col2:
        if st.button("Refresh"):
            st.session_state.email = ""
            st.session_state.mobile = ""
            st.session_state.query_description = ""
            st.session_state.query_heading = "Storage Issue"
            st.rerun()   

   
    with col3:
        if st.button("Go to Login Page"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["role"] = ""
            st.rerun()
