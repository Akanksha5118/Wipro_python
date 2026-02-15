class Vehicle:
    # Class variable to track number
    vehicle_count = 0

    def __init__(self):
        Vehicle.vehicle_count += 1

    def start(self):
        print("Vehicle is starting")

#Single Inheritance
#Car inherits from Vehicle
class Car(Vehicle):
    def drive(self):
        print("Car is being driven")

# Multilevel Inheritance
# ElectricCar inherits from Car
class ElectricCar(Car):
    def charge(self):
        print("Electric car is charging")

# Creating objects
v1=Vehicle()
c1=Car()
e1=ElectricCar()

# Calling Methods
v1.start()
c1.start()
c1.drive()
e1.start()
e1.drive()
e1.charge()


# Display total number of vehicles created
print("Total vehicles created:" , Vehicle.vehicle_count)