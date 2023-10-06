import streamlit as st
import pandas as pd

def inp_disp(cursor):
    st.title("Tab 2 Content")
    st.write("This is the content for Tab 2.")
    user_input = st.text_area("Enter text here")
    if st.button("Submit"):
        cursor.execute(user_input)
    # del cols
    if cursor.description!=None:
        cols=[i[0] for i in cursor.description]
        rows=cursor.fetchall()
        st.dataframe(pd.DataFrame(rows,columns=cols))
        st.success("retrieved successfully")
