# Import pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom','eshan','aman','ram'],
    'Age': [28, 24, 35, 32, 40,33,44,55],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo','city1','city2','city3']
}
df = pd.DataFrame(data)

# Head: returns the first 5 rows of the DataFrame
print("Head:")
print(df.head())

# Tail: returns the last 5 rows of the DataFrame
print("\nTail:")
print(df.tail())

# Info: returns a concise summary of the DataFrame 
print("\nInfo:")
print(df.info())

# Describe: generates descriptive statistics for numeric columns
print("\nDescribe:")    
print(df.describe())

# Loc: label-based data selection
print("Loc:")
print(df.loc[0, 'Name'])  # selects the value at row 0, column 'Name'
print(df.loc[0:2, 'Name':'Age'])  # selects rows 0-2, columns 'Name' to 'Age'

# Iloc: integer-based data selection
print("\nIloc:")
print(df.iloc[0, 0])  # selects the value at row 0, column 0
print(df.iloc[0:2, 0:2])  # selects rows 0-1, columns 0-1


# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'John', 'Anna', 'Peter'],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo', 'New York', 'Paris', 'Berlin'],
    'Sales': [100, 200, 300, 400, 500, 100, 200, 300]
}
df = pd.DataFrame(data)

# Groupby: groups the data by one or more columns and applies an aggregation function
print("Groupby:")

print(df.groupby('City')['Sales'].sum())

# Pivot_table: creates a spreadsheet-style pivot table as a DataFrame
print("\nPivot_table:")
print(df.pivot_table(index='City', values='Sales', aggfunc='sum'))



# Create sample DataFrames
data1 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df2 = pd.DataFrame(data2)

# Merge: combines two DataFrames based on a common column
print("Merge:")
print(pd.merge(df1, df2, on='Name'))

# Join: combines two DataFrames based on their indices
print("\nJoin:")
print(df1.set_index('Name').join(df2.set_index('Name')))


# Create a sample DataFrame with duplicate rows
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'John', 'Anna'],
    'Age': [28, 24, 35, 32, 28, 24]
}
df = pd.DataFrame(data)

# Drop_duplicates: removes duplicate rows
print("Drop_duplicates:")
print(df.drop_duplicates())



# Create a sample DataFrame with missing values
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, None, 32]
}
df = pd.DataFrame(data)

# Dropna: removes rows with missing values
print("\nDropna:")
df3=df.dropna()
print(df3)

# Sort by Age in ascending order
df_sorted = df3.sort_values('Age')
print(df_sorted)


# Create a DataFrame
data = {'City': ['New York', 'New York', 'Paris', 'Paris', 'Berlin', 'Berlin'],
        'Sales': [100, 200, 50, 75, 150, 225]}
df = pd.DataFrame(data)

# Group by City and calculate the sum of Sales
df_grouped = df.groupby('City')['Sales'].sum()

print(df_grouped)


# Create three DataFrames
df1 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'Age': [28, 24, 35, 32]})
df2 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'City': ['New York', 'Paris', 'Berlin', 'London']})
df3 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'Country': ['USA', 'France', 'Germany', 'UK']})

# Merge the three DataFrames
df_merged = pd.merge(df1, df2, on='Name')
df_merged = pd.merge(df_merged, df3, on='Name')

print(df_merged)


# Create a DataFrame
data = {'Name': ['John', 'John', 'Anna', 'Anna', 'Peter', 'Peter'],
        'Year': [2020, 2021, 2020, 2021, 2020, 2021],
        'Sales': [100, 200, 50, 75, 150, 225]}
df = pd.DataFrame(data)
print(df)
# Pivot the data
df_pivoted = pd.pivot_table(df, values='Sales', index='Name', columns='Year')

print(df_pivoted)

 #q2


import pandas as pd

# Define the SensorHealthReport data
sensor_data = [
    {"sensor_id": "TEMP_01", "timestamp": 10.5, "status": "OK", "temperature": 45.2},
    {"sensor_id": "BRAKE_02", "timestamp": 20.1, "status": "WARN", "temperature": 60.3},
    {"sensor_id": "TEMP_01", "timestamp": 30.7, "status": "FAIL", "temperature": 75.0},
    {"sensor_id": "BRAKE_02", "timestamp": 40.2, "status": "OK", "temperature": 50.1},
    {"sensor_id": "TEMP_01", "timestamp": 50.9, "status": "WARN", "temperature": 65.4}
]

# Convert to DataFrame
df = pd.DataFrame(sensor_data)

# Group by status and calculate count and average temperature
result = df.groupby("status").agg(
    count=("status", "size"),
    average_temperature=("temperature", "mean")
)

