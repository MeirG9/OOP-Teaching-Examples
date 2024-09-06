# © 2024 
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Stage 2: Inheritance

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Vehicle: {self.make} {self.model}')

# Car inherits from Vehicle
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)
        self.doors = doors

    def display_info(self):
        super().display_info()
        print(f'This car has {self.doors} doors.')

def main():
    car = Car('Toyota', 'Corolla', 4)
    car.display_info()

if __name__ == '__main__':
    main()
