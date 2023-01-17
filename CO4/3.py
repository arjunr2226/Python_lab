class Rectangle:
  def __init__(self, length, width):
    self.__length = length
    self.__width = width
    self.area = self.__length*self.__width
  def printArea(self):
    print("Area :", self.area)
  def __lt__(self, other):
    return self.area < other.area
r1 = Rectangle(1, 2)
r2 = Rectangle(1, 3)
print(r1<r2)