import streamlit as st
import time
import mysql.connector
import pandas as pd
from streamlit_option_menu import option_menu

def ret_db_config():
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "ujjwalmk",
        # "password": "varunbwaj",
        # "database": "airport_staff_management"
        "database": "airport"
        }
    return db_config

import tab1 as tb1, \
       tab2 as tb2, \
       login as lg, \
       user_auth as ua,\
       tab3 as tb3, \
       tab4 as tb4, \
       tab5 as tb5, \
       tab6 as tb6, \
       tab7 as tb7

def homepage(boolean,username,authenticator):
    if boolean:
        st.title("Airport Staff Management")
        progressbar = st.progress(0)
        for i in range(100):
            progressbar.progress(i+1)
            # time.sleep(0.01)

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
                default_index=0,
                # styles={
                #     "container":{"background-color":"#2b2bed"},
                #     "nav-link-selected": {"background-color": "green"}
                # }
            )

            if selected_tab == "Tab 1":
                tb1.display(cursor=cursor)
            elif selected_tab == "Tab 2":
                tb2.inp_disp(cursor=cursor)
            elif selected_tab=="Tab 3":
                st.write("Testing Area")
                tb3.disp()
            elif selected_tab=="Tab 4":
                tb4.disp(cursor=cursor)
            elif selected_tab=="Tab 5":
                tb5.Maintenance(cursor=cursor)
            elif selected_tab=="Tab 6":
                tb6.GHS(cursor=cursor)
            elif selected_tab=="Tab 7":
                try:
                    tb7.disp(cursor)
                except mysql.connector.ProgrammingError as err:
                    st.error("Wrong query!")
            authenticator.logout("Logout","main")

        except mysql.connector.InterfaceError as e:
            st.error("Server is Down, visit back after sometime :)")
        finally:
            if conn:
                conn.commit()
                cursor.close()
                conn.close()


if __name__=="__main__":
    st.set_page_config(layout="wide")
    try:        
        boolean, username, authenticator=ua.login_user()
        homepage(boolean,username,authenticator)
    except:
        pass