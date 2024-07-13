class Employee:
    def __init__(self, name, password, salary):
        self._name = name
        self._password = password
        self._salary =salary

    @property
    def name(self):
        return self._name


    @property
    def password(self):
        return self._name

    @property
    def password(self):
        raise AttributeError('Password not readable')

    @password.setter
    def password(self, new_password):
        self._password = new_password

    @property
    def salary(self):
        return self._salary

    @salary.setter
    def salary(self, new_salary):
        self._salary = new_salary


e = Employee('Yo','Yo', 5000)

print(e)
print(e.name)
#print(e.password)
e.password = 'yup'
print(e.salary)
e.salary = 6000
print(e.salary)
