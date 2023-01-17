class Publisher:
  def __init__(self, name):
    self.name = name

class Book(Publisher):
  def __init__(self, name, title, author):
    Publisher.__init__(self, name)
    self.title = title
    self.author = author

class Python(Book):
  def __init__(self, name, title, author, price, no_pages):
    Book.__init__(self, name, title, author)
    self.price = price
    self.no_pages = no_pages
  # def display(self):
    # print(self.name, self.title, self.author, self.price, self.no_pages)

b = Python(input("ENTER PUBLISHER NAME: "), input("ENTER TITLE: "), input("ENTER AUTHOR NAME: "), int(input("ENTER PRICE: ")), int(input("ENTER NO OF PAGES: ")))

# b = Python('DC Book', 'Python programming', 'Bot', 2999, 1000)
# Python.display(b)
print(vars(b))