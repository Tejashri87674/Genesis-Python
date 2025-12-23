#reverse of number
def rev(n:int):
    revNum=0
    while n>0:
        digit=n%10
        revNum=revNum*10+digit
        n//=10
    print("reveresed number is ",revNum)

n=int(input("Enter number"))
rev(n)

#length of string
def lengthOfStr(string1:str):
    if isinstance(string1,str):
        return len(string1)
    else:
        return "incorrect output"
print(lengthOfStr("kpit"))

k=10
def magic():
    k=20
    print(k,globals()['k'])
magic()

def my_function(*args):
    print(args)
my_function(1,5,8)
my_function(1)
my_function("kpit",100,33.55,True)

'''
** keyword argument
'''
# def my_function(**kwargs):
#     print(kwargs)
# my_function(pname="jone",age=30)
# my_function(address="pune 411033",email="abc@gmail.com",contact=584511)

# #dictionary
# d1={1:[55,66,77],2:(5,8,9)}
# print(d1)
# print(d1[1])

# try:
#     print(d1[3])
# except:
#     print("invalid key")


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)
 
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter even elements
print(even_numbers)
 
#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)
 
# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles))
print(areas)






d1=  {1:89 , 2:99 ,5:78 , 3:55 , 2:78,6:90,6:75,6:11,8:100,9:100}
print(d1)
print(d1.values())
print(set(d1.values()))
print(tuple(d1.values()))

d2={101:"Neha",201:"Varun",301:"Yash"}
d2[301]="Priya"  # if key already present it will overwrite value
d2[401]="Anil"   #if key not present, it will be added newly
print(d2)

d3={"Neha":101,"Varun":201, "Yash":301,"yash":601}
print(d3)
d4={101:"Rahul" , "Tina":"Reena", 102:34.55, 103:[55,66,77]}
print(d4["Tina"])  # access value using key with [] operator
print(d4[103])  
try:
    print(d4[400])#if key not present - gives keyError
except KeyError as k:
    print('Invalid key ',k)
print(d4.get(400,"not found"))
print(d4.get("Tina"))
print("d4.get(222)  ",d4.get(222)) #if not not present- no error - output is None
print(d4)
print(d4.items()) 
print(d4.keys())  # get all keys
print(d4.values()) #get all values
# key- 101 --> whether 101 key is present in given dict
if 101 in d4:
    print('key found')
else:
    print('key not found')

if d4.get(222) is  None:
    print('key not found')
else:
    print('key found')
try:
    if d4[101]:
        print('key found')
except :
    print('key not found')
try:
    if d4[999]:
        print('key found')
except:
    print('key not found')
# value="amit" --->whether "amit" value is present in given dict
print("value found -","Rahul" in d4.values())
d4={101:"Rahul" , "Tina":"Reena", 102:34.55, 103:[55,66,77]}
flag=False
for key in d4:
    #if d4[key]=="Rahul":
    if d4[key]==[55,66,77]:
        flag=True
        break
print('value found' if flag else 'value not found')
#---------------
if any([True for k,v in d4.items()  if v=="Rahul"] ):
    print('** value Found ')
else:
    print('** value Not Found ')

d5={1:[100,200] , (44,55,66):222}
print(d5)
# key can be either number/string/tuple
print('**********************')
d5={1:110,2:200,3:500,5:400,7:900,6:877}
del d5[2]  # gives an error if key not found otherwise deletes record with given key
print(d5)
print('popped value', d5.pop(1))# gives an error if key not found otherwise deletes record with given key
print(d5)
d5.popitem()# remove/pop last item from dictionary
#d5.pop(3)
print(d5)
d6={1:100,2:200,3:300,4:None}
print(len(d6))
print(len(d6.keys()))
print(len(d6.values()))













import datetime
# Sample Vehicle Inventory (List of Dictionaries)
vehicles = [
    {"make": "Toyota", "model": "Camry", "year": 2022, "color": "Silver", "vin": "12345ABC", "price": 25000, "mileage": 15000, "category": "Sedan"},
    {"make": "Honda", "model": "Civic", "year": 2023, "color": "Blue", "vin": "67890DEF", "price": 23000, "mileage": 8000, "category": "Sedan"},
    {"make": "Ford", "model": "F-150", "year": 2021, "color": "Black", "vin": "13579GHI", "price": 35000, "mileage": 22000, "category": "Truck"},
    {"make": "Chevrolet", "model": "Equinox", "year": 2022, "color": "White", "vin": "24680JKL", "price": 27000, "mileage": 12000, "category": "SUV"},
    {"make": "Tesla", "model": "Model 3", "year": 2023, "color": "Red", "vin": "11223MNO", "price": 45000, "mileage": 5000, "category": "Electric"},
    {"make": "Toyota", "model": "Corolla", "year": 2020, "color": "Gray", "vin": "44556PQR", "price": 20000, "mileage": 30000, "category": "Sedan"},
    {"make": "Honda", "model": "CR-V", "year": 2023, "color": "Silver", "vin": "77889STU", "price": 30000, "mileage": 10000, "category": "SUV"},
    {"make": "Ford", "model": "Mustang", "year": 2021, "color": "Yellow", "vin": "99001VWX", "price": 40000, "mileage": 18000, "category": "Sports Car"},
    {"make": "Chevrolet", "model": "Tahoe", "year": 2022, "color": "Black", "vin": "22334YZ", "price": 50000, "mileage": 15000, "category": "SUV"},
    {"make": "Tesla", "model": "Model Y", "year": 2023, "color": "White", "vin": "55667ABC", "price": 55000, "mileage": 7000, "category": "Electric"}
]
# 1. Get all vehicles
def get_all_vehicles():
    return vehicles
# 2. Filter vehicles by make (using comprehension)
def filter_by_make(make):
    return [v for v in vehicles if v["make"] == make]
# 3. Filter vehicles by year (using comprehension)
def filter_by_year(year):
    return [v for v in vehicles if v["year"] == year]
# 4. Filter vehicles by price range (using comprehension)
def filter_by_price_range(min_price, max_price):
    return [v for v in vehicles if min_price <= v["price"] <= max_price]
# 5. Get vehicle details by VIN
def get_vehicle_by_vin(vin):
    return next((v for v in vehicles if v["vin"] == vin), None) #Returns None if not found
