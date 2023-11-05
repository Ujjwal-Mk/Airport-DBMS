import streamlit as st
import mysql.connector
from dbconfig import ret_db_config as db_config
import pandas as pd
import main as mp
def get_types(cursor):
    cursor.execute('SELECT DISTINCT `MessageType` FROM `CommunicationLog`;')
    rows = cursor.fetchall()
    for i in range(len(rows)):
        rows[i] = rows[i][0]
    return rows

def submitted():
    st.session_state.submitted = True
def reset():
    st.session_state.submitted = False

def disp(cursor, conn):
    st.text("")
    st.header("Communication and Announcements")
    st.text("")
    c1,c2,c3 = st.columns(3)
    with st.container():
        with c1:
            st.header(":blue[Recent Incidents]")
            cursor.execute('''SELECT `IncidentDescription` FROM `IncidentReport` \
                            ORDER BY `IncidentDate` DESC LIMIT 3;''')
            rows = cursor.fetchall()
            for row in rows:
                st.markdown(f'''
                    - {row[0]}
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
    with st.container():
        st.write("");st.header("Push New Message?")
        Subject=None;body=None;radios=None
        with st.form("my_form2", clear_on_submit=True):
            st.text_input('Message Subject',key='Subject')
            st.text_input("Message Body",key='body')
            radios = st.radio('Message Type',options=get_types(cursor))
            st.form_submit_button('Submit',on_click=submitted)
            Subject=str(st.session_state.Subject)
            body=str(st.session_state.body)
        if Subject!=None and radios!=None and body!=None and Subject!="" and body!="" and radios!="":
            if 'submitted' in st.session_state and st.session_state.submitted==True:
                operate_str=f"INSERT INTO CommunicationLog (MessageType,\
                            MessageSubject, MessageBody, SentDate)\
                            VALUES ('{radios}', '{Subject}', '{body}', CURRENT_TIMESTAMP);"
                cursor.execute(operate_str)
                conn.commit()
                st.success("New message added")
                reset()