# © 2024 
# All rights reserved.

# This code is part of a teaching example for object-oriented programming concepts.

# Bonus: Magic methods

class Vehicle:
    def __new__(cls, make, model):
        """
        Create a new instance of Vehicle.
        """
        print("Creating instance")
        instance = super().__new__(cls)
        return instance

    def __init__(self, make, model):
        """
        Initialize the Vehicle instance.
        
        :param make: The make of the vehicle.
        :param model: The model of the vehicle.
        """
        print("Initializing instance")
        self.make = make
        self.model = model
        self.features = []

    def display_info(self):
        """
        Display the vehicle's information.
        """
        print(f'Vehicle: {self.make} {self.model}')

    def __str__(self):
        """
        Return a human-readable string representation of the vehicle.
        """
        return f'{self.make} {self.model}'

    def __repr__(self):
        """
        Return an unambiguous string representation of the vehicle.
        """
        return f'Vehicle(make={self.make}, model={self.model})'

    def __eq__(self, other):
        """
        Compare two Vehicle instances for equality.
        
        :param other: Another Vehicle instance.
        :return: True if both vehicles have the same make and model, False otherwise.
        """
        if isinstance(other, Vehicle):
            return self.make == other.make and self.model == other.model
        return False

    def __del__(self):
        """
        Destructor method called when the instance is about to be destroyed.
        """
        print(f'Vehicle {self.make} {self.model} is being destroyed')

    def __lt__(self, other):
        """
        Compare two Vehicle instances to determine if one is less than the other.
        
        :param other: Another Vehicle instance.
        :return: True if this vehicle is less than the other vehicle, False otherwise.
        """
        if isinstance(other, Vehicle):
            return (self.make, self.model) < (other.make, other.model)
        return NotImplemented

    def __len__(self):
        """
        Return the number of features in the vehicle.
        """
        return len(self.features)

    def __getitem__(self, index):
        """
        Get a feature by index.
        
        :param index: Index of the feature.
        :return: The feature at the specified index.
        :raises IndexError: If the index is out of range.
        """
        try:
            return self.features[index]
        except IndexError:
            print("Index out of range")
            raise

    def __setitem__(self, index, value):
        """
        Set a feature at a specific index.
        
        :param index: Index where the feature should be set.
        :param value: The feature to set.
        :raises IndexError: If the index is out of range.
        """
        try:
            self.features[index] = value
        except IndexError:
            print("Index out of range")
            raise

    def __iter__(self):
        """
        Return an iterator for the features.
        """
        return iter(self.features)

    def __next__(self):
        """
        Return the next feature in the iteration.
        """
        return next(self.features)

    def __call__(self, *args, **kwargs):
        """
        Allow the Vehicle instance to be called as a function.
        
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        """
        print(f'Calling Vehicle instance with args: {args} and kwargs: {kwargs}')

def main():
    car = Vehicle('Toyota', 'Corolla')
    car.display_info()
    print(str(car))  # Using __str__
    print(repr(car))  # Using __repr__

    another_car = Vehicle('Toyota', 'Corolla')
    print(car == another_car)  # Using __eq__

    third_car = Vehicle('Honda', 'Civic')
    print(car < third_car)  # Using __lt__

    car.features.append('Air Conditioning')
    car.features.append('Power Steering')
    print(len(car))  # Using __len__
    try:
        print(car[0])  # Using __getitem__
        car[1] = 'Sunroof'  # Using __setitem__
    except IndexError as e:
        print(e)
    print(car.features)

    for feature in car:
        print(feature)  # Using __iter__

    car('start', 'drive', speed=60)  # Using __call__

    del car  # Using __del__

if __name__ == '__main__':
    main()
