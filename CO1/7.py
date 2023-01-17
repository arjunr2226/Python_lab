l1 = [1, 3, 4, 32, 54, 43]
l2 = [6, 4, 3, 12, 34]

if len(l1)>len(l2):
  print("l1 is greater")
elif(len(l1)<len(l2)):
  print("l2 is greater")
else:
  print("same")

print(sum(l1)) 
print(set(l1).intersection(l2))