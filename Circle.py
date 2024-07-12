import math


class Circle:

    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Unsupported negative type")

        self.radius = radius

    def area(self):
        return math.pi * self.radius**2

    @property
    def diameter(self):
        return self.radius*2

    @property
    def circumference (self):
        return math.pi*self.radius*2


c1 = Circle(-5)