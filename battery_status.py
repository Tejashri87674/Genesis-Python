from enum import Enum
class BatteryStatus(Enum):
   CHARGING = "Charging"
   DISCHARGING = "Discharging"
   IDLE = "Idle"
   FAULT = "Fault"