class Shape:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    def calculate_area(self):
        print("you are calculating area of a shape")

class Rectangle(Shape):
    def __init(self, width, height):
        super().__init__()


    def calculate_area(self):
        return self.width * self.height
    
rectangle = Rectangle(5, 10)
print(rectangle.calculate_area())