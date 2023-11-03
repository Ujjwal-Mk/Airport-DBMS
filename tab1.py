import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
def display(cursor):
    st.header("General Airport Information")
    # st.write("This is the content for Tab 1.")
    x1,x2 = st.columns([0.2,0.8])
    with x1:
        with st.container():
            cursor.execute("select AirlineName from airlines;")
            cols=[i[0] for i in cursor.description]
            rows=cursor.fetchall()
            st.write("Data from MySQL Database:")
            df = pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)])
            st.dataframe(df)
    with x2:
        with st.container():
            cursor.execute("SELECT count(*) as Numberofairplanes, \
                            a1.name from Airplanes a0 inner join airlines a1 on \
                            a1.airline_id=a0.airline_id group by a0.airline_id")
            cols1 = [i[0] for i in cursor.description]
            rows1=cursor.fetchall()
            st.header("Number of unique Airlines in the airport")
            graph = pd.DataFrame(rows1, columns=cols1, index=[i for i in range(1,len(rows1)+1)])
            st.bar_chart(graph.set_index('name'))