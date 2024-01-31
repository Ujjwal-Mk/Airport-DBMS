import streamlit as st
import pandas as pd
# Reports and Energency - ATC
def Maintenance(cursor):
        st.text("")
        st.header("Aircraft Maintenance")
        st.text("")
        #     cursor.callproc("GetMaintenanceData")
        #     cursor.nextset()
        #     cols = [i[0] for i in cursor.description]
        #     rows = cursor.fetchall()
        cursor.callproc("GetMaintenanceData")

        # Fetch the result set and column names
        for result in cursor.stored_results():
                rows = result.fetchall()
                cols = [i[0] for i in result.description]
        st.dataframe(pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]), use_container_width=True)