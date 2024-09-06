# © 2024 Meir Garada
# Email: MeirGarada@gmail.com
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Stage 5: Encapsulation and Composition

from abc import ABC, abstractmethod

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

class Engine:
    def __init__(self, engine_type):
        self.engine_type = engine_type

    def start(self):
        print(f'The {self.engine_type} engine is starting.')

class Car(Vehicle):
    def __init__(self, make, model, doors, engine_type):
        super().__init__(make, model)
        self.doors = doors
        self.engine = Engine(engine_type)  # Composition

    def start_engine(self):
        self.engine.start()

    def display_info(self):
        super().display_info()
        print(f'This car has {self.doors} doors.')

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

def main():
    vehicles = [
        Car('Toyota', 'Corolla', 4, 'V6'),
        Motorcycle('Harley-Davidson', 'Street 750', 'Cruiser', 'V-Twin')
    ]

    for vehicle in vehicles:
        vehicle.display_info()
        vehicle.start_engine()
        print()

if __name__ == '__main__':
    main()
