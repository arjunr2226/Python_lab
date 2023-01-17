sqr = lambda x : x**2
rect = lambda l, b: l*b
tri = lambda b, h: b*h*0.5
a = int(input("ENTER THE SIDES: "))
print("Area of square: ", sqr(a))
l = int(input("ENTER THE SIDES: "))
b= int(input("ENTER THE SIDES: "))
print("Area of rectangle: ", rect(l, b))
b = int(input("ENTER THE SIDES: "))
h = int(input("ENTER THE SIDES: "))
print("Area of triangle: ", tri(b, h))
