class Book:
    def __init__(self, isbn, title, author, publisher, pages, price, copies):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publisher = publisher
        self.pages = pages
        self.price = price
        self.copies = copies

    def display(self):
        print("ISBN: " + self.isbn + ", Title: " + self.title +", Author: " + self.author + ", Publisher: "
              + self.publisher + ", Pages: " + str(self.pages) + ", Price: " + str(self.price) + ", Copies: " + str(self.copies))

    def in_stock(self):
        if self.copies > 0:
            return True
        else:
            return False

    def sell(self):
        self.copies -= 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if price < 50:
            raise ValueError("Price cannot be less than 50")
        elif price>1000:
            raise ValueError("Price cannot be higher than 1000")
        self._price = price


book1 = Book('957-4-36-547417-1', 'Learn Physics','Stephen', 'CBC', 350, 500,10)
book2 = Book('652-6-86-748413-3', 'Learn Chemistry','Jack', 'CBC', 400, 50,20)
book3 = Book('957-7-39-347216-2', 'Learn Maths','John', 'XYZ', 500, 300,5)
book4 = Book('957-7-39-347216-2', 'Learn Biology','Jack', 'XYZ', 400, 200,6)

book1.display()
# book2.display()
# book3.display()
# book4.display()

book1.in_stock()
book1.sell()
# book1.display()

books = [book1,book2,book3,book4]
booksByJack = []

for book in books:
    # book.display()
    if book.author == 'Jack':
        booksByJack.append(book.title)

print(booksByJack)


