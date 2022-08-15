import mysql.connector
from mysql.connector import Error

#Creating connection with database.
def create_connection(host_name, database_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            host=host_name,
            database=database_name,
            user=user_name,            
            password=user_password
        )
        print("Connection to MySQL DB successful")
    except Error as e:
        print(f"The error '{e}' occurred")

    return connection

connection = create_connection("localhost", "task1", "root", "root")
cursor = connection.cursor()

#Calling stored procedures.
args=[0]
result=cursor.callproc('sum_of_ints',args)
print("Sum: "+str(result[0]))
    
result=cursor.callproc('median', args)
print("Median: "+str(result[0]))