# 6. Calculate the average price of all vehicles
def average_price():
    return sum(v["price"] for v in vehicles) / len(vehicles)
# 7. Find the most expensive vehicle (using lambda and max)
def most_expensive_vehicle():
    return max(vehicles, key=lambda v: v["price"])
# 8. Find the cheapest vehicle (using lambda and min)
def cheapest_vehicle():
    return min(vehicles, key=lambda v: v["price"])
# 9. Sort vehicles by price (ascending) (using sorted and lambda)
def sort_by_price_asc():
    return sorted(vehicles, key=lambda v: v["price"])
# 10. Sort vehicles by mileage (descending) (using sorted and lambda)
def sort_by_mileage_desc():
    return sorted(vehicles, key=lambda v: v["mileage"], reverse=True)
# 11. Filter vehicles by category (using comprehension)
def filter_by_category(category):
    #return [v for v in vehicles if v["category"] == category]
    return list(filter(lambda x: x["category"]==category, vehicles))
print('***** filter o/p ****************-----------------------')
print(filter_by_category('Sedan'))
print('--------------------------------------------')
# 12. Get a list of all makes (using comprehension)
def get_all_makes():
    return list(set(v["make"] for v in vehicles))  #Use set to avoid duplicates
# 13.  Update vehicle price by VIN
def update_price_by_vin(vin, new_price):
    for v in vehicles:
        if v["vin"] == vin:
            v["price"] = new_price
            return True
    return False
# 14. Add a new vehicle to the inventory
def add_vehicle(vehicle_data):
    vehicles.append(vehicle_data)
'''
Why next is used here
One-shot search - We only need the first matching vehicle, not a list of all matches. 
next stops iterating as soon as it finds a match, making it more efficient than building an intermediate list.
Default handling - By providing None as the default, the code avoids a StopIteration exception when no vehicle matches the VIN. Instead, None is passed to remove.
What happens when the VIN is not found
next(..., None) returns None.
vehicles.remove(None) tries to delete None from the list.
Because None is not an element of vehicles, Python raises ValueError: list.remove(x): x not in list.
'''
# 15. Remove a vehicle by VIN
def remove_vehicle_by_vin(vin):
    return vehicles.remove(next((v for v in vehicles if v["vin"] == vin), None))
try:
    print('remove_vehicle_by_vin----------------->')
    print(remove_vehicle_by_vin("12345ABC"))
except ValueError:
    print('invalid vin ')
# 16. Count the number of vehicles of a specific make (using comprehension)
def count_vehicles_by_make(make):
    return sum(1 for v in vehicles if v["make"] == make)
# 17. Get vehicles with mileage less than a certain value (using comprehension)
def filter_by_mileage(max_mileage):
    return [v for v in vehicles if v["mileage"] < max_mileage]
# 18. Create a list of VINs for all vehicles (using comprehension)
def get_all_vins():
    return [v["vin"] for v in vehicles]
# 19. Calculate total inventory value (using comprehension)
def total_inventory_value():
    return sum(v["price"] for v in vehicles)
# 20. Filter vehicles manufactured after a certain year (using comprehension)
def filter_by_year_after(year):
    return [v for v in vehicles if v["year"] > year]
# 21.  Check if a vehicle with a given VIN exists (using lambda and any)
def vehicle_exists(vin):
    return any(v["vin"] == vin for v in vehicles)
# 22.  Get the average mileage of vehicles within a specific category
def average_mileage_by_category(category):
    category_vehicles = [v for v in vehicles if v["category"] == category]
    if category_vehicles:
        return sum(v["mileage"] for v in category_vehicles) / len(category_vehicles)
    return 0
# 23.  Find the newest vehicle (using lambda and max)
def newest_vehicle():
    return max(vehicles, key=lambda v: v["year"])
# 24.  Get a list of vehicle colors (using comprehension)
def get_all_colors():
    return list(set(v["color"] for v in vehicles))
# 25. Apply a discount to all vehicles of a specific make (using lambda and map)
def apply_discount_to_make(make, discount_percentage):
    return list(map(lambda v: {**v, "price": v["price"] * (1 - discount_percentage/100)} if v["make"] == make else v, vehicles))
# 26.  Get vehicles with a specific color and make (using comprehension)
def filter_by_color_and_make(color, make):
    return [v for v in vehicles if v["color"] == color and v["make"] == make]
# 27.  Convert vehicle data to a specific format (e.g., CSV-like string) using a lambda function
def format_vehicle_data(vehicle):
    return f"{vehicle['make']},{vehicle['model']},{vehicle['year']},{vehicle['price']}"
# 28. Get vehicles with mileage between a range and category
def filter_by_mileage_and_category(min_mileage, max_mileage, category):
    return [v for v in vehicles if min_mileage <= v["mileage"] <= max_mileage and v["category"] == category]
# 29. Check if any vehicles are older than a certain age
def has_old_vehicles(age):
    current_year = datetime.datetime.now().year
    return any(current_year - v["year"] > age for v in vehicles)
# 30. Get vehicles sorted by year and then by price
def sort_by_year_and_price():
    return sorted(vehicles, key=lambda v: (v["year"], v["price"]))

# Example Usage
print("All Vehicles:", get_all_vehicles())
print("\nToyota Vehicles:", filter_by_make("Toyota"))
print("\nVehicles between $25,000 and $40,000:", filter_by_price_range(25000, 40000))
print("\nMost Expensive Vehicle:", most_expensive_vehicle())
print("\nSorted by Price (Ascending):", sort_by_price_asc())
 


'''
Lambdas in Python are small, anonymous functions that can be defined inline within a larger expression. 
They are a shorthand way to create small functions without having to declare a full-fledged function with a name.

Syntax
lambda arguments: expression

Lambdas are often used in situations where a small, one-time-use function is needed, such as:

As an argument to a higher-order function (a function that takes another function as an argument)
As a return value from a function
As a way to create a small, inline function without cluttering up the code with a separate named function
Some common use cases for lambdas include:

Sorting lists of objects based on a specific attribute
Filtering lists of objects based on a specific condition
Mapping a function over a list of objects
'''

numbers = [14, 21, 35, 40, 50, 66]
# Define a lambda function that checks if a number is odd
is_odd = lambda x: x % 2 != 0
# Use the lambda function as an argument to the filter() function
odd_numbers = list(   filter(is_odd, numbers) )
print(odd_numbers)  # prints [1, 3, 5]

