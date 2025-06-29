#   ***     Super() function Exercise      ***

class Shape:
    def __init__(self, color, is_filled):
        self.color = color
        self.is_filled = is_filled

    def describe(self):
        print(f"Its a {self.color} and {'filled' if self.is_filled else 'not filled'}")


class Circle(Shape):
    def __init__(self, color, is_filled, radius):
        super().__init__(color, is_filled)
        self.radius = radius

    def describe(self):
        super().describe()
        print(f"Area of circle is {3.14 * (self.radius * self.radius)}cm^")


class Square(Shape):
    def __init__(self, color, is_filled, width):
        super().__init__(color, is_filled)
        self.width = width


class Rectangle(Shape):
    def __init__(self, color, is_filled, width, length):
        super().__init__(color, is_filled)
        self.width = width
        self.length = length


circle = Circle(color="red", is_filled=True, radius=2)
square = Square(color="Green", is_filled=False, width=3)
rect = Rectangle(color="Orange", is_filled=True, width=5, length=10)

circle.describe()
