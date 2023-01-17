d1 = {1: 'arjun', 2: 'rais'}
d2 = { 3: 'amal', 4: 'aravind'}

for i in d2.keys():
  d1[i] = d2.get(i)
print(d1)