# Display the result
print(result)

#ex3

# Import pandas library
import pandas as pd

# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom','eshan','aman','ram'],
    'Age': [28, 24, 35, 32, 40,33,44,55],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo','city1','city2','city3']
}
df = pd.DataFrame(data)

# Head: returns the first 5 rows of the DataFrame
print("Head:")
print(df.head())

# Tail: returns the last 5 rows of the DataFrame
print("\nTail:")
print(df.tail())

# Info: returns a concise summary of the DataFrame
print("\nInfo:")
print(df.info())

# Describe: generates descriptive statistics for numeric columns
print("\nDescribe:")
print(df.describe())

# Loc: label-based data selection
print("Loc:")
print(df.loc[0, 'Name'])  # selects the value at row 0, column 'Name'
print(df.loc[0:2, 'Name':'Age'])  # selects rows 0-2, columns 'Name' to 'Age'

# Iloc: integer-based data selection
print("\nIloc:")
print(df.iloc[0, 0])  # selects the value at row 0, column 0
print(df.iloc[0:2, 0:2])  # selects rows 0-1, columns 0-1


# Create a sample DataFrame
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'Tom', 'John', 'Anna', 'Peter'],
    'City': ['New York', 'Paris', 'Berlin', 'London', 'Tokyo', 'New York', 'Paris', 'Berlin'],
    'Sales': [100, 200, 300, 400, 500, 100, 200, 300]
}
df = pd.DataFrame(data)

# Groupby: groups the data by one or more columns and applies an aggregation function
print("Groupby:")

print(df.groupby('City')['Sales'].sum())

# Pivot_table: creates a spreadsheet-style pivot table as a DataFrame
print("\nPivot_table:")
print(df.pivot_table(index='City', values='Sales', aggfunc='sum'))



# Create sample DataFrames
data1 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, 35, 32]
}
df1 = pd.DataFrame(data1)

data2 = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
}
df2 = pd.DataFrame(data2)

# Merge: combines two DataFrames based on a common column
print("Merge:")
print(pd.merge(df1, df2, on='Name'))

# Join: combines two DataFrames based on their indices
print("\nJoin:")
print(df1.set_index('Name').join(df2.set_index('Name')))


# Create a sample DataFrame with duplicate rows
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda', 'John', 'Anna'],
    'Age': [28, 24, 35, 32, 28, 24]
}
df = pd.DataFrame(data)

# Drop_duplicates: removes duplicate rows
print("Drop_duplicates:")
print(df.drop_duplicates())



# Create a sample DataFrame with missing values
data = {
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 24, None, 32]
}
df = pd.DataFrame(data)

# Dropna: removes rows with missing values
print("\nDropna:")
df3=df.dropna()
print(df3)

# Sort by Age in ascending order
df_sorted = df3.sort_values('Age')
print(df_sorted)


# Create a DataFrame
data = {'City': ['New York', 'New York', 'Paris', 'Paris', 'Berlin', 'Berlin'],
        'Sales': [100, 200, 50, 75, 150, 225]}
df = pd.DataFrame(data)

# Group by City and calculate the sum of Sales
df_grouped = df.groupby('City')['Sales'].sum()

print(df_grouped)


# Create three DataFrames
df1 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'Age': [28, 24, 35, 32]})
df2 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'City': ['New York', 'Paris', 'Berlin', 'London']})
df3 = pd.DataFrame({'Name': ['John', 'Anna', 'Peter', 'Linda'],
                    'Country': ['USA', 'France', 'Germany', 'UK']})

# Merge the three DataFrames
df_merged = pd.merge(df1, df2, on='Name')
df_merged = pd.merge(df_merged, df3, on='Name')

print(df_merged)


# Create a DataFrame
data = {'Name': ['John', 'John', 'Anna', 'Anna', 'Peter', 'Peter'],
        'Year': [2020, 2021, 2020, 2021, 2020, 2021],
        'Sales': [100, 200, 50, 75, 150, 225]}
df = pd.DataFrame(data)
print(df)
# Pivot the data
df_pivoted = pd.pivot_table(df, values='Sales', index='Name', columns='Year')

print(df_pivoted)

 #q4
 

f = open("info1.txt","w")
f.write("hello world")
f.close()
f = open("info1.txt", "a")
f.write(" thank you ")
f.close()
#open and read the file after write
f = open("info1.txt", "r")
print(f.read())
#Create a file called "myfile.txt":
#"x" - Create - will create a file, returns an error if the file exists
#f = open("info1.txt", "x")
#f.close()

