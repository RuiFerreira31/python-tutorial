class Product:
    def __init__(self,x,y):
        self._x = x
        self._y = y

    def display(self):
        print(self._x,self._y)

    @property
    def value(self):
        return self._x

    @value.setter
    def value(self,val):
        self._x = val

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self,val):
        self._y = val

p = Product(12,24)

print(p.value)
print(p.value + 2)
p.value = 2
print(p.value)


print(p.y)
print(p.y + 2)
p.y = 2
print(p.y)


