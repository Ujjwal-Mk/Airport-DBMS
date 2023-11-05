import streamlit as st
import pandas as pd
import mysql.connector
import numpy as np
import time

def disp(cursor):
    st.text("")
    st.header("Resource Inventory")
    st.text("")
    def submitted():
        st.session_state.submitted = True
    def reset():
        st.session_state.submitted = False
    resource_dict = get_resource_dict(cursor)
    resource_names_list = list(resource_dict.keys())
    st.selectbox(label='Resource Name',options = resource_names_list,index=None,key='resource_name',on_change=submitted,placeholder='Select a resource')
    if 'submitted' in st.session_state and st.session_state.submitted == True:
        with st.container():
            c1,c2 = st.columns([0.70,0.30])
            with c1:
                def graph():
                    operate_str = '''SELECT  `MinimumQuantity`, `Quantity`,`MaximumQuantity` FROM `ResourceInventory`
                                    WHERE `ResourceID` = %s;'''
                    graph = get_df(cursor,resource_dict[st.session_state.resource_name],operate_str)
                    columns = graph.columns.to_list()
                    rows = graph.values.tolist()[0]
                    data = {
                        'Category' : columns,
                        'Value' : rows
                    }
                    min1 = int(graph['MinimumQuantity'].values[0])
                    currval = int(graph['Quantity'].values[0])
                    max1 = int(graph['MaximumQuantity'].values[0])
                    st.bar_chart(pd.DataFrame(data).set_index("Category"), height=400, color='#91c2f9')
                    return (min1,currval,max1)
                min1,currval,max1 = graph()
            with c2:
                operate_str = '''SELECT NextScheduledMaintenance FROM 
                                ResourceInventory WHERE `ResourceID`=%s;'''
                graph = get_df(cursor,resource_dict[st.session_state.resource_name],operate_str)
                date = str(graph.NextScheduledMaintenance.values[0]).split("T")[0]
                time = str(graph.NextScheduledMaintenance.values[0]).split("T")[1].split(".")[0]
                st.write("");st.write("");st.write("");st.write("");st.write("");st.write("")
                st.write(f"The next scheduled Maintenance is on :red[{date}] at {time}")

                operate_str = '''SELECT LastUpdated FROM 
                                ResourceInventory WHERE `ResourceID`=%s;'''            
                graph = get_df(cursor,resource_dict[st.session_state.resource_name],operate_str)
                date = str(graph.LastUpdated.values[0]).split("T")[0]
                time = str(graph.LastUpdated.values[0]).split("T")[1].split(".")[0]; st.write("")
                st.write(f"The Last Scheduled Maintenance was on :green[{date}] at {time}")
        with st.container():
            with st.expander('Restock'):
                with st.form("my_form1"):
                    val = st.select_slider("Restock Quantity",options=[i for i in range(min1, max1-currval+1)])
                    submitt = st.form_submit_button("Submit")
                    if submitt:
                        # graph["Quantity"] = int(graph['Quantity'].values[0])+int(val)
                        st.write("Selected Value is : ",val)
                        operate_str = """
                            Update ResourceInventory
                            SET Quantity= %s
                            WHERE `ResourceID` = %s;
                        """
                        data = (currval+val,resource_dict[st.session_state.resource_name])
                        cursor.execute(operate_str,data)
                        st.write("Successfull")
                        st.success(":green[Restocked!]")
            reset()
    
def get_resource_dict(cursor):
    try:
        resource_ids = []
        resource_names = []
        cursor.execute('SELECT `ResourceID`, `ResourceName` FROM ResourceInventory;')
        resource_name = cursor.fetchall()
        for resource_id, resource_name in resource_name:
            resource_ids.append(resource_id)
            resource_names.append(resource_name)
        resource_dict = dict(zip(resource_names,resource_ids))
        return resource_dict
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