#\n ---- \r\n 
#list of strings
list1=["thankyou welcome good day\n","hi\n","good night\n"]
f = open("info2.txt","w")
f.writelines(list1)
f.close()
f=open("info2.txt","r")
lines= f.readlines()
print('---',lines)
f.close()
#f = open("info6.txt", "r")
#print(f.read())
f=open("info2.txt","r")
for x in f:
  print(x)
f.close()

# read line ny line
f=open("info2.txt","r")
print("current position of file pointer ",f.tell())
line1=f.readline()
print("current position of file pointer ",f.tell())
line2=f.readline()
print("current position of file pointer ",f.tell())
line3=f.readline()
print("current position of file pointer ",f.tell())
'''print(line1)
print(line2)
print(line3)'''
f.close()
#to find current location of file pointer
f=open("info2.txt","r")
print('position of file pointer ',f.tell())  #0
str = f.read()
#print(str)
print('position of file pointer ',f.tell())
f.close()
# to move file pointer to specific position
f=open("info2.txt","r")
f.seek(6,0) # (offset-howmanybytestomove,fromwheretostart)
print("file data =",f.read())
f.close()

f = open("info.txt","w")
f.write("welcome to python coding")
f.close()
import os
print("current working directory= ",os.getcwd())
os.rename("info.txt","data.txt")
os.remove("data.txt")

with open("info2.txt", "rb") as file:
  print("First read:", file.read(5))
  file.seek(2, 1)  # Skip next 2 bytes
  print("After seek:", file.read(5))

  
 
 #5

 # csv file - comma seperated values
#CSVs are similar to spreadsheets but have a .csv extension
'''
CSV files are commonly used for data storage, transfer, and analysis
because they are easy to use, compatible with many programs,
and can handle large amounts of data.
 its purpose is to organize data into rows and columns
'''
# Data to write
data = [ ['Name', 'Age', 'City'], ['Rahul', 40, 'pune'],
         ['Eshan', 45, 'mumbai'], ['Pooja', 55, 'Delhi']  ]

import csv
# Writing to a CSV file
with open('people1.csv','w', newline='') as f:
    writer = csv.writer(f) #returns writer object
    writer.writerows(data)
   

print("Data written to people1.csv")

# Reading from a CSV file
with open('people1.csv','r') as file:
    reader = csv.reader(file) #returns file data
    for row in reader:
        print(row)

#-------------------------------
import csv

# Data to write as a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

import pandas as pd
#write to file using pandas
df=pd.DataFrame(data)
df.to_csv("student1.csv",index=False)


# Writing to a CSV file
with open('people_dict.csv','w', newline='') as file1:
    writer = csv.DictWriter(file1, fieldnames=data[0].keys())
    writer.writeheader()  # Write the header
    writer.writerows(data)  # Write the data

print("Data written to people_dict.csv")

import pandas as pd
# Reading CSV file
df = pd.read_csv("people_dict.csv")
print(df)

# Writing to CSV
df.to_csv("copy.csv", index=False)

# Reading from a CSV file
with open('people_dict.csv', mode='r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        print(row)


#6
# csv file - comma seperated values
#CSVs are similar to spreadsheets but have a .csv extension
'''
CSV files are commonly used for data storage, transfer, and analysis
because they are easy to use, compatible with many programs,
and can handle large amounts of data.
 its purpose is to organize data into rows and columns
'''
# Data to write
data = [ ['Name', 'Age', 'City'], ['Rahul', 40, 'pune'],
         ['Eshan', 45, 'mumbai'], ['Pooja', 55, 'Delhi']  ]

import csv
# Writing to a CSV file
with open('people1.csv','w', newline='') as f:
    writer = csv.writer(f) #returns writer object
    writer.writerows(data)
   

print("Data written to people1.csv")

# Reading from a CSV file
with open('people1.csv','r') as file:
    reader = csv.reader(file) #returns file data
    for row in reader:
        print(row)

#-------------------------------
import csv

# Data to write as a list of dictionaries
data = [
    {'Name': 'Alice', 'Age': 30, 'City': 'New York'},
    {'Name': 'Bob', 'Age': 25, 'City': 'Los Angeles'},
    {'Name': 'Charlie', 'Age': 35, 'City': 'Chicago'}
]

import pandas as pd
#write to file using pandas
df=pd.DataFrame(data)
df.to_csv("student1.csv",index=False)


# Writing to a CSV file
with open('people_dict.csv','w', newline='') as file1:
    writer = csv.DictWriter(file1, fieldnames=data[0].keys())
    writer.writeheader()  # Write the header
    writer.writerows(data)  # Write the data

print("Data written to people_dict.csv")

import pandas as pd
# Reading CSV file
df = pd.read_csv("people_dict.csv")
print(df)

# Writing to CSV
df.to_csv("copy.csv", index=False)

# Reading from a CSV file
with open('people_dict.csv', mode='r') as file1:
    reader = csv.DictReader(file1)
    for row in reader:
        print(row)



 #7
  
import json
'''
JSON (JavaScript Object Notation) is a popular data format 
used for representing structured data. It's common to transmit
 and receive data between a server and web application in JSON format.
JSON stands for JavaScript Object Notation and
is a lightweight format for storing and transporting data.
JSON is often used when data is sent from a server to a web page.
Python has the built-in module json , which allow us to work with JSON data.
'''
# Data to write
data = {
    'people': [
        {'Name': 'Teena', 'Age': 40, 'City': 'Pune'},
        {'Name': 'Omkar', 'Age': 30, 'City': 'Delhi'},
        {'Name': 'Chirag', 'Age': 55, 'City': 'Mumbai'}
    ]
}
# Writing to a JSON file
with open('people.json', 'w') as file:
    json.dump(data, file,indent=4)
print("Data written to people.json")
# Reading from a JSON file
with open('people.json', 'r') as file:
    data = json.load(file)    
    print(data)

# how to write and read json file using pandas
 
 
import xlsxwriter
# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Ajay', 30, 'New York'],
    ['Yash', 25, 'Los Angeles'],
    ['Jay', 35, 'Chicago'],
    ['John', 45, 'Mumbai']
]
# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('people.xlsx')
worksheet = workbook.add_worksheet()
# Write data to the worksheet
for index, row_data in enumerate(data):
    #print(index,row_data)
    worksheet.write_row(index, 0, row_data)

