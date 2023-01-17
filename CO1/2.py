l = []
for i in range(2022, 3000):
  if (i%4==0 and i%100!=0) or (i%400==0 and i%100==0):
    l.append(i) 
print(l)