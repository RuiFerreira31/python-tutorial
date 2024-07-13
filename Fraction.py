class Fraction:
    def __init__(self,nr, dr=1):
        if dr < 0:
            nr = -nr
            dr = -dr

        self.nr = nr
        self.dr = dr
        self.__reduce()

    def show(self):
        print(str(self.nr) + '/' + str(self.dr))

    def multiply(self, f2):
        if isinstance(f2, Fraction):
            fx = Fraction(self.nr * f2.nr, self.dr * f2.dr)
            self.__reduce()
            return fx
        elif isinstance(f2, int):
            fx = Fraction(self.nr * f2, self.dr)
            self.__reduce()
            return fx
        else:
            raise TypeError("Unsupported operand type for multiply")

    def add(self, f2):
        if isinstance(f2, Fraction):
            fx = Fraction(self.nr * f2.dr + f2.nr * self.dr, self.dr*f2.dr)
            self.__reduce()
            return fx
        elif isinstance(f2, int):
            fx = Fraction(self.nr * 1 + f2 * self.dr, self.dr*1)
            self.__reduce()
            return fx
        else:
            raise TypeError("Unsupported operand type for multiply")

    @staticmethod
    def hcf(x,y):
        x=abs(x)
        y=abs(y)
        smaller = y if x>y else x
        s = smaller
        while s>0:
            if x%s==0 and y%s==0:
                break
            s-=1
        return s


    def __reduce(self):
        common_factor = Fraction.hcf(self.nr,self.dr)
        return print(str(self.nr/common_factor) + '/' + str(self.dr/common_factor))




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


