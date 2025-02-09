import mysql.connector

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='',
        database = 'indigo'
    )
    mycursor = conn.cursor()
    print('Connection Established')
except:
    print('Connection Error')
#mycursor.execute("CREATE DATABASE indigo")
#conn.commit()

#create table
#airport
#mycursor.execute("""
#CREATE TABLE airport (
     #airport_id INTEGER PRIMARY KEY,
     #code VARCHAR(10) NOT NULL,
     #city VARCHAR(50) NOT NULL,
     #name VARCHAR(255) NOT NULL
#)
#""")
#conn.commit()
#mycursor.execute("""
    #INSERT INTO airport VALUES
    #(1,'DEL','New Delhi' ,'IGIA'),
    #(2,'CCU','Kolakata' ,'NSCA')
#""")
#conn.commit()

# mycursor.execute("SELECT * FROM airport WHERE airport_id >1")
# data =mycursor.fetchall()
# print(data)

