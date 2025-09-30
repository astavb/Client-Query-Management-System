import streamlit as st
import mysql.connector
from datetime import datetime


def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="support_system"
    )

def fetch_queries():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM client_queries ORDER BY id")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def close_query(query_id):
    conn = get_connection()
    cursor = conn.cursor()
    closed_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor.execute(
            "UPDATE client_queries SET query_status=%s, closed_time=%s WHERE id=%s",
            ("closed", closed_time, query_id)
        )
        conn.commit()
        if cursor.rowcount == 0:
            st.warning(f"No query found with ID {query_id}")
        else:
            st.success(f"Query ID {query_id} closed successfully!")
    except Exception as e:
        st.error(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

def support_page():
    st.title("🛠 Support Team Dashboard")

   
    if "table_placeholder" not in st.session_state:
        st.session_state.table_placeholder = st.empty()
    if "close_query_click" not in st.session_state:
        st.session_state.close_query_click = False


    st.subheader("All Queries")
    queries = fetch_queries()
    st.session_state.table_placeholder.dataframe(queries, use_container_width=True)

    
    st.subheader("Close a Query")
    if "query_id_input" not in st.session_state:
        st.session_state.query_id_input = ""
    st.session_state.query_id_input = st.text_input("Enter the ID of the query to close", st.session_state.query_id_input)

    col1, col2, col3 = st.columns(3)

    
    with col1:
        if st.button("Close Query"):
            st.session_state.close_query_click = True  

   
    if st.session_state.close_query_click:
        query_id = st.session_state.query_id_input.strip()
        if query_id != "":
            close_query(query_id)
            
            st.session_state.table_placeholder.dataframe(fetch_queries(), use_container_width=True)
        else:
            st.warning("Please enter a valid Query ID")
        st.session_state.close_query_click = False  

    
    with col3:
        if st.button("Go to Login"):
            st.session_state["logged_in"] = False
            st.session_state["username"] = ""
            st.session_state["role"] = ""
            st.rerun()
