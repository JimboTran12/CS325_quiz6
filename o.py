import math

class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length

    def get_area(self):
        return self.side_length ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

if __name__ == "__main__":
    # Dummy values
    circle = Circle(5)
    square = Square(4)
    rectangle = Rectangle(3, 6)

    print("Area of the circle:", circle.get_area())
    print("Area of the square:", square.get_area())
    print("Area of the rectangle:", rectangle.get_area())
