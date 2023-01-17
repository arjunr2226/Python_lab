n = int(input("ENTER THE SIZE: "))
l=[]
for i in range(n):
  l.append(int(input("ENTER THE NO: ")))
print(l)

for i in range(len(l)):
  if l[i] > 100:
    l[i] = 'over'
print(l)