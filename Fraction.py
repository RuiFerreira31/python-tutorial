class Fraction:
    def __init__(self,nr, dr=1):
        if dr < 0:
            nr = -nr
            dr = -dr

        self.nr = nr
        self.dr = dr

    def show(self):
        print(str(self.nr) + '/' + str(self.dr))

    def multiply(self, f2):
        if isinstance(f2, Fraction):
            fx = Fraction(self.nr * f2.nr, self.dr * f2.dr)
            return fx
        elif isinstance(f2, int):
            fx = Fraction(self.nr * f2, self.dr)
            return fx
        else:
            raise TypeError("Unsupported operand type for multiply")

    def add(self, f2):
        if isinstance(f2, Fraction):
            fx = Fraction(self.nr * f2.dr + f2.nr * self.dr, self.dr*f2.dr)
            return fx
        elif isinstance(f2, int):
            fx = Fraction(self.nr * 1 + f2 * self.dr, self.dr*1)
            return fx
        else:
            raise TypeError("Unsupported operand type for multiply")


f1 = Fraction(2, 3)
f1.show()
f2 = Fraction(3, 4)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()