# We can also define the lambda function directly as an argument to the filter() function, like this:
numbers = [1, 2, 3, 4, 5, 6]
# Use a lambda function as an argument to the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # prints [1, 3, 5]

#Example:As an argument to a higher-order function
objects = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_objects = sorted(objects, key=lambda x: x['age'])
print(sorted_objects)  # prints [{'name': 'Bob', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]


#objects = [{'name': 'John', 'age': 25,'exp':40}, {'name': 'Jane', 'age': 30,'exp':2}, 
#{'name': 'Bob', 'age': 20,'exp':30}]



a=[1,2,3,5]
r= list(  map(lambda x:x**2,a)  )
print(r)


from functools import reduce
sumnumbers = lambda x, y: x + y
#print(sumnumbers(3, 4))
l1=[1,2,3,4,5,22,10,20,11]
#resultlist=reduce(sumnumbers,l1)
resultlist=reduce(lambda x,y:x+y , l1)
print("Sum of list elements =",resultlist)
#print('sum of numbers in list =',sum(l1))


v = lambda x, y: x - y
l1=[20,1,3,2]
result = reduce(v,l1)
print("result = ",result)


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter odd elements
print(even_numbers)

#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)

# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles)) 
print(areas) 

# from functools import reduce
numbers = [7, 2, 6, 1, 4]
product = reduce(lambda x, y: x * y, numbers) #multiply elements 
print(product)


fruits = ['apple', 'banana', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))#get elements which starts with a
print(a_fruits)

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
twenty_five_year_olds = list(filter(lambda x: x['age'] == 25, people))
print('twenty_five_year_olds', twenty_five_year_olds)


students = [
    {'name': 'John', 'age': 20},
    {'name': 'Ajay', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Anay', 'age': 31},
    {'name': 'John', 'age': 25}
]
students.sort(key=lambda x: x['age'])
print(students)

# fruits = {'apple': 5, 'banana': 10, 'cherry': 15}
# double_fruits = {k: lambda x: x*2 for k, x in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': <function <lambda> at 0x7f937f16c1f0>, 'banana': <function <lambda> at 0x7f937f16c280>, 'cherry': <function <lambda> at 0x7f937f16c310>}
# double_fruits = {k: v*2 for k, v in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': 10, 'banana': 20, 'cherry': 30}

from functools import reduce

# Sample dataset
vehicles = [
    {"id": 1, "fuel_efficiency": 25, "engine_power": 220, "transmission": "automatic"},
    {"id": 2, "fuel_efficiency": 30, "engine_power": 180, "transmission": "manual"},
    {"id": 3, "fuel_efficiency": 20, "engine_power": 250, "transmission": "automatic"},
    {"id": 4, "fuel_efficiency": 35, "engine_power": 200, "transmission": "manual"},
    {"id": 5, "fuel_efficiency": 28, "engine_power": 230, "transmission": "automatic"},
]

#Calculate the average fuel efficiency with automatic transmission:
automatic_vehicles = [x for x in vehicles if x["transmission"] == "automatic"]
print(automatic_vehicles)

fuel_efficiencies = [x["fuel_efficiency"] for x in automatic_vehicles]
print('eff',fuel_efficiencies)
total=0
for i in fuel_efficiencies:
       total+=i 
average_fuel_efficiency = total/len(fuel_efficiencies)
print("Average fuel efficiency of automatic vehicles:", average_fuel_efficiency)




#Remove vehicles with engine power less than 200 horsepower
filtered_vehicles = list(filter(lambda x: x["engine_power"] >= 200, vehicles))
print("Vehicles with engine power >= 200 horsepower:")
for vehicle in filtered_vehicles:
    print(vehicle)

#Map the transmission type to a numerical value (0 for automatic, 1 for manual)
transmission_map = {"automatic": 0, "manual": 1}
mapped_vehicles = list(map(lambda x: {**x, "transmission_code": transmission_map[x["transmission"]]}, vehicles))
print("Vehicles with transmission code:")
for vehicle in mapped_vehicles:
    print(vehicle)

# Reduce the dataset to only include vehicles with the highest fuel efficiency
max_fuel_efficiency = reduce(lambda x, y: x if x["fuel_efficiency"] > y["fuel_efficiency"] else y, vehicles)
print("Vehicle with the highest fuel efficiency:")
print(max_fuel_efficiency)


 




 '''
Lambdas in Python are small, anonymous functions that can be defined inline within a larger expression. 
They are a shorthand way to create small functions without having to declare a full-fledged function with a name.

Syntax
lambda arguments: expression

Lambdas are often used in situations where a small, one-time-use function is needed, such as:

As an argument to a higher-order function (a function that takes another function as an argument)
As a return value from a function
As a way to create a small, inline function without cluttering up the code with a separate named function
Some common use cases for lambdas include:

Sorting lists of objects based on a specific attribute
Filtering lists of objects based on a specific condition
Mapping a function over a list of objects
'''

numbers = [14, 21, 35, 40, 50, 66]
# Define a lambda function that checks if a number is odd
is_odd = lambda x: x % 2 != 0
# Use the lambda function as an argument to the filter() function
odd_numbers = list(   filter(is_odd, numbers) )
print(odd_numbers)  # prints [1, 3, 5]

# We can also define the lambda function directly as an argument to the filter() function, like this:
numbers = [1, 2, 3, 4, 5, 6]
# Use a lambda function as an argument to the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # prints [1, 3, 5]

#Example:As an argument to a higher-order function
objects = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_objects = sorted(objects, key=lambda x: x['age'])
print(sorted_objects)  # prints [{'name': 'Bob', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]


#objects = [{'name': 'John', 'age': 25,'exp':40}, {'name': 'Jane', 'age': 30,'exp':2}, 
#{'name': 'Bob', 'age': 20,'exp':30}]



a=[1,2,3,5]
r= list(  map(lambda x:x**2,a)  )
print(r)


from functools import reduce
sumnumbers = lambda x, y: x + y
#print(sumnumbers(3, 4))
l1=[1,2,3,4,5,22,10,20,11]
#resultlist=reduce(sumnumbers,l1)
resultlist=reduce(lambda x,y:x+y , l1)
print("Sum of list elements =",resultlist)
#print('sum of numbers in list =',sum(l1))


v = lambda x, y: x - y
l1=[20,1,3,2]
result = reduce(v,l1)
print("result = ",result)


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter odd elements
print(even_numbers)

#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)

# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles)) 
print(areas) 

# from functools import reduce
numbers = [7, 2, 6, 1, 4]
product = reduce(lambda x, y: x * y, numbers) #multiply elements 
print(product)


fruits = ['apple', 'banana', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))#get elements which starts with a
print(a_fruits)

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
twenty_five_year_olds = list(filter(lambda x: x['age'] == 25, people))
print('twenty_five_year_olds', twenty_five_year_olds)


