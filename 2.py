class bankAccount:

    def __init__(self, name):
        self.name = name
    def set_details(self, name):
        self.name = name
        self.balance = 0


    def display(self):
        print("Name:",self.name, "| Balance:",self.balance)

    def withdraw(self, amount):
        if self.balance == 0:
            print("Account is empty")
        elif (self.balance - amount < 0):
            print("Not enought money")
        else:
            self.balance -= amount

    def deposit(self,amount):
        self.balance += amount


bancAccount1 = bankAccount()
bancAccount1.set_details("John")
bancAccount1.display()
bancAccount1.withdraw(5)
bancAccount1.deposit(10)
bancAccount1.withdraw(11)
bancAccount1.withdraw(5)
bancAccount1.display()

