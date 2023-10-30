import streamlit as st
import pandas as pd
def display(cursor):
    st.title("Tab 1 Content")
    st.write("This is the content for Tab 1.")
    cursor.execute("SELECT name FROM Airlines")
    cols=[i[0] for i in cursor.description]
    rows=cursor.fetchall()
    st.write("Data from MySQL Database:")
    df = pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)])
    st.dataframe(df)