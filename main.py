import streamlit as st
import tab1 as tb1, tab2 as tb2, login as lg, user_auth as ua, tab3 as tb3, tab4 as tb4
import time
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

check_login=True
st.set_page_config(layout="wide")

# while lg.login_user() and check_login:
#     check_login=False
st.title("Airport Staff Management")
def homepage():
    if boolean:
        st.title("Airport Staff Management")
        progressbar = st.progress(0)
        for i in range(100):
            progressbar.progress(i+1)
            time.sleep(0.01)
        db_config = {
            "host": "localhost",
            "user": "root",
            "password": "ujjwalmk",
            # "password": "varunbwaj",
            "database": "art_gallery",
        }
        try:
            conn = mysql.connector.connect(**ret_db_config())
            cursor = conn.cursor()    
            auth_icons, auth_options = ua.get_options(username)
            selected_tab = option_menu(
                menu_title="Main Menu",
                options=auth_options,
                icons=auth_icons,
                menu_icon="cast",
                orientation="horizontal",
                default_index=0
            )

            if selected_tab == "Tab 1":
                last_selected_tab=0
                tb1.display(cursor=cursor)
            elif selected_tab == "Tab 2":
                last_selected_tab=1
                try:
                    tb2.inp_disp(cursor)
                except mysql.connector.ProgrammingError as err:
                    st.error("Wrong query!")
            elif selected_tab=="Tab 3":
                last_selected_tab=2
                st.write("Work in progress")
            
            auth.logout("Logout","main")
        except mysql.connector.InterfaceError as e:
            st.error("Server is Down, visit back after sometime :)")
            # Comment bro

try:
    boolean, auth=ua.login_user()
    homepage()
except:
    pass