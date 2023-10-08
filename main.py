import streamlit as st
import tab1 as tb1, tab2 as tb2, login as lg
import time
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

check_login=True
st.set_page_config(layout="wide")

# while lg.login_user() and check_login:
#     check_login=False
if lg.login_user():
    st.write("DBMS Mini-Project")
    
    progressbar = st.progress(0)
    for i in range(100):
        progressbar.progress(i+1)
        time.sleep(0.01)

    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "ujjwalmk",
        "database": "art_gallery",
    }
    try:
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        # selected_tab=st.selectbox("Select a Tab", ["Tab 1", "Tab 2", "Tab 3"])
        selected_tab = option_menu(
            menu_title="Main Menu",
            options=["Tab 1","Tab 2","Tab 3"],
            icons=['1-circle-fill','2-circle-fill','3-circle-fill'],
            menu_icon="cast",
            orientation="horizontal",
            default_index=0
        )

        if selected_tab == "Tab 1":
            last_selected_tab=0
            tb1.display(cursor=cursor)
        elif selected_tab == "Tab 2":
            last_selected_tab=1
            # st.write("You entered:", user_input)
            # print(type(user_input))
            # st.write(" ")
            try:
                tb2.inp_disp(cursor)
            except mysql.connector.ProgrammingError as err:
                st.error("Wrong query!")
        elif selected_tab=="Tab 3":
            last_selected_tab=2
            st.write("Work in progress")
    except mysql.connector.InterfaceError as e:
        st.error("Server is Down, visit back after sometime :)")