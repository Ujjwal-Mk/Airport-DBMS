import mysql.connector
import streamlit_authenticator as stauth

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "varunbwaj",
    "database": "airport_staff_management",
}
def get_usr_info():
    try:
        # Establish a connection to the MySQL database
        connection = mysql.connector.connect(**db_config)

        # Create a cursor object to interact with the database
        cursor = connection.cursor()

        # Initialize empty lists for usernames and passwords
        usernames = []
        passwords = []
        names = []

        # Execute a query to fetch usernames and passwords
        cursor.execute('SELECT username, hashed_pass as password, CONCAT(f_name, " ", l_name) as names FROM airport_staff_management.usr_info;')

        # Fetch all the rows as a list of tuples
        user_data = cursor.fetchall()

        # print(user_data,type(user_data),'\n')

        # Extract usernames and passwords from the fetched data
        for username, password, name in user_data:
            usernames.append(username)
            passwords.append(password)
            names.append(name)

        # print(names)

    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            # Close the cursor and the database connection
            cursor.close()
            connection.close()

    return (names,usernames,passwords)


def add_usr(uname,Pass,f_name,minit,l_name,auth_lvl):
    try:    
        connection = mysql.connector.connect(**db_config)

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