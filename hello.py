import streamlit as st
st.write("DBMS Mini-Project")
# st.sidebar()

import time
progressbar = st.progress(0)
for i in range(100):
    progressbar.progress(i+1)
    time.sleep(0.01)

import mysql.connector
import pandas as pd

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "ujjwalmk",
    "database": "art_gallery",
}

conn = mysql.connector.connect(**db_config)

cursor = conn.cursor()

cursor.execute("SELECT * FROM art")
cols=[i[0] for i in cursor.description]
# st.write(cols)

rows=cursor.fetchall()
st.write("Data from MySQL Database:")



st.sidebar.title("Tabs")
selected_tab = st.sidebar.radio("Select a Tab", ["Tab 1", "Tab 2", "Tab 3"])

if selected_tab == "Tab 1":
    st.title("Tab 1 Content")
    st.write("This is the content for Tab 1.")
    st.dataframe(pd.DataFrame(rows,columns=cols))

elif selected_tab == "Tab 2":
    st.title("Tab 2 Content")
    st.write("This is the content for Tab 2.")

elif selected_tab == "Tab 3":
    st.title("Tab 3 Content")
    st.write("This is the content for Tab 3.")
