import math as m


class Shape:
    def __init__(self, name):
        self.name = name

    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius

    def area(self):
        return m.pi * self.radius**2


class Rectangle(Shape):
    def __init__(self, name, width, height):
        super().__init__(name)
        self.width = width
        self.height = height

    def area(self):
        return self.height * self.width


c = Circle("MyCircle", 5)
print(c.name)
print(c.area())

r = Rectangle("MyRectangle", 20, 4)
print(r.name)
print(r.area())
