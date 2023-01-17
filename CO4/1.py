class Rectangle:
  def __init__(self, l, b):
    self.l = l
    self.b = b
  def area(self):
    return self.l*self.b
  def per(self):
    peri = 2*(self.l + self.b)
    return peri
r1 = Rectangle(int(input("ENTER LENGTH FOR R1")), int(input("ENTER LENGTH FOR R1")))
r2 = Rectangle(int(input("ENTER LENGTH FOR R2")), int(input("ENTER LENGTH FOR R2")))
if(r1.area() > r2.area()):
  print("{0} is greater".format(r1.area()))
elif(r1.area() < r2.area()):
  print("{0} is greater".format(r2.area()))
else:
  print("Equal")
print("Perimeter :", r1.per())