students = [
    {'name': 'John', 'age': 20},
    {'name': 'Ajay', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Anay', 'age': 31},
    {'name': 'John', 'age': 25}
]
students.sort(key=lambda x: x['age'])
print(students)

# fruits = {'apple': 5, 'banana': 10, 'cherry': 15}
# double_fruits = {k: lambda x: x*2 for k, x in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': <function <lambda> at 0x7f937f16c1f0>, 'banana': <function <lambda> at 0x7f937f16c280>, 'cherry': <function <lambda> at 0x7f937f16c310>}
# double_fruits = {k: v*2 for k, v in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': 10, 'banana': 20, 'cherry': 30}

from functools import reduce

# Sample dataset
vehicles = [
    {"id": 1, "fuel_efficiency": 25, "engine_power": 220, "transmission": "automatic"},
    {"id": 2, "fuel_efficiency": 30, "engine_power": 180, "transmission": "manual"},
    {"id": 3, "fuel_efficiency": 20, "engine_power": 250, "transmission": "automatic"},
    {"id": 4, "fuel_efficiency": 35, "engine_power": 200, "transmission": "manual"},
    {"id": 5, "fuel_efficiency": 28, "engine_power": 230, "transmission": "automatic"},
]

#Calculate the average fuel efficiency with automatic transmission:
automatic_vehicles = [x for x in vehicles if x["transmission"] == "automatic"]
print(automatic_vehicles)

fuel_efficiencies = [x["fuel_efficiency"] for x in automatic_vehicles]
print('eff',fuel_efficiencies)
total=0
for i in fuel_efficiencies:
       total+=i 
average_fuel_efficiency = total/len(fuel_efficiencies)
print("Average fuel efficiency of automatic vehicles:", average_fuel_efficiency)




#Remove vehicles with engine power less than 200 horsepower
filtered_vehicles = list(filter(lambda x: x["engine_power"] >= 200, vehicles))
print("Vehicles with engine power >= 200 horsepower:")
for vehicle in filtered_vehicles:
    print(vehicle)

#Map the transmission type to a numerical value (0 for automatic, 1 for manual)
transmission_map = {"automatic": 0, "manual": 1}
mapped_vehicles = list(map(lambda x: {**x, "transmission_code": transmission_map[x["transmission"]]}, vehicles))
print("Vehicles with transmission code:")
for vehicle in mapped_vehicles:
    print(vehicle)

# Reduce the dataset to only include vehicles with the highest fuel efficiency
max_fuel_efficiency = reduce(lambda x, y: x if x["fuel_efficiency"] > y["fuel_efficiency"] else y, vehicles)
print("Vehicle with the highest fuel efficiency:")
print(max_fuel_efficiency)


 




  
'''
Lambdas in Python are small, anonymous functions that can be defined inline within a larger expression. 
They are a shorthand way to create small functions without having to declare a full-fledged function with a name.
Syntax
lambda arguments: expression
Lambdas are often used in situations where a small, one-time-use function is needed, such as:
As an argument to a higher-order function (a function that takes another function as an argument)
As a return value from a function
As a way to create a small, inline function without cluttering up the code with a separate named function
Some common use cases for lambdas include:
Sorting lists of objects based on a specific attribute
Filtering lists of objects based on a specific condition
Mapping a function over a list of objects
'''
numbers = [14, 21, 35, 40, 50, 66]
# Define a lambda function that checks if a number is odd
is_odd = lambda x: x % 2 != 0
# Use the lambda function as an argument to the filter() function
odd_numbers = list(   filter(is_odd, numbers) )
print(odd_numbers)  # prints [1, 3, 5]
# We can also define the lambda function directly as an argument to the filter() function, like this:
numbers = [1, 2, 3, 4, 5, 6]
# Use a lambda function as an argument to the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # prints [1, 3, 5]
#Example:As an argument to a higher-order function
objects = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_objects = sorted(objects, key=lambda x: x['age'])
print(sorted_objects)  # prints [{'name': 'Bob', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]

#objects = [{'name': 'John', 'age': 25,'exp':40}, {'name': 'Jane', 'age': 30,'exp':2}, 
#{'name': 'Bob', 'age': 20,'exp':30}]

a=[1,2,3,5]
r= list(  map(lambda x:x**2,a)  )
print(r)

from functools import reduce
sumnumbers = lambda x, y: x + y
#print(sumnumbers(3, 4))
l1=[1,2,3,4,5,22,10,20,11]
#resultlist=reduce(sumnumbers,l1)
resultlist=reduce(lambda x,y:x+y , l1)
print("Sum of list elements =",resultlist)
#print('sum of numbers in list =',sum(l1))

v = lambda x, y: x - y
l1=[20,1,3,2]
result = reduce(v,l1)
print("result = ",result)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter odd elements
print(even_numbers)
#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)
# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles)) 
print(areas) 
# from functools import reduce
numbers = [7, 2, 6, 1, 4]
product = reduce(lambda x, y: x * y, numbers) #multiply elements 
print(product)

fruits = ['apple', 'banana', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))#get elements which starts with a
print(a_fruits)
people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
twenty_five_year_olds = list(filter(lambda x: x['age'] == 25, people))
print('twenty_five_year_olds', twenty_five_year_olds)

