"""
Homework Assignment #9: Classes

"""
import random
from termcolor import colored, cprint

# define vehicle class - parent class
class Vehicle:
    def __init__(self, make, model, year, weight, needsMaintenance = False, tripsSinceMaintenance = 0):
        self.make = make
        self.model = model
        self.year = year
        self.weight = weight
        self.needsMaintenance = needsMaintenance
        self.tripsSinceMaintenance = tripsSinceMaintenance

    #setters
    def setMake(self, make):
        self.make = make        

    def setModel(self, mode):
        self.mode = mode      

    def setYear(self, year):
        self.year = year      

    def setWeight(self, weight):
        self.weight = weight      
    
    #getters
    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getYear(self):
        return self.year

    def getWeight(self):
        return self.weight
    
    def repair(self):
        self.tripsSinceMaintenance = 0
        self.needsMaintenance = False

# define cars class - inherited from vehicle class
class Cars(Vehicle):
    def __init__(self, make, model, year, weight, isDriving = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isDriving = isDriving
    
    def drive(self):
        self.isDriving = True
    
    def stop(self):
        if self.isDriving:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isDriving = False

# define plane class - inherited from vehicle class
class Plane(Vehicle):
    def __init__(self, make, model, year, weight, isFlying = False):
        Vehicle.__init__(self, make, model, year, weight)
        self.isFlying = isFlying
    
    def flying(self):
        if self.needsMaintenance == True:
            return False
        self.isFlying = True
        return True
    
    def landing(self):
        if self.isFlying:
            self.tripsSinceMaintenance += 1
            if self.tripsSinceMaintenance > 100:
                self.needsMaintenance = True
        self.isFlying = False

# helpers functions

# drive and stop car random no of times
def randomly_drive_car(car):
    drive_times = random.randint(1, 101)
    for i in range(drive_times):
        car.drive()
        car.stop()

# fly and land plane random no of times
def randomly_fly_plane(plane, fly_times = None):
    fly_times = random.randint(1, 101) if fly_times is None else fly_times
    for i in range(fly_times):
        is_flying = plane.flying()
        if is_flying:
            plane.landing()
        else:
            cprint("plane " + plane.model + " can't fly until it's repair", 'red', attrs=['bold'])
            cprint("Repairing... " + plane.model, 'blue', attrs=['bold'])
            plane.repair()

# print car attributes         
def print_car_specs(car):
    print("========================")
    print('Make ',car.make)
    print('Model ',car.model)
    print('Year ',car.year)
    print('Weight ',car.weight)
    print('Needs Maintenance ',car.needsMaintenance)
    print('Trips Since Maintenance ',car.tripsSinceMaintenance)
    print('Weight ',car.weight)
    print("========================\n")

# print plane attributes
def print_plane_specs(plane):
    print("========================")
    print('Make ',plane.make)
    print('Model ',plane.model)
    print('Year ',plane.year)
    print('Weight ',plane.weight)
    print('Needs Maintenance ',plane.needsMaintenance)
    print('Trips Since Maintenance ',plane.tripsSinceMaintenance)
    print('Weight ',plane.weight)
    print("========================\n")

# creating three instances from Cars class
carOne = Cars("volkswagen group", "ameo", 2010, 1033 )
carTwo = Cars("volkswagen group", "polo", 2008, 1038 )
carThree = Cars("volkswagen group", "vento", 2010, 1023 )

# creating two objects from Plane class
planeOne = Plane("Aeronca","15 AC Sedan", 1992, 2050)
planeTwo = Plane("Aeronca","12 AC Sedan", 1982, 2030)

# using helpers function, randomly driving cars and fly planes
randomly_drive_car(carOne)
randomly_drive_car(carTwo)
randomly_drive_car(carThree)
randomly_fly_plane(planeOne)
randomly_fly_plane(planeTwo, 102)

# printing cars and plane attributes
print_car_specs(carOne)
print_car_specs(carTwo)
print_car_specs(carThree)
print_plane_specs(planeOne)
print_plane_specs(planeTwo)