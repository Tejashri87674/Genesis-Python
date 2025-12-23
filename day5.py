class Vehicle:
    vehicle_count=0
    def __init__(self,brand,model):
      # self.model self.brand are instance member
      self.brand=brand
      self.model=model
      Vehicle.vehicle_count +=1

    @classmethod
    def from_string(cls,vehicle_str):
       "create vehicle object from a string like 'Toyota-corolla' ."
       brand,model=vehicle_str.split('-')
       return cls(brand,model)
    
    @classmethod
    def total_vehicle(cls):
       "return total number of vehicle created"
       return f"Total vehicles: {cls.vehicle_count}"

#"crate obj noramlly"
#v1=Vehicle("honda","civic")
#create obj using class method
v3=Vehicle.from_string("Toyota-Corolla")
#check totla vehicles
print(Vehicle.total_vehicle())

print("---------------------------------------------------------------------------")

class Student:
    school_name = "ABC School"
    student_count = 0

    def __init__(self, name, grade):
        self.name = name     
        self.grade = grade 
        Student.student_count += 1

    def show_details(self):
        print(f"Name: {self.name}, Grade: {self.grade}, School: {Student.school_name}")

    @classmethod
    def change_school(cls, new_name):
        cls.school_name = new_name 
        print(f"School name changed to: {cls.school_name}")

    @classmethod
    def get_student_count(cls):
        return cls.student_count

s1 = Student("xyz", "11th")
s2 = Student("pqr", "10th")
s1.show_details()
s2.show_details()
Student.change_school("International School")
s1.show_details()
s2.show_details()
print("Total Students:", Student.get_student_count())
