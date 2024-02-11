# Explain Inheritance in Python with an example? What is init? Or What
# Is A Constructor In Python?



# Inheritance in Python allows a class to inherit attributes and methods from another class.
# The __init__ method is a constructor in Python that gets called when an object is created.

class Vehicle:
    def __init__(self, name):
        self.name = name

class Car(Vehicle):
    def sound(self):
        return (f"{self.name} makes the sound Vroom Vroom...")

car = Car("Car")
print("Base class attribute:", car.name)  # Accessing attribute from the base class
print(car.sound())  # Calling a method specific to the derived class
