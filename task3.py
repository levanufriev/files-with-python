import mysql.connector
from mysql.connector import Error
from datetime import datetime

#Creating connection to sql.
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

#Query to insert data to the table.
insert_query= """INSERT INTO t(
   Date, Latin, Cyrillic, Intnumber, Floatnumber)
   VALUES (%s, %s, %s, %s, %s)"""

#Get file name.
filename = input('Enter file name: ')

#Import data to the database.
def import_to_db(fname):
    #Number of added lines.
    added_lines=0
    #Get number of lines in the file.
    with open(fname) as file:
        total_lines=len(file.readlines())
        
    with open(fname) as file:
        for line in file:
            #Split the line.
            words = line.split('||')
            #Save words.
            date = words[0]
            latin = words[1]
            cyrillic = words[2]
            intnumber = int(words[3])
            floatnumber = float(words[4])
            #Add words to the database.
            data = (date, latin, cyrillic, intnumber, floatnumber)
            #Executing query.
            try:
                cursor.execute(insert_query, data)
                added_lines+=1
                print('Imported: '+str(added_lines)+' Left: '+str(total_lines-added_lines))
                connection.commit()
            except:
                connection.rollback()
                

import_to_db(filename)
