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
from enum import Enum

#enum BatteryType
class BatteryType(Enum):
    LI_ION=1
    NIMH=2
    LEAD_ACID=3
    SOLID_STATE=4
#enum BatteryStatus
class BatteryStatus(Enum):
    CHARGING=1
    DISCHARGING=2
    IDLE=3
    FAULT=4

class Battery:
    def __init__(self,battery_id,battery_type,status,voltage,temperature):
        if not isinstance(battery_type,BatteryType):
            raise ValueError("battery type must be batteryType in enum")
        
        if not isinstance(status,BatteryStatus):
            raise ValueError("status must be batteryStatus enum")
        
        self.battery_id=battery_id
        self.battery_type=battery_type
        self.status=status
        self.voltage=voltage
        self.temperature=temperature

    def __repr__(self):
        return f"battery id: {self.battery_id}, battery_type: {self.battery_type}, status:{self.status}, voltage:{self.voltage},temperature:{self.temperature}"
    
class BatteryManagementSystem:
    def __init__(self,max_voltage_limit=4.2,min_voltage_limit=2.5,max_temp_limit=60):
        self.batteries={}
        self.max_voltage_limit=max_voltage_limit
        self.min_voltage_limit=min_voltage_limit
        self.max_temp_limit=max_temp_limit
        self.alerts=[]

    def add_battery(self,battery:Battery):
        self.batteries[battery.battery_id]=battery
    
    def remove_battery(self,battery_id):
        self.batteries.pop(battery_id,None)

    def update_status(self,battery_id,new_status):
        if battery_id in self.batteries:
            if isinstance(new_status,BatteryStatus):
                self.batteries[battery_id].status=new_status

    #calculate total voltage   
    def total_voltage(self):
        return sum(b.voltage for b in self.batteries.values())
    
    #avg temperature
    def average_temprature(self):
        return sum(b.temperature for b in self.batteries.values())/len(self.batteries) if self.batteries else 0
    

    def max_voltage_battery(self):
        return max(self.batteries.values(),key=lambda b:b.voltage) 

    def min_temperature_battery(self):
        return min(self.batteries.values(),key=lambda b:b.temperature)

    def filter_over_temp(self):
        return [b for b in self.batteries.values() if b.temperature>self.max_temp_limit]   

    def filter_low_voltge(self):
        return [b for b in self.batteries.values() if b.voltage<self.min_voltage_limit]
    
    def generate_alerts(self):
        self.alerts=[]
        check=lambda b:(b.temperature>self.max_temp_limit or b.voltage> self.max_voltage_limit or b.voltage<self.min_voltage_limit)
        for b in self.batteries.values():
            if check(b):
                self.alerts.append(f"Alert: {b.battery_id} abnormal condition")

    #list of battery type
    def battery_types_list(self):
        return [b.battery_type.name for b in self.batteries.values()]
    
    #sort batteries by voltage
    def sort_by_voltage(self):
        return sorted(self.batteries.values(),key=lambda b:b.voltage)
    
    #sort batteries by temp desc
    def sort_by_temp(self):
        return sorted(self.batteries.values(), key=lambda b:b.temperature,reverse=True)

    #Count batteries by status
    def count_by_status(self):
        return {status.name:sum(1 for b in self.batteries.values() if b.status==status)
                for status in BatteryStatus }
    #predict charging completion time
    def predict_completion_time(self,battery_id,max_voltage=4.2,rate=0.05):
        b=self.batteries.get(battery_id)
        if not b:
            return None
        return max((max_voltage - b.voltage)/rate,0)
    
    #historical voltage trend
    @staticmethod
    def voltage_trend(history):
        return [h['voltage']for h in history]
    
    #check if all batteries are healthy
    def all_healthy(self):
        return all(
            self.min_voltage_limit<=b.voltage<=self.max_voltage_limit and
            b.temperature<=self.max_temp_limit 
            for b in self.batteries.values()
        )


if __name__ == "__main__":
    b1=Battery("1",BatteryType.LI_ION,BatteryStatus.CHARGING,3.5,35)
    b2=Battery("2",BatteryType.NIMH,BatteryStatus.IDLE,4.0,45)
    b3=Battery("3",BatteryType.SOLID_STATE,BatteryStatus.DISCHARGING,2.2,65)

    bms=BatteryManagementSystem()
    bms.add_battery(b1)
    bms.add_battery(b2)
    bms.add_battery(b3)

    bms.generate_alerts()
    print("Alerts: ",bms.alerts)
    print("total voltage: ",bms.total_voltage())
    print("healthy: ",bms.all_healthy())
