d = {1: 'arjun', 2: 'rais', 3: 'amal', 4: 'aravind'}
d1 = dict()
d2 = dict()
# for i in sorted(d.keys()):
#   d1[i] = d.get(i)
# print(d1)
# for i in sorted(d.keys(), reverse = True):
#   d2[i] = d.get(i)
# print(d2)

print(dict(sorted(d.items(), key = lambda t:t[0])))
print(dict(sorted(d.items(), key = lambda t:t[0], reverse= True)))