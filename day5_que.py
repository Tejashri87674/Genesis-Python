Design a Python program to estimate the State of Health (SoH) of a Lithium-ion battery used in an Electric Vehicle, utilizing data from the BMS.
 
Create a class Battery with the following attributes:
cell_voltage (list of floats): Voltage of each cell in the battery pack.
current (float): Current flowing through the battery (positive for discharge, negative for charge).
temperature (float): Battery pack temperature in Celsius.
cycle_count (int): Number of charge/discharge cycles completed.
 
Battery Management System Class:
Create a class BMS that manages the Battery object and implements SoH estimation.
Implement the following functions using Lambda expressions where appropriate:
calculate_average_cell_voltage():
Input: cell_voltages (List of floats): A list representing the voltage of each cell in the battery.
Task: Calculate the average voltage of all cells in the input list. Uses a Lambda function for a concise calculation.
Output: float: The average cell voltage. Returns 0.0 if the input list is empty.
Constraints:
Input list must contain only numerical values (floats or integers).
Handles empty input list gracefully.
detect_overvoltage(threshold):
Input:
cell_voltages (List of floats): A list representing the voltage of each cell.
threshold (float): The voltage threshold. Cells with voltage exceeding this threshold are considered overvoltage.
Task: Identify cells in cell_voltages that exceed the specified threshold. Uses a Lambda function with filter() to achieve this. Returns a list of indices (positions) of the overvoltage cells.
Output: List[int]: A list of indices corresponding to the cells exceeding the threshold. Returns an empty list if no cells exceed the threshold.
Constraints:
Input list must contain only numerical values (floats or integers).
Threshold must be a numerical value.
apply_temperature_correction(voltage, temperature):
Input:
voltage (float): The cell voltage to be corrected.
temperature (float): The temperature of the cell in Celsius.
Task: Apply a temperature correction factor to the cell voltage using a Lambda function. The correction factor is calculated as 1 + 0.005 * (temperature - 25).
Output: float: The temperature-corrected voltage.
Constraints:
Voltage and temperature must be numerical values.
 
estimate_soh(capacity):
Input:
current_capacity (float): The current capacity of the battery.
original_capacity (float): The original capacity of the battery.
Task: Estimate the State of Health (SoH) as a percentage of the original capacity. Uses a Lambda function to calculate the SoH. SoH = (Current Capacity / Original Capacity) * 100.
Output: float: The estimated SoH as a percentage. Returns 0.0 if original_capacity is zero to avoid division by zero.
Constraints:
Capacities must be numerical values.
Handles the case where the original capacity is zero to avoid division by zero.
 
Create objects:
battery1:
cell_voltage: [3.6, 3.7, 3.8, 3.9, 3.7]
current: 10.0 (Discharge)
temperature: 25.0
cycle_count: 100
battery2:
cell_voltage: [4.0, 4.1, 4.2, 4.1, 4.0]
current: -5.0 (Charge)
temperature: 40.0
cycle_count: 500
battery3:
cell_voltage: [3.5, 3.4, 3.6, 3.3, 3.5]
current: 8.0 (Discharge)
temperature: 0.0
cycle_count: 200








#que2
Abstract Base Class: VehicleComponent (Abstract)
Attributes:  
component_id: str
status: str (e.g., "OK", "Fault")
reading: float (numeric performance metric)
Abstract Methods:
status_message() → Must return a detailed health message.
validate_reading() → Must validate readings and raise exceptions if unsafe.
compute_efficiency() → Abstract method to calculate efficiency based on component-specific logic.
 
Derived Classes
Class 1: EngineSensor
Additional Attributes:
rpm: int
temperature: float
max_rpm=6000
Complex Methods:
Override compute_efficiency():
Efficiency = (rpm / max_rpm) * (1 - temperature_penalty)
Use lambda for penalty calculation.
Override status_message():
Include dynamic analysis: "Engine running smoothly" or "Engine alert!" based on condition of status.(if status is not “OK” then "Engine alert!” otherwise "Engine running smoothly")
Override validate_reading():
Raise EngineOverheatException if temperature > 150°C.
Log warnings if rpm exceeds safe range.
 
Class 2: BrakeSensor
Additional Attributes:
pad_thickness: float (in mm)
fluid_level: float (in %)
ideal_thickness=5.0
Complex Methods:
Override compute_efficiency():
Efficiency = (fluid_level / 100) * (pad_thickness / ideal_thickness)
Use lambda for quick ratio calculation.
Override status_message():
Return "Brakes optimal" or "Brake maintenance required" with severity level.
(if status is not “OK” then " Brake maintenance required” otherwise " Brakes optimal ")
 
Override validate_reading():
Raise BrakeFailureException if pad_thickness < 1 mm.
Suggest maintenance schedule dynamically.
 
Custom Exceptions
EngineOverheatException : Raised when engine temperature exceeds safe limit.
BrakeFailureException : Raised when brake pad thickness is critically low.
 
Object Creation
Create 3 EngineSensor objects and 2 BrakeSensor objects.
Store all objects in a list called components.
 
Functions
Implement the following operations:
filter_faulty_components(components)
Return components where status != "OK".
Use list comprehension and isinstance() to group by type.
sort_components_by_efficiency(components)
Sort components by computed efficiency using their compute_efficiency() method.
Use lambda with sorted().
generate_health_report(components)
Output a dictionary:
{
"total_components": int,
"engine_alerts": int,
"brake_alerts": int,
"average_efficiency": float
}
Use dictionary comprehension and map().
 
# EngineSensor Objects
e1 = EngineSensor(component_id="E001", status="OK", reading=85.0, rpm=2500, temperature=95.0)
e2 = EngineSensor(component_id="E002", status="Fault", reading=70.0, rpm=7000, temperature=160.0)
e3 = EngineSensor(component_id="E003", status="OK", reading=90.0, rpm=1500, temperature=110.0)

# BrakeSensor Objects
b1 = BrakeSensor(component_id="B001", status="OK", reading=60.0, pad_thickness=4.5, fluid_level=80.0)
b2 = BrakeSensor(component_id="B002", status="Fault", reading=40.0, pad_thickness=0.8, fluid_level=30.0)
 
# Combine into a single list
components = [e1, e2, e3, b1, b2]