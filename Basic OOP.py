# © 2024 Meir Garada
# Email: MeirGarada@gmail.com
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Stage 1: Basic Object-Oriented Programming

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f'Vehicle: {self.make} {self.model}')

def main():
    car = Vehicle('Toyota', 'Corolla')
    car.display_info()

if __name__ == '__main__':
    main()
