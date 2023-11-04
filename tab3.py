import streamlit as st
import pandas as pd
import mysql.connector
import numpy as np

def disp(cursor):
    def submitted():
        st.session_state.submitted = True
    def reset():
        st.session_state.submitted = False
    resource_dict = get_resource_dict(cursor)
    resource_names_list = list(resource_dict.keys())
    st.selectbox(label='Resource Name',options = resource_names_list,index=None,key='resource_name',on_change=submitted,placeholder='Select a resource')
    if 'submitted' in st.session_state and st.session_state.submitted == True:
        with st.container():
            operate_str = '''SELECT  `MinimumQuantity`, `Quantity`,`MaximumQuantity` FROM `ResourceInventory`
                            WHERE `ResourceID` = %s;'''
            graph = get_df(cursor,resource_dict[st.session_state.resource_name],operate_str)
            # graph_cols = graph.columns.to_list()
            # st.write(graph_cols)
            columns = graph.columns.to_list()
            rows = graph.values.tolist()[0]
            # print(type(rows),type(columns))
            # print(columns)
            # print(rows)
            data = {
                'Category' : [i for i in columns],
                'Value' : [j for j in rows]
            }
            graph2 = pd.DataFrame(data)
            st.bar_chart(graph2.set_index('Category'))
        with st.container():
            operate_str = '''SELECT NextScheduledMaintenance FROM 
                            ResourceInventory WHERE `ResourceID`=%s;'''
            graph = get_df(cursor,resource_dict[st.session_state.resource_name],operate_str)
            time_stamp = graph.values[0,0]
            date = str(np.datetime_as_string(time_stamp, unit='D'))
            time_component = str(time_stamp).split('T')[1].split(':')[0:2]
            time = ':'.join(time_component)
            display_str = f"The next scheduled Maintenance is on {date} at {time}"
            st.header(display_str)

            operate_str = '''SELECT LastUpdated FROM 
                            ResourceInventory WHERE `ResourceID`=%s;'''            
            graph = get_df(cursor,resource_dict[st.session_state.resource_name],operate_str)
            time_stamp = graph.values[0,0]
            date = str(np.datetime_as_string(time_stamp, unit='D'))
            time_component = str(time_stamp).split('T')[1].split(':')[0:2]
            time = ':'.join(time_component)
            display_str = f"The Last Scheduled Maintenance was on {date} at {time}"
            st.header(display_str)
            
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
