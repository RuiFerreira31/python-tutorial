class SalesPerson:
    names = []
    total_revenue = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.sales_amount = 0
        SalesPerson.names.append(name)

    def make_sale(self, money):
        self.sales_amount += money
        SalesPerson.total_revenue += money

    def show(self):
        print(self.name, self.age, self.sales_amount)


s1 = SalesPerson('Bob', 25)
print(SalesPerson.names)
s2 = SalesPerson('Ted', 22)
print(SalesPerson.names)
s3 = SalesPerson('Jack', 27)
print(SalesPerson.names)

s1.make_sale(1000)
print(SalesPerson.total_revenue)
s1.make_sale(1200)
print(SalesPerson.total_revenue)
s2.make_sale(5000)
print(SalesPerson.total_revenue)
s3.make_sale(3000)
print(SalesPerson.total_revenue)
s3.make_sale(8000)
print(SalesPerson.total_revenue)

s1.show()
s2.show()
s3.show()