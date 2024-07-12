class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(self.name,self._age)

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, new_age):
        if 20<new_age<80:
            self._age = new_age
        else:
            raise ValueError('Age must be between 20 and 80')

if __name__ == '__main__':
    p = Person('Yo',30)
    p.display()
    p.age = 35
    p.display()

    #p1 = Person('Dev',100)