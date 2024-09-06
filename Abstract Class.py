# © 2024 Meir Garada
# Email: MeirGarada@gmail.com
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Stage 3: Abstract Class

from abc import ABC, abstractmethod

# Abstract class Vehicle
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

def main():
    car = Car('Toyota', 'Corolla', 4)
    car.display_info()
    car.start_engine()

if __name__ == '__main__':
    main()
