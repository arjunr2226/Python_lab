l1 = []
l2 = []
n1 = 20
n2 = 28

for i in range(1, n1+1):
  if n1%i == 0:
    l1.append(i)


for i in range(1, n2+1):
  if n2%i == 0:
    l2.append(i)

print("GCD IS", max(set(l1).intersection(l2)))