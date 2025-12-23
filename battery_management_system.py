from battery_status import BatteryStatus
from battery_type import BatteryType
from battery import Battery

class BatteryManagementSystem:
   def __init__(self, max_voltage_limit=4.2, min_voltage_limit=2.5, max_temp_limit=60):
       self.batteries = {}
       self.max_voltage_limit = max_voltage_limit
       self.min_voltage_limit = min_voltage_limit
       self.max_temp_limit = max_temp_limit
       self.alerts = []
 
   # Add Battery
   def add_battery(self, battery: Battery):
       self.batteries[battery.battery_id] = battery
       print(f"Battery {battery.battery_id} added.")
 
   # Remove Battery
   def remove_battery(self, battery_id):
       if battery_id in self.batteries:
           del self.batteries[battery_id]
           print(f"Battery {battery_id} removed.")
       else:
           print("Battery not found.")
 
   # Update Status
   def update_status(self, battery_id, new_status: BatteryStatus):
       if battery_id in self.batteries:
           self.batteries[battery_id].status = new_status
           print(f"Battery {battery_id} status updated to {new_status.value}.")
       else:
           print("Battery not found.")
 
   # Monitoring & Calculations
   def calculate_total_voltage(self):
       return sum(b.voltage for b in self.batteries.values())
 
   def calculate_average_temperature(self):
       return sum(b.temperature for b in self.batteries.values()) / len(self.batteries) if self.batteries else 0
 
   def battery_with_max_voltage(self):
       return max(self.batteries.values(), key=lambda b: b.voltage)
 
   def battery_with_min_temperature(self):
       return min(self.batteries.values(), key=lambda b: b.temperature)
 
   def filter_above_max_temp(self):
       return {bid: b for bid, b in self.batteries.items() if b.temperature > self.max_temp_limit}
 
   def filter_below_min_voltage(self):
       return {bid: b for bid, b in self.batteries.items() if b.voltage < self.min_voltage_limit}
 
   # Alerts using lambda
   def generate_alerts(self):
       check_alert = lambda b: (
           f"Alert: Battery {b.battery_id} abnormal condition!" 
           if b.voltage > self.max_voltage_limit or b.voltage < self.min_voltage_limit or b.temperature > self.max_temp_limit 
           else None
       )
       self.alerts = [alert for b in self.batteries.values() if (alert := check_alert(b))]
       return self.alerts
 
   # Summary dictionary of voltages
   def summary_voltages(self):
       return {bid: b.voltage for bid, b in self.batteries.items()}
 
   # List of battery types
   def list_battery_types(self):
       return [b.battery_type.value for b in self.batteries.values()]
 
   # Sort batteries by voltage
   def sort_by_voltage(self):
       return sorted(self.batteries.values(), key=lambda b: b.voltage)
 
   # Sort by temperature descending
   def sort_by_temperature_desc(self):
       return sorted(self.batteries.values(), key=lambda b: b.temperature, reverse=True)
 
   # Count batteries by status
   def count_by_status(self):
       return {status.value: sum(1 for b in self.batteries.values() if b.status == status) for status in BatteryStatus}
 
   # Predict charging completion time (simple model)
   def predict_charging_time(self, battery_id, charging_rate=0.1):
       if battery_id in self.batteries and self.batteries[battery_id].status == BatteryStatus.CHARGING:
           remaining = self.max_voltage_limit - self.batteries[battery_id].voltage
           return (lambda r: remaining / r)(charging_rate)
       return None
 
   # Check if all batteries are healthy
   def all_batteries_healthy(self):
       return all(self.min_voltage_limit <= b.voltage <= self.max_voltage_limit and b.temperature <= self.max_temp_limit for b in self.batteries.values())
 