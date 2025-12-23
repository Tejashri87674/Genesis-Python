class Product:
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
    def __repr__(self):
        return f"Product name: {self.name}, price: {self.price},quantity: {self.quantity}"
    
class Inventory:
    def __init__(self):
        self.productlist=[]
    def addproduct(self,productobject):
        self.productlist.append(productobject)
    def showInventory(self):
        for p in self.productlist:
            print(p)
    def searchProduct(self,pname):
        flag=False
        for p in self.productlist:
            if p.name==pname:
                flag=True
                break
        if flag:
            print("prodcut found")
        else:
            print("product not found")

p1=Product("Laptop",70000,200)
print(p1)

p2=Product("Mobile",75000,300)
p3=Product("Bag",2000,400)




class Vehicle:
    """Represents a vehicle in the fleet."""

    def __init__(self, vehicle_id, vehicle_type, fuel_capacity, maintenance_cost, last_service_days, delivery_rating):
        self.vehicle_id = vehicle_id
        self.vehicle_type = vehicle_type  # e.g., "Van", "Truck"
        self.fuel_capacity = fuel_capacity  # Liters
        self.maintenance_cost = maintenance_cost  # Last maintenance cost
        self.last_service_days = last_service_days  # Days since last service
        self.delivery_rating = delivery_rating # Rating between 1-5

    def __repr__(self):
        return (f"Vehicle ID: {self.vehicle_id}, Type: {self.vehicle_type}, Fuel: {self.fuel_capacity}, "
                f"Maintenance: {self.maintenance_cost}, Service Days: {self.last_service_days}, Rating: {self.delivery_rating}")


class VehicleFleetManager:
    """Manages a fleet of vehicles."""

    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        """Adds a vehicle to the fleet."""
        self.vehicles.append(vehicle)
        print(f"Vehicle {vehicle.vehicle_id} added to the fleet.")

    def remove_vehicle(self, vehicle_id):
        """Removes a vehicle from the fleet by ID."""
        self.vehicles = [v for v in self.vehicles if v.vehicle_id != vehicle_id]
        print(f"Vehicle {vehicle_id} removed from the fleet.")

    def get_vehicle(self, vehicle_id):
        """Retrieves a vehicle by its ID."""
        for vehicle in self.vehicles:
            if vehicle.vehicle_id == vehicle_id:
                return vehicle
        return None

    def get_vehicles_by_type(self, vehicle_type):
       """Returns a list of vehicles of a specific type."""
       return [vehicle for vehicle in self.vehicles if vehicle.vehicle_type == vehicle_type]

    def calculate_statistic(self, operation):
        """Calculates a statistic (avg, sum, min, max) for maintenance_cost."""
        if not self.vehicles:
            return None  # Handle empty fleet case

        values = [vehicle.maintenance_cost for vehicle in self.vehicles]

        if operation == "avg":
            return sum(values) / len(values)
        elif operation == "sum":
            return sum(values)
        elif operation == "min":
            return min(values)
        elif operation == "max":
            return max(values)
        else:
            return None # Invalid operation

    def filter_greater_than(self, threshold):
        """Filters vehicles where maintenance_cost is greater than the threshold."""
        return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost > threshold]

    def filter_less_than(self, threshold):
        """Filters vehicles where maintenance_cost is less than the threshold."""
        return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost < threshold]

    def filter_equal_to(self, threshold):
        """Filters vehicles where maintenance_cost is equal to the threshold."""
        return [vehicle for vehicle in self.vehicles if vehicle.maintenance_cost == threshold]


    def sort_vehicles(self, reverse=False):
        """Sorts vehicles based on maintenance_cost."""
        return sorted(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost, reverse=reverse)

    def find_min_vehicle(self):
        """Finds the vehicle with the minimum maintenance_cost."""
        if not self.vehicles:
            return None
        return min(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost)

    def find_max_vehicle(self):
        """Finds the vehicle with the maximum maintenance_cost."""
        if not self.vehicles:
            return None
        return max(self.vehicles, key=lambda vehicle: vehicle.maintenance_cost)

# Example Usage:
fleet_manager = VehicleFleetManager()
v1 = Vehicle("V101", "Van", 60, 500, 30, 4)
v2 = Vehicle("V102", "Van", 70, 600, 15, 5)
v3 = Vehicle("T201", "Truck", 200, 2000, 60, 3)
fleet_manager.add_vehicle(v1)
fleet_manager.add_vehicle(v2)
fleet_manager.add_vehicle(v3)

print(f"Average Maintenance Cost: {fleet_manager.calculate_statistic('avg')}")
print(f"Sum of Maintenance Costs: {fleet_manager.calculate_statistic('sum')}")
print(f"Minimum Maintenance Cost: {fleet_manager.calculate_statistic('min')}")
print(f"Maximum Maintenance Cost: {fleet_manager.calculate_statistic('max')}")

high_maintenance_vehicles = fleet_manager.filter_greater_than(700)
print(f"Vehicles with Maintenance Cost > 700: {high_maintenance_vehicles}")

sorted_by_maintenance = fleet_manager.sort_vehicles()
print(f"Sorted by Maintenance Cost: {sorted_by_maintenance}")

min_maintenance_vehicle = fleet_manager.find_min_vehicle()
print(f"Vehicle with Minimum Maintenance Cost: {min_maintenance_vehicle}")

max_maintenance_vehicle = fleet_manager.find_max_vehicle()
print(f"Vehicle with Maximum Maintenance Cost: {max_maintenance_vehicle}")

 #setter demo
  
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age
    @property
    def name(self): #getter method- to access value of particular attribute
        return self._name
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")
        self._name = value
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("Age must be a non-negative integer")
        self._age = value
 
person = Person("John", 30)
person.name = "Jane"
print(person.name)  # person._name()


try:
    person.name = 123
except TypeError as e:
    print(e)  
 
person.age = 25
 
try:
    person.age = -1
except ValueError as e:
    print(e)   
 






#typehit

from typing import List, Dict, Any


RAW_DATA: List[Dict[str, Any]]