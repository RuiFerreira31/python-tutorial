class Rectangle():
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    @property
    def diagonal(self):
        return (self.length * self.length + self.breadth * self.breadth) ** 0.5

    def area(self):
        return self.breadth * self.length

    def perimeter(self):
        return 2 * (self.length + self.breadth)


r = Rectangle(5, 5)

print(r.area())
print(r.perimeter())
print(r.diagonal)
r.length = 50
print(r.diagonal)