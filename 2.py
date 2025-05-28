# Write a python program to create table of TelevisionShows (show_id, 
# ,show_name,day_telecast ,show_type). Perform the CURD operations using 
# Psycopg2 liabrary.  
# a. Insert 7 records 
# b. Display all the records. 
# c. Change telecast day of the show which currently telecasts on Thursday to 
# Saturday. And display the records. 
# d. Delete all comedy show records and display the records.

import psycopg2
con=psycopg2.connect(
    dbname='' ,
    user="",
    password="",
    host='',
    port=5432
)
cur=con.cursor()
cur.execute("""DROP TABLE IF EXISTS Tvshows""")
cur.execute("""CREATE TABLE Tvshows(show_id int primary key,show_name varchar(30),tele_day varchar(20),show_type varchar(50));""")
con.commit()

Tvshows=[(1,'yrkkh','thursday','serial'),(2,'tmkoc','monday','comedy'),(3,'tkss','saturday','comedy'),(4,'imlie','thursday','serial'),
         (5,'dj','friday','movie'),(6,'shinchan','tuesday','cartoon'),(7,'igt','sunday','program')]
cur.executemany("""INSERT INTO (show_id,show_name,tele_day,show_type) VALUES (%s,%s,%s,%s);,Tvshows""")
con.commit()
print("\nDisplay records")
cur.execute("""SELECT * FROM Tvshows;""")
for row in cur.fetchall:
    print(row)

cur.execute("""UPDATE Tvshows set tele_day='Saturday' where tele_day='thursday';""")
con.commit()
print("\nAfter updating:")
cur.execute("""SELECT * FROM Tvshows;""")
for row in cur.fetchall:
    print(row)

cur.execute("""DELETE FROM Tvshows WHERE show_type='comedy';""")
con.commit()
cur.execute("""SELECT * FROM Tvshows;""")
for row in cur.fetchall:
    print(row)

cur.close()
con.close()

