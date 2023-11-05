import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import altair as alt
def display(cursor):
    st.text("")
    st.header("General Airport Information")
    st.text("")
    # st.write("This is the content for Tab 1.")
    x1,x2 = st.columns([0.25,0.75])
    with x1:
        with st.container():
            cursor.execute("select AirlineName from airlines;")
            cols=[i[0] for i in cursor.description]
            rows=cursor.fetchall()
            st.header("Unique Airlines:")
            df = pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)])
            st.dataframe(df, use_container_width=True)
    with x2:
        with st.container():
            cursor.execute("select count(*) as UniqueAirLines, a1.AirlineName \
                          from airplanes as a0 join airlines \
                          as a1 on a0.AirlineID=a1.AirlineID group by a1.AirlineID;")
            cols1 = [i[0] for i in cursor.description]
            rows1=cursor.fetchall()
            st.header("Number of unique Airlines in the airport")
            graph = pd.DataFrame(rows1, columns=cols1, index=[i for i in range(1,len(rows1)+1)]).set_index(cols1[1])
            st.bar_chart(graph,color='#768b69')