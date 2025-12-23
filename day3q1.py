'''
Case Study: Automotive Vehicle Management System
 
A vehicle manufacturing company wants to manage its vehicle inventory, including details such as vehicle type, model, year, color, and engine type.
 The company also wants to track the sales and maintenance history of each vehicle.
 
Program Requirements:
 
Create a Vehicle class to store vehicle information.
Create a Sales class to store sales information and update the vehicle status.
Create a Maintenance class to store maintenance information and update the vehicle status.
Implement functions to:
Add a vehicle to the inventory.
Display vehicle information.
Update vehicle status (e.g., sold, in-maintenance).
Record sales information.
Record maintenance information.
Display sales history for a vehicle.
Display maintenance history for a vehicle.
'''
class Vehicle:
    def __init__(self,vehicleId,vehicleType,model,year,color,engineType):
        self.vehicleId=vehicleId
        self.vehicleType=vehicleType
        self.model=model 
        self.year=year
        self.color=color
        self.engineType=engineType
        self.status="Available"
        self.sales_history=[]
        self.maintenance_history=[]
    
    def __repr__(self):
        return ()
    



from enum import Enum

# Define Enum for Vehicle Types
class VehicleType(Enum):
    CAR = "Car"
    TRUCK = "Truck"
    MOTORCYCLE = "Motorcycle"

class VehicleRecords:
    def __init__(self):
        self.vehicles = {}
        self.fuel_types = ["Gasoline", "Diesel", "Electric"]
        self.transmission_types = ["Automatic", "Manual"]

    def add_vehicle(self, vehicle_type: VehicleType, make, model, year, fuel_type, transmission_type, mileage=0):
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")
        
        vehicle_id = len(self.vehicles) + 1
        self.vehicles[vehicle_id] = {
            "vehicle_type": vehicle_type.value,  # Store the string value
            "make": make,
            "model": model,
            "year": year,
            "fuel_type": fuel_type,
            "transmission_type": transmission_type,
            "mileage": mileage,
            "maintenance_records": []
        }
        print(f"Vehicle added with ID: {vehicle_id}")

    def remove_vehicle(self, vehicle_id):
        if vehicle_id in self.vehicles:
            del self.vehicles[vehicle_id]
            print(f"Vehicle with ID {vehicle_id} removed")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")

    def update_vehicle(self, vehicle_id, make=None, model=None, year=None, fuel_type=None, transmission_type=None, mileage=None):
        if vehicle_id in self.vehicles:
            if make:
                self.vehicles[vehicle_id]["make"] = make
            if model:
                self.vehicles[vehicle_id]["model"] = model
            if year:
                self.vehicles[vehicle_id]["year"] = year
            if fuel_type:
                self.vehicles[vehicle_id]["fuel_type"] = fuel_type
            if transmission_type:
                self.vehicles[vehicle_id]["transmission_type"] = transmission_type
            if mileage:
                self.vehicles[vehicle_id]["mileage"] = mileage
            print(f"Vehicle with ID {vehicle_id} updated")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")

    def get_vehicle_info(self, vehicle_id):
        return self.vehicles.get(vehicle_id, None)

    def drive_vehicle(self, vehicle_id, miles):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id]["mileage"] += miles
            print(f"Vehicle with ID {vehicle_id} driven for {miles} miles")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")

    def perform_maintenance(self, vehicle_id, maintenance_type, description):
        if vehicle_id in self.vehicles:
            self.vehicles[vehicle_id]["maintenance_records"].append({
                "maintenance_type": maintenance_type,
                "description": description
            })
            print(f"Maintenance performed on Vehicle with ID {vehicle_id}")
        else:
            print(f"Vehicle with ID {vehicle_id} not found")

    def display_all_vehicles(self):
        for vehicle_id, vehicle_info in self.vehicles.items():
            print(f"Vehicle ID: {vehicle_id}")
            print(f"Vehicle Type: {vehicle_info['vehicle_type']}")
            print(f"Make: {vehicle_info['make']}")
            print(f"Model: {vehicle_info['model']}")
            print(f"Year: {vehicle_info['year']}")
            print(f"Fuel Type: {vehicle_info['fuel_type']}")
            print(f"Transmission Type: {vehicle_info['transmission_type']}")
            print(f"Mileage: {vehicle_info['mileage']}")
            print(f"Maintenance Records: {vehicle_info['maintenance_records']}")
            print("--------------------")

    def filter_vehicles_by_type(self, vehicle_type: VehicleType):
        if not isinstance(vehicle_type, VehicleType):
            raise ValueError("Invalid vehicle type. Must be a VehicleType Enum.")
        
        filtered_vehicles = {
            vehicle_id: vehicle_info
            for vehicle_id, vehicle_info in self.vehicles.items()
            if vehicle_info["vehicle_type"] == vehicle_type.value
        }
        return filtered_vehicles

# Example Usage
vehicle_records = VehicleRecords()

# Add vehicles using Enum
vehicle_records.add_vehicle(VehicleType.CAR, "Toyota", "Corolla", 2015, "Gasoline", "Automatic", 50000)
vehicle_records.add_vehicle(VehicleType.TRUCK, "Ford", "F-150", 2018, "Diesel", "Manual", 30000)
vehicle_records.add_vehicle(VehicleType.MOTORCYCLE, "Honda", "CBR500R", 2020, "Gasoline", "Manual", 10000)

# Display all vehicles
vehicle_records.display_all_vehicles()

# Filter by Enum type
filtered_vehicles = vehicle_records.filter_vehicles_by_type(VehicleType.CAR)
print("Filtered Vehicles by Type:")
for vehicle_id, vehicle_info in filtered_vehicles.items():
    print(vehicle_info)
 





#example
 '''
 Create two classes:
Battery → Represents individual battery cells with 5 attributes (including Enums).
BatteryManagementSystem → Manages a dictionary of Battery objects and performs operations using lambda and comprehensions.
 
-Enums to Use
BatteryType → LI_ION, NIMH, LEAD_ACID, SOLID_STATE
BatteryStatus → CHARGING, DISCHARGING, IDLE, FAULT
 
-Battery Class
Attributes:
battery_id → Unique identifier for the battery.
battery_type → Enum BatteryType.
status → Enum BatteryStatus.
voltage → Current voltage of the battery.
temperature → Current temperature of the battery.
 
BatteryManagementSystem Class
Attributes:
batteries → Dictionary where key = battery_id, value = Battery object.
max_voltage_limit, min_voltage_limit, max_temp_limit → Safety thresholds.
alerts → List of alerts generated.
 
Functionalities (using lambda & comprehensions)
Add a new Battery object to dictionary
      → Validate Enums and store in batteries.
Remove a Battery by ID
Update Battery status:→ Change Enum status dynamically.
Monitoring & Calculation
Calculate total voltage of all batteries.
Calculate average temperature.
Find battery with max voltage
Find battery with min temperature.
Filter batteries above max temperature
Filter batteries below min voltage.
Generate alerts for abnormal conditions:→ Use lambda to check and append alerts.
Create summary dictionary of battery voltages.
Create list of battery types.
Sort batteries by voltage
Sort batteries by temperature descending
Count batteries by status
Predict charging completion time:→ Lambda based on voltage difference and charging rate.
Generate historical voltage trend:→ Extract voltages from logs using [h['voltage'] for h in history].
Check if all batteries are healthy (within limits)
 '''