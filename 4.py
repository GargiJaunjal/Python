# Write a python program to create table of Company (company_id, 
# company_name, avg_salary, noOfemplolyees , TypeofCompany) 
# Perform the CURD operations using Psycopg2 library.  
# a. Accept the details from user. (Total Number of Companies, use sequence 
# data type to store all the employees) 
# b. Display all the records. 
# c. Update the number of employees of ___ company. (Accept the number of 
# employees from user.) 
# d. Give the total number of companies having more than 50 employees. 
# e. Delete all records of service type companies. (Print before and after count 
# of service type companies.)

import psycopg2
con=psycopg2.connect(
    dbname='',
    user='',
    password='',
    host='',
    port=5432
)
cur=con.cursor
cur.execute("""DROP TABLE IF EXISTS Company""")
cur.execute("""CREATE TABLE Company (company_id int primary key,comp_name varchar(50),avg_sal int,no_emps int,type_comp varchar(50));""")
con.commit()
n=int(input("Enter number of companies:"))
for i in range(n):
    name=input(f"Name of company {i+1}")
    id=int(input("id of company:"))
    salary=int(input(" Salary:"))
    no=int(input("Number of employees"))
    type=input("Company type:")
cur.execute("""INSERT INTO Company (company_id,comp_name,avg_sal,no_emps,type_comp) VALUES (%s,%s,%s,%s,%s);,Company""")
con.commit()
print("\nDisplay the records")
cur.execute("""SELECT * FROM Company;""")
for row in cur.fetchall:
    print(row)

name=input("\nEnter the company name to update employee count:")
new_count=int(input("Enter new number of employees"))
cur.execute("""UPDATE Company SET no_emps=%s WHERE comp_name=%s""" ,(new_count,name))
con.commit()
print("Employee count updated")

cur.execute("""SELECT COUNT(*) FROM Company WHERE type_comp like 'service';""")
before=cur.fetchone()[0]
print(f"\nservice companies before deletion")

cur.execute("""DELETE FROM Company WHERE type_comp like 'service';""")
con.commit()

cur.execute("""SELECT COUNT(*) FROM Company WHERE type_comp like 'service';""")
after=cur.fetchone()[0]
print(f"\nservice companies after deletion")

cur.execute("""SELECT * FROM Company;""")
print("\n Company records after operations:")
for row in cur.fetchall:
    print(row)

cur.close()
con.close()











