students = [
    {'name': 'John', 'age': 20},
    {'name': 'Ajay', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Anay', 'age': 31},
    {'name': 'John', 'age': 25}
]
students.sort(key=lambda x: x['age'])
print(students)
# fruits = {'apple': 5, 'banana': 10, 'cherry': 15}
# double_fruits = {k: lambda x: x*2 for k, x in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': <function <lambda> at 0x7f937f16c1f0>, 'banana': <function <lambda> at 0x7f937f16c280>, 'cherry': <function <lambda> at 0x7f937f16c310>}
# double_fruits = {k: v*2 for k, v in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': 10, 'banana': 20, 'cherry': 30}
from functools import reduce
# Sample dataset
vehicles = [
    {"id": 1, "fuel_efficiency": 25, "engine_power": 220, "transmission": "automatic"},
    {"id": 2, "fuel_efficiency": 30, "engine_power": 180, "transmission": "manual"},
    {"id": 3, "fuel_efficiency": 20, "engine_power": 250, "transmission": "automatic"},
    {"id": 4, "fuel_efficiency": 35, "engine_power": 200, "transmission": "manual"},
    {"id": 5, "fuel_efficiency": 28, "engine_power": 230, "transmission": "automatic"},
]
#Calculate the average fuel efficiency with automatic transmission:
automatic_vehicles = [x for x in vehicles if x["transmission"] == "automatic"]
print(automatic_vehicles)
fuel_efficiencies = [x["fuel_efficiency"] for x in automatic_vehicles]
print('eff',fuel_efficiencies)
total=0
for i in fuel_efficiencies:
       total+=i 
average_fuel_efficiency = total/len(fuel_efficiencies)
print("Average fuel efficiency of automatic vehicles:", average_fuel_efficiency)


#Remove vehicles with engine power less than 200 horsepower
filtered_vehicles = list(filter(lambda x: x["engine_power"] >= 200, vehicles))
print("Vehicles with engine power >= 200 horsepower:")
for vehicle in filtered_vehicles:
    print(vehicle)
#Map the transmission type to a numerical value (0 for automatic, 1 for manual)
transmission_map = {"automatic": 0, "manual": 1}
mapped_vehicles = list(map(lambda x: {**x, "transmission_code": transmission_map[x["transmission"]]}, vehicles))
print("Vehicles with transmission code:")
for vehicle in mapped_vehicles:
    print(vehicle)
# Reduce the dataset to only include vehicles with the highest fuel efficiency
max_fuel_efficiency = reduce(lambda x, y: x if x["fuel_efficiency"] > y["fuel_efficiency"] else y, vehicles)
print("Vehicle with the highest fuel efficiency:")
print(max_fuel_efficiency)

 


 
 
 
 
# Initialize an empty dictionary to store battery cells
battery_cells = {}
def add_battery_cell(cell_id, vt, cp, tp):
    """
    Add a new battery cell to the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float): Voltage of the battery cell.
        capacity (float): Capacity of the battery cell.
        temperature (float): Temperature of the battery cell.
    """
    # Create a new dictionary with battery cell information
    cell = {
        "voltage": vt,
        "capacity": cp,
        "temperature": tp
    }
    # Add the battery cell to the dictionary
    battery_cells[cell_id] = cell
    print(f"Battery cell with ID {cell_id} added successfully")
def remove_battery_cell(cell_id):
    """
    Remove a battery cell from the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Remove the battery cell from the dictionary
        del battery_cells[cell_id]
        print(f"Battery cell with ID {cell_id} removed successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")
def update_battery_cell(cell_id, voltage=None, capacity=None, temperature=None):
    """
    Update a battery cell's information in the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float, optional): Voltage of the battery cell. Defaults to None.
        capacity (float, optional): Capacity of the battery cell. Defaults to None.
        temperature (float, optional): Temperature of the battery cell. Defaults to None.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Update the battery cell information
        if voltage:
            battery_cells[cell_id]["voltage"] = voltage
        if capacity:
            battery_cells[cell_id]["capacity"] = capacity
        if temperature:
            battery_cells[cell_id]["temperature"] = temperature
        print(f"Battery cell with ID {cell_id} updated successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")
def display_battery_cells():
    """
    Display all battery cells in the dictionary.
    """
    # Check if the dictionary is empty
    if not battery_cells:
        print("No battery cells in the database")
    else:
        # Print each battery cell in the dictionary
        for cell_id, cell in battery_cells.items():
            print(f"Battery Cell ID: {cell_id}")
            print(f"Voltage: {cell['voltage']}")
            print(f"Capacity: {cell['capacity']}")
            print(f"Temperature: {cell['temperature']}")
            print("------------------------")
def search_battery_cell(cell_id):
    """
    Search for a battery cell by ID.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Print the battery cell information
        cell = battery_cells[cell_id]
        print(f"Battery Cell ID: {cell_id}")
        print(f"Voltage: {cell['voltage']}")
        print(f"Capacity: {cell['capacity']}")
        print(f"Temperature: {cell['temperature']}")
    else:
        print(f"Battery cell with ID {cell_id} not found")
def calculate_total_capacity():
    """
    Calculate the total capacity of all battery cells.
    """
  
# Test the functions
add_battery_cell("C1", 3.7, 2000, 25)
add_battery_cell("C2", 3.8, 2500, 30)
add_battery_cell("C3", 3.9, 3000, 35)
print(battery_cells)
display_battery_cells()
search_battery_cell("C1")
calculate_total_capacity()
{"c1":{3.7,2000,25} , }
 
 







 
'''
Lambdas in Python are small, anonymous functions that can be defined inline within a larger expression. 
They are a shorthand way to create small functions without having to declare a full-fledged function with a name.
Syntax
lambda arguments: expression
Lambdas are often used in situations where a small, one-time-use function is needed, such as:
As an argument to a higher-order function (a function that takes another function as an argument)
As a return value from a function
As a way to create a small, inline function without cluttering up the code with a separate named function
Some common use cases for lambdas include:
Sorting lists of objects based on a specific attribute
Filtering lists of objects based on a specific condition
Mapping a function over a list of objects
'''
numbers = [14, 21, 35, 40, 50, 66]
# Define a lambda function that checks if a number is odd
is_odd = lambda x: x % 2 != 0
# Use the lambda function as an argument to the filter() function
odd_numbers = list(   filter(is_odd, numbers) )
print(odd_numbers)  # prints [1, 3, 5]
# We can also define the lambda function directly as an argument to the filter() function, like this:
numbers = [1, 2, 3, 4, 5, 6]
# Use a lambda function as an argument to the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # prints [1, 3, 5]
#Example:As an argument to a higher-order function
objects = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_objects = sorted(objects, key=lambda x: x['age'])
print(sorted_objects)  # prints [{'name': 'Bob', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]

#objects = [{'name': 'John', 'age': 25,'exp':40}, {'name': 'Jane', 'age': 30,'exp':2}, 
#{'name': 'Bob', 'age': 20,'exp':30}]

a=[1,2,3,5]
r= list(  map(lambda x:x**2,a)  )
print(r)

from functools import reduce
sumnumbers = lambda x, y: x + y
#print(sumnumbers(3, 4))
l1=[1,2,3,4,5,22,10,20,11]
#resultlist=reduce(sumnumbers,l1)
resultlist=reduce(lambda x,y:x+y , l1)
print("Sum of list elements =",resultlist)
#print('sum of numbers in list =',sum(l1))

v = lambda x, y: x - y
l1=[20,1,3,2]
result = reduce(v,l1)
print("result = ",result)

numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter odd elements
print(even_numbers)
#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)
# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles)) 
print(areas) 
# from functools import reduce
numbers = [7, 2, 6, 1, 4]
product = reduce(lambda x, y: x * y, numbers) #multiply elements 
print(product)

fruits = ['apple', 'banana', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))#get elements which starts with a
print(a_fruits)
people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
twenty_five_year_olds = list(filter(lambda x: x['age'] == 25, people))
print('twenty_five_year_olds', twenty_five_year_olds)

students = [
    {'name': 'John', 'age': 20},
    {'name': 'Ajay', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Anay', 'age': 31},
    {'name': 'John', 'age': 25}
]
students.sort(key=lambda x: x['age'])
print(students)
# fruits = {'apple': 5, 'banana': 10, 'cherry': 15}
# double_fruits = {k: lambda x: x*2 for k, x in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': <function <lambda> at 0x7f937f16c1f0>, 'banana': <function <lambda> at 0x7f937f16c280>, 'cherry': <function <lambda> at 0x7f937f16c310>}
# double_fruits = {k: v*2 for k, v in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': 10, 'banana': 20, 'cherry': 30}
from functools import reduce
# Sample dataset
vehicles = [
    {"id": 1, "fuel_efficiency": 25, "engine_power": 220, "transmission": "automatic"},
    {"id": 2, "fuel_efficiency": 30, "engine_power": 180, "transmission": "manual"},
    {"id": 3, "fuel_efficiency": 20, "engine_power": 250, "transmission": "automatic"},
    {"id": 4, "fuel_efficiency": 35, "engine_power": 200, "transmission": "manual"},
    {"id": 5, "fuel_efficiency": 28, "engine_power": 230, "transmission": "automatic"},
]
#Calculate the average fuel efficiency with automatic transmission:
automatic_vehicles = [x for x in vehicles if x["transmission"] == "automatic"]
print(automatic_vehicles)
fuel_efficiencies = [x["fuel_efficiency"] for x in automatic_vehicles]
print('eff',fuel_efficiencies)
total=0
for i in fuel_efficiencies:
       total+=i 
average_fuel_efficiency = total/len(fuel_efficiencies)
print("Average fuel efficiency of automatic vehicles:", average_fuel_efficiency)


#Remove vehicles with engine power less than 200 horsepower
filtered_vehicles = list(filter(lambda x: x["engine_power"] >= 200, vehicles))
print("Vehicles with engine power >= 200 horsepower:")
for vehicle in filtered_vehicles:
    print(vehicle)
#Map the transmission type to a numerical value (0 for automatic, 1 for manual)
transmission_map = {"automatic": 0, "manual": 1}
mapped_vehicles = list(map(lambda x: {**x, "transmission_code": transmission_map[x["transmission"]]}, vehicles))
print("Vehicles with transmission code:")
for vehicle in mapped_vehicles:
    print(vehicle)
# Reduce the dataset to only include vehicles with the highest fuel efficiency
max_fuel_efficiency = reduce(lambda x, y: x if x["fuel_efficiency"] > y["fuel_efficiency"] else y, vehicles)
print("Vehicle with the highest fuel efficiency:")
print(max_fuel_efficiency)

 


 
 
 
 
# Initialize an empty dictionary to store battery cells
battery_cells = {}
def add_battery_cell(cell_id, vt, cp, tp):
    """
    Add a new battery cell to the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float): Voltage of the battery cell.
        capacity (float): Capacity of the battery cell.
        temperature (float): Temperature of the battery cell.
    """
    # Create a new dictionary with battery cell information
    cell = {
        "voltage": vt,
        "capacity": cp,
        "temperature": tp
    }
    # Add the battery cell to the dictionary
    battery_cells[cell_id] = cell
    print(f"Battery cell with ID {cell_id} added successfully")
def remove_battery_cell(cell_id):
    """
    Remove a battery cell from the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Remove the battery cell from the dictionary
        del battery_cells[cell_id]
        print(f"Battery cell with ID {cell_id} removed successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")
