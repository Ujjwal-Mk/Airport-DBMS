import mysql.connector

# Database connection parameters
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "varunbwaj",
    "database": "mysql",
}

# Initialize empty lists for usernames and passwords
usernames = []
passwords = []

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(**db_config)

    # Create a cursor object to interact with the database
    cursor = connection.cursor()

    # Execute a query to fetch usernames and passwords
    cursor.execute("SELECT User, authentication_string FROM mysql.user")

    # Fetch all the rows as a list of tuples
    user_data = cursor.fetchall()

    # Extract usernames and passwords from the fetched data
    for username, password in user_data:
        usernames.append(username)
        passwords.append(password)

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    if connection:
        # Close the cursor and the database connection
        cursor.close()
        connection.close()

# Now, you have the usernames and passwords in the lists
print("Usernames:", usernames)
print("Passwords:", passwords)
