import streamlit as st
st.set_page_config(layout="wide")
st.write("DBMS Mini-Project")
# st.sidebar()
import tab1 as tb1, tab2 as tb2
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



st.sidebar.title("Tabs")
selected_tab = st.sidebar.radio("Select a Tab", ["Tab 1", "Tab 2", "Tab 3"])

if selected_tab == "Tab 1":
    tb1.display(cursor=cursor)

elif selected_tab == "Tab 2":

    # st.write("You entered:", user_input)
    # print(type(user_input))
    # st.write(" ")
    try:
        tb2.inp_disp(cursor)
    except mysql.connector.ProgrammingError as err:
        st.error("Wrong query!")

    

elif selected_tab == "Tab 3":
    st.title("Tab 3 Content")
    st.write("This is the content for Tab 3.")
