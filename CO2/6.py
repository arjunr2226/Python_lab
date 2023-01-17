s = "aarjun"
# d = dict()
# for i in set(s):
#   d[i] = s.count(i)
# print(d)

for i in set(s):
  count = 0
  for j in s:
    if i == j:
      count += 1
  print(i, count)