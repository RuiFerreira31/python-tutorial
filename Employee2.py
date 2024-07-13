class Employee:

    domains = set()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        domain = email.split('@')[1]
        Employee.domains.add(domain)

    def display(self):
        print(self.name, self.email, Employee.domains)


e1 = Employee('John', 'john@gmail.com')
print(Employee.domains)
e2 = Employee('Jack', 'jack@yahoo.com')
print(Employee.domains)
e3 = Employee('Jill', 'jill@outlook.com')
print(Employee.domains)
e4 = Employee('Ted', 'ted@yahoo.com')
print(Employee.domains)
e5 = Employee('Tim', 'tim@gmail.com')
print(Employee.domains)
e6 = Employee('Mike', 'mike@yahoo.com')
print(Employee.domains)
