class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def display(self):
        print("I'm",self.name, "I am", self.age, "years old")
    def greet(self):
        if self.age <18:
            print("Hello little fella")
        else:
            print("Hello Friend")
            self.display()


p1 = Person('Eu',20)
p2 = Person('Tu',90)
p3 = Person('Tu',90)

p1.greet()
p1.display()

p2.greet()
p2.display()
