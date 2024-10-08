class Employee:

    allowed_domains = {'yahoo.com', 'gmail.com', 'outlook.com'}

    def __init__(self, name, email):
        self.name = name
        self.email = email

    def display(self):
        print(self.name, self.email)

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email):
        domain = new_email.split('@')[1]

        if domain not in Employee.allowed_domains:
            raise ValueError(f"{domain} not found in the list.")
        else:
            self._email = new_email


e1 = Employee('John', 'john@gmail.com')
e2 = Employee('Jack', 'jack@yahoo.com')
e3 = Employee('Jill', 'jill@outlook.com')
e4 = Employee('Ted', 'ted@yahoo.com')
e5 = Employee('Tim', 'tim@xmail.com')