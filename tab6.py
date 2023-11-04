import streamlit as st
import pandas as pd

def GHS(cursor):
    st.write("")
    with st.container():
        st.header(":green[Hangar bay]")
        cursor.execute('''
            SELECT 
            GA.`ArrivalDate`, GA.`DepartureDate`, GA.`FlightNumber`, 
            a0.`AirlineName`, 
            a1.`AirplaneType`, a1.`AirplaneRegistration`, 
            GW.`GatewayLocation`
            FROM `GateAllocation` as GA
            JOIN `Airlines` as a0
            ON a0.`AirlineID` = GA.`AirlineID`
            JOIN `Airplanes` as a1
            ON a1.`AirplaneID` = GA.`AirplaneID`
            JOIN `Gateways` as GW
            ON GW.`GatewayID` = GA.`GateID`;
        ''')
        cols = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        st.dataframe(pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]), use_container_width=True)
    with st.container():
        st.header(":green[Ground Handling Service Requests]")
        cursor.execute('''
            SELECT 
            a0.`AirplaneType`, a0.`AirplaneRegistration`,  
            GHR.`GroundHandlingService`, GHR.`RequestDate`, GHR.`Status`
            FROM `GroundHandlingRequests` as GHR
            JOIN `Airplanes` as a0
            ON GHR.`AirplaneID` = a0.`AirplaneID`;
        ''')
        cols = [i[0] for i in cursor.description]
        rows = cursor.fetchall()
        st.dataframe(pd.DataFrame(rows,columns=cols,index=[i for i in range(1,len(rows)+1)]), use_container_width=True)