def update_battery_cell(cell_id, voltage=None, capacity=None, temperature=None):
    """
    Update a battery cell's information in the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float, optional): Voltage of the battery cell. Defaults to None.
        capacity (float, optional): Capacity of the battery cell. Defaults to None.
        temperature (float, optional): Temperature of the battery cell. Defaults to None.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Update the battery cell information
        if voltage:
            battery_cells[cell_id]["voltage"] = voltage
        if capacity:
            battery_cells[cell_id]["capacity"] = capacity
        if temperature:
            battery_cells[cell_id]["temperature"] = temperature
        print(f"Battery cell with ID {cell_id} updated successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")
def display_battery_cells():
    """
    Display all battery cells in the dictionary.
    """
    # Check if the dictionary is empty
    if not battery_cells:
        print("No battery cells in the database")
    else:
        # Print each battery cell in the dictionary
        for cell_id, cell in battery_cells.items():
            print(f"Battery Cell ID: {cell_id}")
            print(f"Voltage: {cell['voltage']}")
            print(f"Capacity: {cell['capacity']}")
            print(f"Temperature: {cell['temperature']}")
            print("------------------------")
def search_battery_cell(cell_id):
    """
    Search for a battery cell by ID.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Print the battery cell information
        cell = battery_cells[cell_id]
        print(f"Battery Cell ID: {cell_id}")
        print(f"Voltage: {cell['voltage']}")
        print(f"Capacity: {cell['capacity']}")
        print(f"Temperature: {cell['temperature']}")
    else:
        print(f"Battery cell with ID {cell_id} not found")
