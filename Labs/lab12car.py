'''
CS 115, Lab 12, Inheritance

Author: Edward Yaroslavsky eyarosla 11/29/18
Pledge: I pledge my honor that I have abided by the Stevens Honor System.
'''

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 1 
' Implement missing sections of the Car class.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class Car(object):
    '''Write the constructor. It should take in four arguments:
       - make (a string, the company name, a.k.a. brand)
       - model (a string)
       - mpg (miles per gallon, a float)
       - tank_capacity (capacity of the gas tank in gallons, a float)
       These should all be assigned to corresponding private fields, i.e., with
       names that start with '__'.  Use the names in the 'str' method provided below.
       '''
    def __init__(self, make, model, mpg, tank_capacity):
        self.make = make
        self.model = model
        self.mpg = mpg
        self.tank_capacity = tank_capacity

    '''Write getters for make, model, mpg, and tank_capacity.'''
    def getMake(self): return self.make

    def getModel(self): return self.model

    def getMPG(self): return self.mpg

    def getTankCapacity(self): return self.tank_capacity

    '''Write setters for mpg and tank_capacity.'''
    def setMPG(self, mpg): self.mpg = mpg

    def setTankCapacity(self, tank_capacity): self.tank_capacity = tank_capacity

    '''Write a method called get_total_range.
       It returns the total distance the car can travel on a full tank of
       gas.'''
    def get_total_range(self):
        return self.getMPG() * self.getTankCapacity()


    def __str__(self):
        '''A string for printing information about a car.'''
        return self.make + ' ' + self.model + ', MPG: ' + str(self.mpg) \
            + ', tank capacity: ' + str(self.tank_capacity)

'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Part 2 
' Implement missing sections of the HybridCar class. 
' Make HybridCar be a subclass of Car.
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
class HybridCar(Car):  
    '''Write the constructor. It should take in 6 arguments:
    - the first four are the same as in the Car constructor
    - battery_kWh (battery power in kilowatt-hours, a float)
    - miles_per_kWh (miles per kilowatt-hours, a float)
    The additional fields must be private.
    '''
    def __init__(self, make, model, mpg, tank_capacity, battery_kWh, miles_per_kWh):
        self.make = make
        self.model = model
        self.mpg = mpg
        self.tank_capacity = tank_capacity
        self.battery_kWh = battery_kWh
        self.miles_per_kWh = miles_per_kWh

    '''Write getters for battery_kWh and miles_per_kWh.'''
    def getBatteryKWH(self): return self.battery_kWh

    def getMilesPerKWH(self): return self.miles_per_kWh

    '''Implement the following method.'''
    def get_battery_range(self):
        '''Returns the total distance the car can travel on a fully charged
        battery.
        '''
        return self.getBatteryKWH() * self.getMilesPerKWH()
 

    '''Override the method get_total_range.
    Returns the total distance the car can travel on a full tank of
    gas and a fully charged battery.
    Do not do any math here except a single +. To get credit, you must call
    the methods you have already written.
    '''
    def get_total_range(self):
        return self.get_battery_range() + super().get_total_range()

    def __str__(self):
        '''A string for printing information about a car.'''
        return super().__str__() + ', battery kWh: ' + \
            str(self.battery_kWh) + ', miles/kWh: ' + \
            str(self.miles_per_kWh)
