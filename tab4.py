import streamlit as st
import mysql.connector
from dbconfig import ret_db_config as db_config
import pandas as pd

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
    st.header(":orange[Communication and Announcements]")
    st.write("")
    c1,c2,c3 = st.columns(3)
    with st.container():
        with c1:
            st.header(":blue[Recent Incidents]")
            cursor.execute('''SELECT `IncidentDescription` FROM `IncidentReport` ORDER BY `IncidentDate` DESC LIMIT 3;''')
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
        conn1 = mysql.connector.connect(**db_config())
        cursor1 = conn1.cursor()
        types=get_types(cursor1)
        print(types)
        with st.expander('New Message'):
            with st.form("my_form2", clear_on_submit=True):
                # print('Hi')
                st.text_input('Message Subject',key='Subject')
                st.text_input("Message Body",key='body')
                # st.text_input('Message Type',key='type',placeholder='Notification Or Emergency')
                radios = st.radio('Message Type',options=types,index=0,key='type')
                st.form_submit_button('Submit',on_click=submitted)

        if 'submitted' in st.session_state and st.session_state.submitted==True:
            # print(st.session_state)
            print(f'{radios},{st.session_state.Subject},{st.session_state.body}')
            try:
                operate_str=f'INSERT INTO CommunicationLog (MessageType, MessageSubject, MessageBody, SentDate) VALUES ({radios},{st.session_state.Subject},{st.session_state.body},CURRENT_TIMESTAMP);'
                print('New Message added')
                cursor1.execute(operate_str)
                conn1.commit()
                cursor1.close()
                conn1.close()
                exit()
            except mysql.connector.ProgrammingError as err:
                print(err)
            st.success("New message added")
            reset()