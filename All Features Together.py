# © 2024 
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Final Stage: All Features Together

from abc import ABC, abstractmethod

# Abstract class
class Vehicle(ABC):
    def __init__(self, make, model):
        self.__make = make  # Private attribute
        self.__model = model  # Private attribute

    @abstractmethod
    def start_engine(self):
        pass

    def display_info(self):
        print(f'Vehicle: {self.__make} {self.__model}')

    # Encapsulation: Getter and Setter methods
    def get_make(self):
        return self.__make

    def set_make(self, make):
        self.__make = make

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

# Composition
class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f'The {self.engine_type} engine is starting.')

# Inheritance and Polymorphism
class Car(Vehicle):
    def __init__(self, make, model, doors, engine_type):
        super().__init__(make, model)
        self.doors = doors
        self.engine = Engine(engine_type)  # Composition

    def start_engine(self):
        self.engine.start()

    # Polymorphism
    def display_info(self, detailed=False):
        super().display_info()
        print(f'This car has {self.doors} doors.')
        if detailed:
            print(f'Engine type: {self.engine.engine_type}')

class Motorcycle(Vehicle):
    def __init__(self, make, model, type, engine_type):
        super().__init__(make, model)
        self.type = type
        self.engine = Engine(engine_type)  # Composition

    def start_engine(self):
        self.engine.start()

    def display_info(self):
        super().display_info()
        print(f'This motorcycle is a {self.type} type.')

# Method Overloading (using default arguments)
class Truck(Vehicle):
    def __init__(self, make, model, capacity, engine_type):
        super().__init__(make, model)
        self.capacity = capacity
        self.engine = Engine(engine_type)  # Composition

    def start_engine(self):
        self.engine.start()

    def display_info(self, detailed=False):
        super().display_info()
        print(f'This truck has a capacity of {self.capacity} tons.')
        if detailed:
            print(f'Engine type: {self.engine.engine_type}')

def main():
    vehicles = [
        Car('Toyota', 'Corolla', 4, 'V6'),
        Motorcycle('Harley-Davidson', 'Street 750', 'Cruiser', 'V-Twin'),
        Truck('Volvo', 'FH16', 25, 'Diesel')
    ]

    for vehicle in vehicles:
        vehicle.display_info()
        vehicle.start_engine()
        print()

if __name__ == '__main__':
    main()