def calculate_total_capacity():
    """
    Calculate the total capacity of all battery cells.
    """
  
# Test the functions
add_battery_cell("C1", 3.7, 2000, 25)
add_battery_cell("C2", 3.8, 2500, 30)
add_battery_cell("C3", 3.9, 3000, 35)
print(battery_cells)
display_battery_cells()
search_battery_cell("C1")
calculate_total_capacity()
{"c1":{3.7,2000,25} , }
 
 















 # Initialize an empty dictionary to store battery cells
battery_cells = {}

def add_battery_cell(cell_id, vt, cp, tp):
    """
    Add a new battery cell to the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float): Voltage of the battery cell.
        capacity (float): Capacity of the battery cell.
        temperature (float): Temperature of the battery cell.
    """
    # Create a new dictionary with battery cell information
    cell = {
        "voltage": vt,
        "capacity": cp,
        "temperature": tp
    }
    # Add the battery cell to the dictionary
    battery_cells[cell_id] = cell
    print(f"Battery cell with ID {cell_id} added successfully")

def remove_battery_cell(cell_id):
    """
    Remove a battery cell from the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Remove the battery cell from the dictionary
        del battery_cells[cell_id]
        print(f"Battery cell with ID {cell_id} removed successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def update_battery_cell(cell_id, voltage=None, capacity=None, temperature=None):
    """
    Update a battery cell's information in the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float, optional): Voltage of the battery cell. Defaults to None.
        capacity (float, optional): Capacity of the battery cell. Defaults to None.
        temperature (float, optional): Temperature of the battery cell. Defaults to None.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Update the battery cell information
        if voltage:
            battery_cells[cell_id]["voltage"] = voltage
        if capacity:
            battery_cells[cell_id]["capacity"] = capacity
        if temperature:
            battery_cells[cell_id]["temperature"] = temperature
        print(f"Battery cell with ID {cell_id} updated successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def display_battery_cells():
    """
    Display all battery cells in the dictionary.
    """
    # Check if the dictionary is empty
    if not battery_cells:
        print("No battery cells in the database")
    else:
        # Print each battery cell in the dictionary
        for cell_id, cell in battery_cells.items():
            print(f"Battery Cell ID: {cell_id}")
            print(f"Voltage: {cell['voltage']}")
            print(f"Capacity: {cell['capacity']}")
            print(f"Temperature: {cell['temperature']}")
            print("------------------------")

def search_battery_cell(cell_id):
    """
    Search for a battery cell by ID.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Print the battery cell information
        cell = battery_cells[cell_id]
        print(f"Battery Cell ID: {cell_id}")
        print(f"Voltage: {cell['voltage']}")
        print(f"Capacity: {cell['capacity']}")
        print(f"Temperature: {cell['temperature']}")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def calculate_total_capacity():
    """
    Calculate the total capacity of all battery cells.
    """
  

# Test the functions
add_battery_cell("C1", 3.7, 2000, 25)
add_battery_cell("C2", 3.8, 2500, 30)
add_battery_cell("C3", 3.9, 3000, 35)
print(battery_cells)
display_battery_cells()
search_battery_cell("C1")
calculate_total_capacity()

{"c1":{3.7,2000,25} , }
 















'''
Lambdas in Python are small, anonymous functions that can be defined inline within a larger expression. 
They are a shorthand way to create small functions without having to declare a full-fledged function with a name.

Syntax
lambda arguments: expression

Lambdas are often used in situations where a small, one-time-use function is needed, such as:

As an argument to a higher-order function (a function that takes another function as an argument)
As a return value from a function
As a way to create a small, inline function without cluttering up the code with a separate named function
Some common use cases for lambdas include:

Sorting lists of objects based on a specific attribute
Filtering lists of objects based on a specific condition
Mapping a function over a list of objects
'''

numbers = [14, 21, 35, 40, 50, 66]
# Define a lambda function that checks if a number is odd
is_odd = lambda x: x % 2 != 0
# Use the lambda function as an argument to the filter() function
odd_numbers = list(   filter(is_odd, numbers) )
print(odd_numbers)  # prints [1, 3, 5]

# We can also define the lambda function directly as an argument to the filter() function, like this:
numbers = [1, 2, 3, 4, 5, 6]
# Use a lambda function as an argument to the filter() function
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print(odd_numbers)  # prints [1, 3, 5]

#Example:As an argument to a higher-order function
objects = [{'name': 'John', 'age': 25}, {'name': 'Jane', 'age': 30}, {'name': 'Bob', 'age': 20}]
sorted_objects = sorted(objects, key=lambda x: x['age'])
print(sorted_objects)  # prints [{'name': 'Bob', 'age': 20}, {'name': 'Jane', 'age': 30}, {'name': 'John', 'age': 25}]


#objects = [{'name': 'John', 'age': 25,'exp':40}, {'name': 'Jane', 'age': 30,'exp':2}, 
#{'name': 'Bob', 'age': 20,'exp':30}]



a=[1,2,3,5]
r= list(  map(lambda x:x**2,a)  )
print(r)


from functools import reduce
sumnumbers = lambda x, y: x + y
#print(sumnumbers(3, 4))
l1=[1,2,3,4,5,22,10,20,11]
#resultlist=reduce(sumnumbers,l1)
resultlist=reduce(lambda x,y:x+y , l1)
print("Sum of list elements =",resultlist)
#print('sum of numbers in list =',sum(l1))


v = lambda x, y: x - y
l1=[20,1,3,2]
result = reduce(v,l1)
print("result = ",result)


numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x**2, numbers))#make square of each element
print(squared_numbers)

numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) #filter odd elements
print(even_numbers)

#Convert each string to uppercase
fruits = ['apple', 'banana', 'cherry']
uppercase_fruits = list(map(lambda x: x.upper(), fruits))#convert to upper case
print(uppercase_fruits)

# # Calculate the area of each rectangle
rectangles = [(2, 3), (4, 5), (6, 7)]
areas = list(map(lambda x: x[0] * x[1], rectangles)) 
print(areas) 

# from functools import reduce
numbers = [7, 2, 6, 1, 4]
product = reduce(lambda x, y: x * y, numbers) #multiply elements 
print(product)


fruits = ['apple', 'banana', 'cherry', 'apricot']
a_fruits = list(filter(lambda x: x.startswith('a'), fruits))#get elements which starts with a
print(a_fruits)

people = [
    {'name': 'John', 'age': 25},
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25}
]
twenty_five_year_olds = list(filter(lambda x: x['age'] == 25, people))
print('twenty_five_year_olds', twenty_five_year_olds)


students = [
    {'name': 'John', 'age': 20},
    {'name': 'Ajay', 'age': 22},
    {'name': 'Bob', 'age': 19},
    {'name': 'Anay', 'age': 31},
    {'name': 'John', 'age': 25}
]
students.sort(key=lambda x: x['age'])
print(students)

# fruits = {'apple': 5, 'banana': 10, 'cherry': 15}
# double_fruits = {k: lambda x: x*2 for k, x in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': <function <lambda> at 0x7f937f16c1f0>, 'banana': <function <lambda> at 0x7f937f16c280>, 'cherry': <function <lambda> at 0x7f937f16c310>}
# double_fruits = {k: v*2 for k, v in fruits.items()}
# print(double_fruits)  
# # Outputs: {'apple': 10, 'banana': 20, 'cherry': 30}

from functools import reduce

# Sample dataset
vehicles = [
    {"id": 1, "fuel_efficiency": 25, "engine_power": 220, "transmission": "automatic"},
    {"id": 2, "fuel_efficiency": 30, "engine_power": 180, "transmission": "manual"},
    {"id": 3, "fuel_efficiency": 20, "engine_power": 250, "transmission": "automatic"},
    {"id": 4, "fuel_efficiency": 35, "engine_power": 200, "transmission": "manual"},
    {"id": 5, "fuel_efficiency": 28, "engine_power": 230, "transmission": "automatic"},
]

#Calculate the average fuel efficiency with automatic transmission:
automatic_vehicles = [x for x in vehicles if x["transmission"] == "automatic"]
print(automatic_vehicles)

fuel_efficiencies = [x["fuel_efficiency"] for x in automatic_vehicles]
print('eff',fuel_efficiencies)
total=0
for i in fuel_efficiencies:
       total+=i 
average_fuel_efficiency = total/len(fuel_efficiencies)
print("Average fuel efficiency of automatic vehicles:", average_fuel_efficiency)




#Remove vehicles with engine power less than 200 horsepower
filtered_vehicles = list(filter(lambda x: x["engine_power"] >= 200, vehicles))
print("Vehicles with engine power >= 200 horsepower:")
for vehicle in filtered_vehicles:
    print(vehicle)

#Map the transmission type to a numerical value (0 for automatic, 1 for manual)
transmission_map = {"automatic": 0, "manual": 1}
mapped_vehicles = list(map(lambda x: {**x, "transmission_code": transmission_map[x["transmission"]]}, vehicles))
print("Vehicles with transmission code:")
for vehicle in mapped_vehicles:
    print(vehicle)

# Reduce the dataset to only include vehicles with the highest fuel efficiency
max_fuel_efficiency = reduce(lambda x, y: x if x["fuel_efficiency"] > y["fuel_efficiency"] else y, vehicles)
print("Vehicle with the highest fuel efficiency:")
print(max_fuel_efficiency)













# Initialize an empty dictionary to store battery cells
battery_cells = {}

def add_battery_cell(cell_id, vt, cp, tp):
    """
    Add a new battery cell to the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float): Voltage of the battery cell.
        capacity (float): Capacity of the battery cell.
        temperature (float): Temperature of the battery cell.
    """
    # Create a new dictionary with battery cell information
    cell = {
        "voltage": vt,
        "capacity": cp,
        "temperature": tp
    }
    # Add the battery cell to the dictionary
    battery_cells[cell_id] = cell
    print(f"Battery cell with ID {cell_id} added successfully")

def remove_battery_cell(cell_id):
    """
    Remove a battery cell from the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Remove the battery cell from the dictionary
        del battery_cells[cell_id]
        print(f"Battery cell with ID {cell_id} removed successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def update_battery_cell(cell_id, voltage=None, capacity=None, temperature=None):
    """
    Update a battery cell's information in the dictionary.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
        voltage (float, optional): Voltage of the battery cell. Defaults to None.
        capacity (float, optional): Capacity of the battery cell. Defaults to None.
        temperature (float, optional): Temperature of the battery cell. Defaults to None.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Update the battery cell information
        if voltage:
            battery_cells[cell_id]["voltage"] = voltage
        if capacity:
            battery_cells[cell_id]["capacity"] = capacity
        if temperature:
            battery_cells[cell_id]["temperature"] = temperature
        print(f"Battery cell with ID {cell_id} updated successfully")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def display_battery_cells():
    """
    Display all battery cells in the dictionary.
    """
    # Check if the dictionary is empty
    if not battery_cells:
        print("No battery cells in the database")
    else:
        # Print each battery cell in the dictionary
        for cell_id, cell in battery_cells.items():
            print(f"Battery Cell ID: {cell_id}")
            print(f"Voltage: {cell['voltage']}")
            print(f"Capacity: {cell['capacity']}")
            print(f"Temperature: {cell['temperature']}")
            print("------------------------")

def search_battery_cell(cell_id):
    """
    Search for a battery cell by ID.
    
    Args:
        cell_id (str): Unique ID for the battery cell.
    """
    # Check if the battery cell exists in the dictionary
    if cell_id in battery_cells:
        # Print the battery cell information
        cell = battery_cells[cell_id]
        print(f"Battery Cell ID: {cell_id}")
        print(f"Voltage: {cell['voltage']}")
        print(f"Capacity: {cell['capacity']}")
        print(f"Temperature: {cell['temperature']}")
    else:
        print(f"Battery cell with ID {cell_id} not found")

def calculate_total_capacity():
    """
    Calculate the total capacity of all battery cells.
    """
  

# Test the functions
add_battery_cell("C1", 3.7, 2000, 25)
add_battery_cell("C2", 3.8, 2500, 30)
add_battery_cell("C3", 3.9, 3000, 35)
print(battery_cells)
display_battery_cells()
search_battery_cell("C1")
calculate_total_capacity()

{"c1":{3.7,2000,25} , }
 