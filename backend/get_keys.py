import mysql.connector
import streamlit_authenticator as stauth
import pathlib, sys
module_dir = pathlib.Path(__file__).parent.parent
sys.path.append(str(module_dir))
from backend.dbconfig import ret_db_config
# Database connection parameters

import mysql.connector

def get_usr_info():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**ret_db_config())

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Initialize empty lists for usernames and passwords
        usernames = []
        passwords = []
        names = []

        # Execute a query to fetch usernames and passwords
        cursor.execute('SELECT username, hashed_pass as password, CONCAT(f_name, " ", l_name) as names FROM usr_info;')

        # Fetch all the rows as a list of tuples
        user_data = cursor.fetchall()

        # print(user_data,type(user_data),'\n')

        # Extract usernames and passwords from the fetched data
        for username, password, name in user_data:
            usernames.append(username)
            passwords.append(password)
            names.append(name)

    except mysql.connector.Error as err:
        # Handle specific errors and raise a custom exception for InterfaceError
        if isinstance(err, mysql.connector.InterfaceError):
            raise CustomDatabaseError("Database connection error")
        else:
            print(f"Error: {err} get_usr_info",**ret_db_config())
    finally:
        if connection:
            # Close the cursor and the database connection
            cursor.close()
            connection.close()

    return (names, usernames, passwords)

# Custom exception class
class CustomDatabaseError(Exception):
    pass



def add_usr(uname,Pass,f_name,minit,l_name,auth_lvl):
    try:    
        connection = mysql.connector.connect(**ret_db_config())

        cursor = connection.cursor()
        dummy_list = []
        dummy_list.append(Pass)
        hash_pass = stauth.Hasher(dummy_list).generate()[0]

        operate_str = 'INSERT INTO usr_info (f_name,minit,l_name,username,hashed_pass,auth_level) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (f_name,minit,l_name,uname,hash_pass,auth_lvl)

        cursor.execute(operate_str,data)

        operate_str1 = 'INSERT INTO usr_info1 (f_name,minit,l_name,username,hashed_pass,auth_level) VALUES (%s,%s,%s,%s,%s,%s)'
        data = (f_name,minit,l_name,uname,Pass,auth_lvl)
        cursor.execute(operate_str1,data)
        print("\nnew user added\n")


    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            connection.commit()
            cursor.close()
            connection.close()
def get_level(username):
    try:
        connection = mysql.connector.connect(**ret_db_config())
        cursor = connection.cursor()
        auth_levels = []
        operate_str1 = (f"SELECT auth_level FROM usr_info WHERE username='{username}'")
        # print(operate_str1)
        cursor.execute(operate_str1)
        user_data = cursor.fetchall()

        for level in user_data:
            auth_levels.append(level)
        # print(auth_levels)
        # print(type(auth_levels[0]))
        # print(type(auth_levels[0][0]))
        return auth_levels[0][0]
    
    except mysql.connector.Error as err:
        print(f"Error{err}")
    finally:
        if connection:
            # connection.commit()
            cursor.close()
            connection.close()
# print(get_level('admin'))