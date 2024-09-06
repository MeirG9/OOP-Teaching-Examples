# © 2024 
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Stage 4: Polymorphism

from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    @abstractmethod
    def start_engine(self):
        pass

    def display_info(self):
        print(f'Vehicle: {self.make} {self.model}')

class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def start_engine(self):
        print(f'The engine of the car {self.make} {self.model} is starting.')

    def display_info(self):
        super().display_info()
        print(f'This car has {self.doors} doors.')

class Motorcycle(Vehicle):
    def __init__(self, make, model, type):
        super().__init__(make, model)
        self.type = type

    def start_engine(self):
        print(f'The engine of the motorcycle {self.make} {self.model} is starting.')

    def display_info(self):
        super().display_info()
        print(f'This motorcycle is a {self.type} type.')

def main():
    vehicles = [
        Car('Toyota', 'Corolla', 4),
        Motorcycle('Harley-Davidson', 'Street 750', 'Cruiser')
    ]

    for vehicle in vehicles:
        vehicle.display_info()
        vehicle.start_engine()

if __name__ == '__main__':
    main()
