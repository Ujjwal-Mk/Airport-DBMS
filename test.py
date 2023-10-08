import mysql.connector
import streamlit_authenticator as stauth
# # Database connection parameters

# db_config = {
#     "host": "localhost",
#     "user": "root",
#     "password": "varunbwaj",
#     "database": "airport_staff_management",
# }

# try:
#     # Establish a connection to the MySQL database
#     connection = mysql.connector.connect(**db_config)

#     # Create a cursor object to interact with the database
#     cursor = connection.cursor()

#     f_names, minits, l_names, usernames, Passes, auth_levels = [],[],[],[],[],[]

#     # hashed_password = stauth.Hasher(pass_word).generate()[0]
#     # print(hashed_password)

#     # # execute_str = f"SELECT InsertPassword('{hashed_password}')"
#     # execute_str = f"INSERT INTO  test(hashed_pass) VALUES ('{hashed_password}');"
#     # print(execute_str)

#     # Execute a query to fetch usernames and passwords
#     operate_str = 'SELECT f_name, minit, l_name, username, hashed_pass as Pass, auth_level FROM airport_staff_management.usr_info1;'
#     cursor.execute(operate_str)

#     # # Fetch all the rows as a list of tuples
#     user_data = cursor.fetchall()
#     for f_name, minit, l_name, username, Pass, auth_level in user_data:
#         f_names.append(f_name)
#         minits.append(minit)
#         l_names.append(l_name)
#         usernames.append(username)
#         Passes.append(Pass)
#         auth_levels.append(auth_level)

#     hashed_passes = stauth.Hasher(Passes).generate()

#     print(usernames,"\n",Passes,"\n",hashed_passes,"\n")

#     for i in range(len(usernames)):
#         operate_str1 = 'INSERT INTO usr_info (f_name,minit,l_name,username,hashed_pass,auth_level) VALUES (%s,%s,%s,%s,%s,%s)'
#         data = (f_names[i],minits[i],l_names[i],usernames[i],hashed_passes[i],auth_levels[i])
#         # print(operate_str1,"\n")
#         cursor.execute(operate_str1,data)
#         cursor.fetchall()

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
# finally:
#     if connection:
#         # Close the cursor and the database connection
#         connection.commit()
#         cursor.close()
#         connection.close()

# # # Now, you have the usernames and passwords in the lists
# # print("Usernames:", usernames)
# # print("Passwords:", passwords)

pass1 = "pass123"
pass2 = "'pass123'"

passes = []
passes.append(pass1)
passes.append(pass2)
h_pass = stauth.Hasher(passes).generate()
hp1 = h_pass[0]
hp2 = h_pass[1]
hp = '$2b$12$bfijJLCDWpQ2B1MhFLKc9OjgcEGjaB65LaFepUTlb1BmGecxupW3K'
print('\n',hp1,'\n',hp2,'\n',hp,'\n',hp1==hp,'\n',hp2==hp)