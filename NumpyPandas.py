# A company collects the monthly salaries (in 1,00,000 Rs.) of 12 employees. 
# Reshape this 1D array into a 3x4 matrix, where each row represents a 
# department, and each column represents employees in that department. 
# Display the original and reshaped array along with their shapes. 

import numpy as np
salaries=np.array([5,7,12,9,3,2,3,4,5,6,7,1])
print("Original array:\n",salaries)
print("Shape of that array is:",salaries.shape)
reshaped_salaries=salaries.reshape(3,4)
print("\nReshaped Array is:",reshaped_salaries)
print("Shape:",reshaped_salaries.shape)

#  Accept an array of hospital bill amount paid by last 10 patients. Compute the 
# total amount. Calculate the total monthly amount assuming these are weekly 
# amounts.  
import numpy as np
bills=np.array([1200,2300,4500,5600])
total_weekly=np.sum(bills)
total_monthly=total_weekly*4

print("Hospital bills form patients",bills)
print("\nTotal weekly amount",total_weekly)
print("\nTotal monthly",total_monthly)

# Store the student’s marks in 6 subjects using NumPy array and generate the 
# following:  
# 1.  Total Marks obtained 
# 2. Average marks  
# 3. Maximum marks 
import numpy as np
marks=([23,45,67,87,56,78])
total_marks=np.sum(marks)
Avg_marks=np.mean(marks)
Maximum_marks=np.max(marks)
print("Marks in 6 subjects:",marks)
print("Total marks obtained",total_marks)
print("Average marks:",Avg_marks)
print("Maximum marks:",Maximum_marks)

# Perform the following operations on two arrays:  
# 1. Addition  
# 2. Multiplication 
# 3. Accept the number from user and add, multiply the array  
# 4. Find the square root of maximum number in each array 
import numpy as np
x=np.array([1,2,3])
y=np.array([5,6,7])
Addition=x+y
product=x*y
num=int(input("Enter number"))
add_num=x+num
mul_num=y*num
sqrt_max1=np.sqrt(np.max(x))
sqrt_max2=np.sqrt(np.max(y))
print("\nAddition of arrays is:",Addition)
print("\nMultiplication of arrays is:",product)
print("\nNew added array",add_num)
print("\nNew multiplied array",mul_num)
print("\nMax sqrt of arrays are:",sqrt_max1,sqrt_max2)

# Create a Pandas DataFrame with the following employee data and display it. 
# Name Age Department 
# Alice 
# Bob 
# 25 
# 30 
# IT 
# HR 
# Charlie 28 Finance 
# Create the DataFrame using pandas. Print the DataFrame. Display the shape of the 
# DataFrame.
import pandas as pd
data={'Name':['Alice','Bob','Charlie'],
      'Age':[25,30,28],
      'Department':['IT','HR','Finance']}
df=pd.DataFrame(data)
print("Employee details:")
print(df)
print("\nshape of the Dataframe:",df.shape)

# Read data from a CSV file named "employees.csv".Display first 5 rows.
import pandas as pd

df=pd.read_csv("employees.csv")
print("first 5 rows of csv file")
print(df.head())

# Given student marks data in a Pandas DataFrame: 
# Student Math  
# Science 
# Jignesh  85  
# Emma 79  
# Mamta 90  
# Sunita 
# 88  
# 78  
# 85  
# 88  
# 92  
# English 
# 92 
# 88 
# 76 
# 80 
# Display students who scored more than 80 in Mathematics. Find students who 
# scored more than 80 in both Mathematics and Science. 

import pandas as pd
data={
    'Student':['Jignesh','Emma','Mamta','Sunita'],
    'Math':[85,79,90,88],'Science':[78,85,88,92],'English':[92,88,76,80]
}
df=pd.DataFrame(data)
print(df)
math_above=df[df['Math']>80]
math_science_above=df[(df['Math']>80)&(df['Science']>80)]
print("Students with marks in maths above 80:")
print(math_above[['Student','Math']])

print("Students with marks in maths and science above 80:")
print(math_science_above[['Student','Math','Science']])

# A store sells three products, and their prices and tax rates. Create a dataframe 
# with initial values considering three columns as product name, price and tax.  
# Add new column in dataframe with name Final Price which is calculated as -    
# Final Price=Price+(Price×Tax Rate) 
# Display the updated dataframe.  
import pandas as pd
product_names=[]
prices=[]
tax_rate=[]
n=int(input("Enter number of products"))
for i in range (n):
    print(f"Enter details for product{i+1}")
    name=input("Product name:")
    price=float(input("Price:"))
    tax=float(input("Tax Rate(As percentage)"))/100

    product_names.append(name)
    prices.append(price)
    tax_rate.append(tax)

df=pd.DataFrame({'Product Name':product_names,'Price':prices,'Tax Rate':tax_rate})
df['Final Price']=df['Price']+(df['Price']*df['Tax Rate'])
print("\nUpdated Dataframe:")
print(df)

# Consider the data of company’s regional sales performance which has columns 
# as – Salesperson name, Region and Sales.  
# Create pandas dataframe for this data. Sort the data based on sales. 

import pandas as pd
# data={
#     'Salesperson':['Riya','Siya','Rahul','Samir'],'Region':['North','South','East','West'],'Sales':[2300,4500,2345,56777]
# }
# df=pd.DataFrame(data)
# print(df)
# sort_data=df.sort_values(by='Sales',ascending=True)
# print(sort_data)

n=int(input("Enter number of sales records"))
salesperson=[]
region=[]
sales=[]
for i in range(n):
    print(f"\nEnter data for record {i+1}")
    salesp=input("salesperson name:")
    reg=input("region:")
    sale=int(input("sales:"))
    salesperson.append(salesp)
    region.append(reg)
    sales.append(sale)

data={'Salesperson':salesperson,'Region':region,'Sales':sales}
df=pd.DataFrame(data)
print(df)
sort_data=df.sort_values(by='Sales',ascending=False)
print(sort_data)






