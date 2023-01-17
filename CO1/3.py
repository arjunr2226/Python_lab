l1 = [-1, 2, -3, -5, 3, 6]

l1 = [x for x in l1 if x>0]
print(l1)

l1 = [x*x for x in l1]
print(l1)

s = "arjun"
l = [x for x in s if x in 'aeiou']
print(l)

l = [ord(x) for x in l]
print(l)