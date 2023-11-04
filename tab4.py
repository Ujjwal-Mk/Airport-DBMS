import streamlit as st
import mysql.connector
import main as mp
import pandas as pd

def disp(cursor):
    st.header(":orange[Communication and Announcements]")
    st.write("")
    c1,c2,c3 = st.columns(3)
    with st.container():
        with c1:
            st.header(":blue[Recent Incidents]")
            cursor.execute('''SELECT `ResourceID`, `ResourceName` FROM ResourceInventory;''')
            rows = cursor.fetchall()
            for row in rows:
                st.markdown(f'''
                    - {row[1]}
                ''')
        with c2:
            st.header(":red[Emergency]")
            cursor.execute("""SELECT `MessageSubject`, 
                            `MessageBody` FROM `CommunicationLog` WHERE `MessageType` 
                            LIKE ('%Emergency%') ORDER BY `SentDate` DESC LIMIT 5;""")
            rows = cursor.fetchall()
            for row in rows:
                st.markdown(f'''
                    - {row[1]}
                ''')
        with c3:
            st.header(":green[Notification]")
            cursor.execute("""SELECT `MessageSubject`, 
                            `MessageBody` FROM `CommunicationLog` WHERE `MessageType` 
                            LIKE ('%Notification%') ORDER BY `SentDate` DESC LIMIT 5;""")
            rows = cursor.fetchall()
            for row in rows:
                st.markdown(f'''
                    - {row[1]}
                ''')
        