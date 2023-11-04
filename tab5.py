import streamlit as st
import pandas as pd
# Reports and Energency - ATC
def Maintenance(cursor):
    st.header(":orange[Aircraft Maintenance]")
    st.write("")
    cursor.execute('''
            SELECT `RequestedBy`, `MaintenanceType`, `RequestDate`, `Status`, a0.`AirplaneType`, a0.`AirplaneRegistration` FROM `MaintenanceRequests` as mr
            JOIN `Airplanes` as a0
            ON a0.`AirplaneID`=mr.`AirplaneID`
            UNION ALL
            SELECT a1.`AirlineName` as `RequestedBy`, MaintenanceType,  ScheduledDate,  `Status`, a0.`AirplaneType`, a0.`AirplaneRegistration`
            FROM `MaintenanceSchedule` as ms
            JOIN `Airplanes` as a0
            ON a0.`AirplaneID` = ms.`AirplaneID`
            JOIN `Airlines` as a1
            ON a1.`AirlineID` = a0.`AirlineID`; 
    ''')
    cols = [i[0] for i in cursor.description]
    rows = cursor.fetchall()
    st.dataframe(pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]), use_container_width=True)