
l = ['aswin', 'aravind', 'ayash', 'rais', 'amal']
di = dict()

# for i in l:
#   di[i] = i.count('a')
# print(di)
    
for i in l:
  di[i] = i.count('a')
print(dict(sorted(di.items(), key = lambda t:t[1], reverse = True)))







# print(Counter(l))