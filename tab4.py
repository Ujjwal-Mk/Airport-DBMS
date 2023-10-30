import streamlit as st
import mysql.connector
import main as mp
import pandas as pd
def disp():
    def submitted():
         st.session_state.submitted = True
    def reset():
         st.session_state.submitted = False
    air_names_dict = get_names_dict()
    air_name_list = list(air_names_dict.keys())
    st.selectbox('Airline name',air_name_list,index=0,key='air_name',on_change=submitted)
    if 'submitted' in st.session_state and st.session_state.submitted == True:
        # st.write(air_names_dict[st.session_state.air_name])
        airplane_df = get_df(air_names_dict[st.session_state.air_name])
        st.dataframe(airplane_df)
        reset()
    # st.write("Testing")
    # if st.button("Hello"):
    #     test_dict = get_names_dict()
    #     st.write(test_dict)
    #     st.write(list(test_dict.keys()))
    #     st.write(test_dict[list(test_dict.keys())[0]])
         
    


def get_names_dict():
    try:
        connection = mysql.connector.connect(**mp.ret_db_config())

        cursor = connection.cursor()

        airline_ids = []
        names = []

        cursor.execute('SELECT * FROM Airlines;')

        airline_data = cursor.fetchall()

        for airline_id, name in airline_data:
             airline_ids.append(airline_id)
             names.append(name)

        airline_dict = dict(zip(names,airline_ids))
        return airline_dict

    except mysql.connector.Error as err:
            print(f"Error: {err}")
    finally:
        if connection:
            # Close the cursor and the database connection
            cursor.close()
            connection.close()


def get_df(char):
    try:
        connection = mysql.connector.connect(**mp.ret_db_config()) 

        cursor = connection.cursor()

        operate_str = 'SELECT airplane_id, type FROM `Airplanes` WHERE airline_id=%s;'
        data = (char,)

        cursor.execute(operate_str,data)
        
        cols = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        
        return (pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]))

    except:
        pass

    return None