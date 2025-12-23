from battery_status import BatteryStatus
from battery_type import BatteryType

class Battery:
   def __init__(self, battery_id, battery_type: BatteryType, status: BatteryStatus, voltage: float, temperature: float):
       if not isinstance(battery_type, BatteryType):
           raise ValueError("Invalid battery type. Must be BatteryType Enum.")
       if not isinstance(status, BatteryStatus):
           raise ValueError("Invalid battery status. Must be BatteryStatus Enum.")
       
       self.battery_id = battery_id
       self.battery_type = battery_type
       self.status = status
       self.voltage = voltage
       self.temperature = temperature
 
   def __repr__(self):
       return f"Battery(ID={self.battery_id}, Type={self.battery_type.value}, Status={self.status.value}, Voltage={self.voltage}, Temp={self.temperature})"
 