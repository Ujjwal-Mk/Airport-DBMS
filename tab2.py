import streamlit as st
import mysql.connector
import main as mp
import pandas as pd

def inp_disp(cursor):
    def submitted():
        st.session_state.submitted = True
    def reset():
        st.session_state.submitted = False
    air_names_dict = get_names_dict(cursor)
    air_name_list = list(air_names_dict.keys())
    st.selectbox(label='Airline name',options=air_name_list,index=None,key='airlinename',on_change=submitted, placeholder="Select Any Airline")
    with st.container:
        c1,c2 = st.columns([0.25,0.75])
        with c1:
            if 'submitted' in st.session_state and st.session_state.submitted == True:
                st.dataframe(get_df(cursor,air_names_dict[st.session_state.air_name]))
                reset()
        with c2:
            pass
    with st.container:
        st.header(":red[Revenue] over the months")

        

def get_names_dict(cursor):
    try:
        airline_ids = []
        names = []
        cursor.execute('SELECT AirlineID,AirlineName FROM Airlines')
        airline_data = cursor.fetchall()
        for airline_id, name in airline_data:
             airline_ids.append(airline_id)
             names.append(name)
        airline_dict = dict(zip(names,airline_ids))
        return airline_dict
    except mysql.connector.Error as err:
        print(f"Error: {err}")


def get_df(cursor,char):
    try:
        operate_str = '''SELECT s.type, a1.type as t1  FROM airplanes a1 JOIN
                    airlines a2 ON a1.airline_id = a2.airline_id JOIN
                    services s ON a1.airplane_id = s.airplane_id where a2.airline_id=%s;'''
        cursor.execute(operate_str,(char,))
        cols = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        print(pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]))
        return (pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]))
    except:
        pass
    return None