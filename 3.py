# Write a python program to create table of temperature (city_id, city_name, 
# avg_max_temperature_celcious , month, ) 
# Perform the CURD operations using Psycopg2 liabrary.  
# a. Insert 7 records 
# b. Display all the records. 
# c. Update the temperature of Pune city in the month of January with increase 
# of 20C And display the records. 
# d. Delete all records in month of March. And display all the records. 

import psycopg2
con=psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=5432
)
cur=con.cursor

cur.execute("""DROP TABLE IF EXISTS TEMP""")
cur.execute("""CREATE TABLE TEMP (city_id int primary key,city_name varchar(50),avg_max_temp_cel int,month varchar(40);""")
con.commit()

TEMP=[(1,'Nagpur',45,'June'),(2,'Pune',23,'January'),(3,'Mumbai',42,'april'),(4,'goa',39,'Feb'),(5,'Patna',42,'july'),
      (6,'Bihar',45,'Sept'),(7,'Bangalore',34,'August')]
cur.execute("""INSERT INTO (city_id,city_name,avg_max_temp_cel,month)VALUES(%s,%s,%s,%s);""")
con.commit()
print("\nDisplay records")
cur.execute("""SELECT * FROM TEMP;""")
for row in cur.fetchall:
    print(row)

cur.execute("""UPDATE TEMP SET avg_max_temp_cel+20 WHERE city_name='Pune' and month='january';""")
con.commit()
print("\nAfter updating:")
cur.execute("""SELECT * FROM TEMP""")
for row in cur.fecthall:
    print(row)

cur.execute("""DELETE FROM TEMP WHERE month='March';""")
con.commit()
print("\nAfter deleting:")
cur.execute("""SELECT * FROM TEMP;""")
for row in cur.fetchall:
    print(row)

cur.close()
con.close()