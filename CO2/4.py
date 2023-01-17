import math as m
l = []
for i in range(1000, 10000):
  if m.sqrt(i) % 1 == 0 and len([x for x in str(i) if int(x)%2 == 1]) == 0:
    l.append(i)
print(l)