import streamlit as st
import mysql.connector
import main as mp
import pandas as pd

def inp_disp(cursor):
    st.text("")
    st.header("Airline Stastictics")
    st.text("")
    def submitted():
        st.session_state.submitted = True
    def reset():
        st.session_state.submitted = False
    air_names_dict = get_names_dict(cursor)
    air_name_list = list(air_names_dict.keys())
    st.selectbox(label='Airline name',options=air_name_list,index=None,key='air_name',on_change=submitted, placeholder="Select Any Airline")
    if 'submitted' in st.session_state and st.session_state.submitted == True:    
        with st.container():
            c1,c2 = st.columns([0.35,0.65])
            with c1:
                operate_str = '''SELECT  a0.`AirplaneRegistration`, a0.`AirplaneType`
                        FROM `Airplanes` as a0
                        JOIN `Airlines` as a1
                        ON a0.`AirlineID`=a1.`AirlineID`
                        WHERE a0.`AirlineID` = %s;'''
                st.dataframe(get_df(cursor,air_names_dict[st.session_state.air_name],operate_str), use_container_width=True)
                reset()
            with c2:
                operate_str = 'SELECT `NumberOfEmployees`, `NumberOfPassengers`as `Total Passengers Flown` \
                                FROM `Airlines` WHERE `AirlineID` = %s;'
                cursor.execute(operate_str,(air_names_dict[st.session_state.air_name],))
                rows = cursor.fetchall()
                for row in rows:
                    st.markdown(f'''
                            - Total Number of Employees: {row[0]}
                            - Total Number of Passengers Flown: {row[1]}
                    ''')
        with st.container():
            st.header("Airplane Count over the months")
            operate_str="""SELECT mac.`AirplaneCount`,mac.`Month`
                        FROM MonthlyAirplaneCount as mac
                        JOIN Airlines as a0 ON mac.AirlineID = a0.AirlineID
                        WHERE mac.AirlineID = %s
                        ORDER BY (mac.Month);"""
            # st.area_chart(get_df(cursor,air_names_dict[st.session_state.air_name],operate_str).set_index("Month"), color='#768b69')
            st.area_chart(get_df(cursor,air_names_dict[st.session_state.air_name],operate_str).set_index("Month"),color='#91c2f9')
            # need to handle multiple years, for now only months have been used
            reset()

        

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


def get_df(cursor,char, operate_str):
    try:
        cursor.execute(operate_str,(char,))
        cols = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        return (pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]))
    except:
        pass
    return None