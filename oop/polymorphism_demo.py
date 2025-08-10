import math

class Shape:
    def __init__(self, length=0, width=0):
        self.length = length
        self.width = width

    def area(self):
        raise NotImplementedError("Derived classes need override this method")

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__(length, width)  # Initialize the base class


    def area(self):
        return self.length * self.width

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        super().__init__()  

    def area(self):
        return math.pi * (self.radius ** 2)