import math

class Shape:
    def get_area(self):
        raise NotImplementedError("Subclasses must implement get_area method")

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def set_radius(self, radius):
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return 0.5 * self.base * self.height

class Polygon(Shape):
    def __init__(self, sides, side_length):
        self.sides = sides
        self.side_length = side_length

    def get_area(self):
        # Implement area calculation for polygon
        # For simplicity, let's assume all polygons are regular
        return 0.25 * self.sides * self.side_length ** 2 / math.tan(math.pi / self.sides)

if __name__ == "__main__":
    # Dummy values
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    triangle = Triangle(3, 4)
    polygon = Polygon(6, 5)

    print("Area of the circle:", circle.get_area())
    print("Area of the rectangle:", rectangle.get_area())
    print("Area of the triangle:", triangle.get_area())
    print("Area of the polygon:", polygon.get_area())
