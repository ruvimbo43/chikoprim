#PRIMROSE MUGOMBI 
#R257042H
#assignment 2
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"Vehicle: {self.make} {self.model}"


class Car(Vehicle):
    def info(self):  # override base method
        return f"Car    : {self.make} {self.model} "


class Bike(Vehicle):
    def info(self):  # override base method
        return f"Bike   : {self.make} {self.model} "


v = Vehicle("Generic", "Base")
c = Car("Nissan", "NP200")
b = Bike("honda", "Prime")

print(v.info())  
print(c.info())  
print(b.info())


#Question 2
import math

class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, Length):
        self.width = width
        self.Length = Length
    
    def area(self):
        return self.width * self.Length

# polymorphism
def total_area(shapes):
    return sum(shape.area() for shape in shapes)


shapes = [
    Circle(10),        
    Rectangle(7, 8),   
    Circle(1.5) 
]

print("Total area of shapes:", total_area(shapes))


#  QUESTION 3 

class Shape:
    def __init__(self, name="Generic Shape"):
        self.name = name
        print(f"Initializing Shape: {self.name}")

    def calculate_area(self):
        print("Base Shape has no defined area.")
        return 0


class Rectangle(Shape):
    
    def __init__(self, width, height):
        super().__init__(name="Rectangle")
        self.width = width
        self.height = height

    def calculate_area(self):
        super().__init__(name="Rectangle (re-init in area)")
        
        area = self.width * self.height
        print(f"Area of {self.name}: {area}")
        return area
        
#Question 4

def process_sound(sound_object):
    print("Processing sound...")
    sound_object.make_sound()



class Dog:
    def make_sound(self):
        print("bark! bark!")


class Cat:
    def make_sound(self):
        print("Meow! Meow!")



dog = Dog()
cat = Cat()

process_sound(dog)  
process_sound(cat)  

# Question 5
from abc import ABC, abstractmethod


class FileHandler(ABC):
    @abstractmethod
    def read(self, filename):
        pass

    @abstractmethod
    def write(self, filename, data):
        pass



class TextFileHandler(FileHandler):
    def read(self, filename):
        with open(filename, "r", encoding="utf-8") as f:
            data = f.read()
        print(f"[TextFileHandler] Reading from {filename}")
        return data

    def write(self, filename, data):
        with open(filename, "w", encoding="utf-8") as f:
            f.write(data)
        print(f"[TextFileHandler] Writing to {filename}")



class BinaryFileHandler(FileHandler):
    def read(self, filename):
        with open(filename, "rb") as f:
            data = f.read()
        print(f"[BinaryFileHandler] Reading from {filename}")
        return data

    def write(self, filename, data):
        with open(filename, "wb") as f:
            f.write(data)
        print(f"[BinaryFileHandler] Writing to {filename}")


if __name__ == "__main__":
    text_handler = TextFileHandler()
    binary_handler = BinaryFileHandler()

    
    text_handler.write("example.txt", "Hello, Abstract Base Classes!")
    print(text_handler.read("example.txt"))

    
    binary_handler.write("example.bin", b"\x48\x65\x6C\x6C\x6F")
    print(binary_handler.read("example.bin"))





