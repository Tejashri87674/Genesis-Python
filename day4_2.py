from abc import ABC, abstractmethod

#import abc as a

# abc- module name
# ABC- class name , to mark our class as abstract
# abstarctmethod - a decorator which is used to mark method as abstract method

class Shape(ABC):
    
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
    
    
class Myclass(ABC):    
    @abstractmethod
    def hello(self):
        pass
    
    def hello2(self):
         print('In Myclass')
         
class Child(Myclass):
    def hello(self):
        print('hello from child class')
        
m1=Child()
m1.hello()
m1.hello2()

# Attempting to instantiate the abstract class will raise an error
try:
    shape = Shape()
except TypeError as e:
   print(e)

# Instantiating the concrete classes works fine
circle = Circle(5)
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")

rectangle = Rectangle(4, 6)
print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")

'''
class Shape:
   void draw(self): .....


class Circle(Shape)
    

class BigCircle(Circle)
     

c1=Circle()
c1.draw()



def add(a,b):
   -----

def add(a,b,c,d):
   ----

add(10,20)

add(1,2,3,4)
'''





#-----------------------------------------------------------------------------------

from abc import ABC, abstractmethod

# Abstract Base Class (ABC)
class Tour(ABC):
    def __init__(self, destination, price):
        self.destination = destination
        self.price = price

    @abstractmethod
    def get_details(self):
        """Abstract method that must be implemented by all subclasses"""
        pass

    @abstractmethod
    def calculate_discounted_price(self, discount):
        """Abstract method to calculate discounted price, must be overridden"""
        pass

# Child class 1: Adventure Tour
class AdventureTour(Tour):
    def __init__(self, destination, price, activity):
        super().__init__(destination, price)
        self.activity = activity

    def get_details(self):
        return f"Adventure Tour: {self.destination} - Activity: {self.activity} - Price: ${self.price}"

    def calculate_discounted_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return f"After {discount}% discount: ${discounted_price:.2f}"

# Child class 2: Luxury Tour
class LuxuryTour(Tour):
    def __init__(self, destination, price, hotel):
        super().__init__(destination, price)
        self.hotel = hotel

    def get_details(self):
        return f"Luxury Tour: {self.destination} - Stay at: {self.hotel} - Price: ${self.price}"

    def calculate_discounted_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return f"After {discount}% discount: ${discounted_price:.2f}"

# Child class 3: Cultural Tour
class CulturalTour(Tour):
    def __init__(self, destination, price, guide_name):
        super().__init__(destination, price)
        self.guide_name = guide_name

    def get_details(self):
        return f"Cultural Tour: {self.destination} - Guide: {self.guide_name} - Price: ${self.price}"

    def calculate_discounted_price(self, discount):
        discounted_price = self.price - (self.price * discount / 100)
        return f"After {discount}% discount: ${discounted_price:.2f}"

# Creating tour objects
adventure_tour = AdventureTour("Mount Everest", 3000, "Trekking")
luxury_tour = LuxuryTour("Maldives", 5000, "5-Star Resort")
cultural_tour = CulturalTour("Egypt", 2000, "Dr. Ahmed")

# Displaying tour details and discounted prices
tours = [adventure_tour, luxury_tour, cultural_tour]

for tour in tours:
    print(tour.get_details())
    print(tour.calculate_discounted_price(10))  # Applying a 10% discount
    print()
 




#---------------------------------------------------------

Abstract Base Class: VehicleComponent (Abstract)
• Attributes: 
o component_id: str
o status: str (e.g., "OK", "Fault")
o reading: float (numeric performance metric)
• Abstract Methods: 
o status_message() → Must return a detailed health message.
o validate_reading() → Must validate readings and raise exceptions if unsafe.
o compute_efficiency() → Abstract method to calculate efficiency based on component-specific logic.

Derived Classes
Class 1: EngineSensor
• Additional Attributes: 
o rpm: int
o temperature: float
o max_rpm=6000
• Complex Methods: 
o Override compute_efficiency(): 
 Efficiency = (rpm / max_rpm) * (1 - temperature_penalty)
 Use lambda for penalty calculation.
o Override status_message(): 
 Include dynamic analysis: "Engine running smoothly" or "Engine alert!" based on condition of status.(if status is not “OK” then "Engine alert!” otherwise "Engine running smoothly")
o Override validate_reading(): 
 Raise EngineOverheatException if temperature > 150°C.
 Log warnings if rpm exceeds safe range.

Class 2: BrakeSensor
• Additional Attributes: 
o pad_thickness: float (in mm)
o fluid_level: float (in %)
o ideal_thickness=5.0
• Complex Methods: 
o Override compute_efficiency(): 
 Efficiency = (fluid_level / 100) * (pad_thickness / ideal_thickness)
 Use lambda for quick ratio calculation.
o Override status_message(): 
 Return "Brakes optimal" or "Brake maintenance required" with severity level.
(if status is not “OK” then " Brake maintenance required” otherwise " Brakes optimal ")

o Override validate_reading(): 
 Raise BrakeFailureException if pad_thickness < 1 mm.
 Suggest maintenance schedule dynamically.

Custom Exceptions
• EngineOverheatException : Raised when engine temperature exceeds safe limit.
• BrakeFailureException : Raised when brake pad thickness is critically low.

Object Creation
o Create 3 EngineSensor objects and 2 BrakeSensor objects.
o Store all objects in a list called components.

Functions
Implement the following operations:
1. filter_faulty_components(components)
o Return components where status != "OK".
o Use list comprehension and isinstance() to group by type.
2. sort_components_by_efficiency(components)
o Sort components by computed efficiency using their compute_efficiency() method.
o Use lambda with sorted().
3. generate_health_report(components)
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
 