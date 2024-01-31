import streamlit as st
import pandas as pd

def GHS(cursor):
    st.write("")
    with st.container():
        st.header("Hangar bay")
        cursor.callproc("GetMaintenanceData1")  
        for result in cursor.stored_results():
            rows = result.fetchall()
            cols = [i[0] for i in result.description]

        st.dataframe(pd.DataFrame(rows, columns=cols,index=[i for i in range(1,len(rows)+1)]),use_container_width=True)

    with st.container():
        st.header("Ground Handling Service Requests")
        # cursor.execute('''
        #     SELECT 
        #     a0.`AirplaneType`, a0.`AirplaneRegistration`,  
        #     GHR.`GroundHandlingService`, GHR.`RequestDate`, GHR.`Status`
        #     FROM `GroundHandlingRequests` as GHR
        #     JOIN `Airplanes` as a0
        #     ON GHR.`AirplaneID` = a0.`AirplaneID`;
        # ''')
        # cols = [i[0] for i in cursor.description]
        # rows = cursor.fetchall()
        cursor.callproc("GetGroundHandlingServiceData")  # Replace with your procedure name

        # Fetch the result set
        for result in cursor.stored_results():
            rows = result.fetchall()
            cols = [i[0] for i in result.description]

        # Convert the result to a Pandas DataFrame
        st.dataframe(pd.DataFrame(rows, columns=cols,index=[i for i in range(1,len(rows)+1)]), use_container_width=True)