workbook.close() # Close the workbook
print("Data written to people.xlsx")

import pandas as pd
# Reading from an Excel file
df = pd.read_excel('people.xlsx')
#print(type(df))
# Display the DataFrame
print(df)
 
 #8
 import xlsxwriter

# Data to write
data = [
    ['Name', 'Age', 'City'],
    ['Ajay', 30, 'New York'],
    ['Yash', 25, 'Los Angeles'],
    ['Jay', 35, 'Chicago'],
    ['John', 45, 'Mumbai']
]

# Create a new Excel file and add a worksheet
workbook = xlsxwriter.Workbook('people.xlsx')
worksheet = workbook.add_worksheet()

# Write data to the worksheet
for index, row_data in enumerate(data):
    #print(index,row_data)
    worksheet.write_row(index, 0, row_data)


workbook.close() # Close the workbook
print("Data written to people.xlsx")


import pandas as pd
# Reading from an Excel file
df = pd.read_excel('people.xlsx')
#print(type(df))
# Display the DataFrame
print(df)
 

 #9
 sales_data2022.csv
Region,Product,Sales
North,Product A,1000
North,Product B,2000
South,Product A,1500
South,Product B,2500
 
 
sales_data2023.csv
Region,Product,Sales
North,Product A,1200
North,Product B,2200
South,Product A,1800
South,Product B,2800

#10
import pandas as pd

# Read CSV files
sales_data_2022 = pd.read_csv('sales_data2022.csv')
print(sales_data_2022)
sales_data_2023 = pd.read_csv('sales_data2023.csv')
print(sales_data_2023)

# Merge DataFrames
sales_data = pd.concat([sales_data_2022, sales_data_2023])
print(sales_data)

# Calculate total sales by region
total_sales_by_region = sales_data.groupby('Region')['Sales'].sum().reset_index()

# Calculate total sales by product
total_sales_by_product = sales_data.groupby('Product')['Sales'].sum().reset_index()

# Find top region
top_region = total_sales_by_region.loc[total_sales_by_region['Sales'].idxmax()]

# Find top product
top_product = total_sales_by_product.loc[total_sales_by_product['Sales'].idxmax()]

print("Total Sales by Region:")
print(total_sales_by_region)
print("\nTotal Sales by Product:")
print(total_sales_by_product)
print("\nTop Region:", top_region['Region'])
print("Top Product:", top_product['Product'])

#11
if __name__ == "__main__":
    print('hi')
 
 
'''
1. if __name__ == "__main__":
 
This line is checking if the script is being run directly (i.e., not being imported as a module in another script). Think of it like a gatekeeper that says: "Hey, are you running me directly, or are you being used by someone else?"
 
2. __name__
 
__name__ is a special variable in Python that holds the name of the script. When you run a script directly, __name__ is set to "__main__". But if you import this script as a module in another script, __name__ will be set to the name of the script (e.g., "test123").
 
3. print('hi')
 
If the condition if __name__ == "__main__": is true, then this line will be executed, and it simply prints the string "hi" to the console.
 
'''  