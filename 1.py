# Write a python program to create table of Hospital (hosp_id 
# ,hosp_name,contact_no,licenece_no,speciality). Perform the CURD operations 
# using Psycopg2 library.  
# a. Insert 7 records 
# b. Display all the records. 
# c. Update the hospital contact number of Radiance Hospital. And display the 
# records. 
# d. Delete all orthopaedic hospitals and display the records.  

import psycopg2
conn=psycopg2.connect(              #conn is connection object
    dbname="PostgreSQL 17",
    user="postgres" ,
    password="gargi123",
    host="localhost",
    port="5432"
)
cur=conn.cursor()

cur.execute("""DROP TABLE  IF EXISTS Hospital; """)
cur.execute("""
            CREATE TABLE Hospital(hosp_id int primary key,hop_name varchar(50),contact_no bigint,license_no int,
                                  speciality varchar(40));""")
conn.commit()

Hospital=[(1,'Radiance',3827559845,87,'MBBS'),(2,'CAre plus clininc',6735284,78,'Cardio'),(3,'Orthopedic clinic',3874735,98,'Ortho'),
          (4,'Sunrise',284335,54,'EYE'),(5,'Seven star',67328,73,'Child'),(6,'Neuron',834727,387,'Heart'),(7,'Green valley',7534657,345,'Genral')]



cur.executemany("""
                INSERT INTO  Hospital(hosp_id,hosp_name,contact_no,licence_no,specaility)VALUES(%s,%s,%s,%s,%s);""",Hospital)
conn.commit()
print("\nAll hospital records:")
cur.execute("SELECT * FROM HOSPITAL;")
for row in cur.fetchall():
    print(row)


cur.execute(""" UPDATE hospital set contact_no=1453286 where hosp_name='Radiance';""")
conn.commit()
print("\nafter updating the contact no :")
cur.execute(""" SELECT * FROM hospital;""")
for row in cur.fetchall:
    print(row)


cur.execute("""DELETE FROM hospital where speciality='Ortho';""")
conn.commit()
print("\nAfter deleting:")
cur.execute("""SELECT * FROM HOSPITAL;""")
for row in cur.fetchall:
    print(row)
cur.close()
conn.close()
