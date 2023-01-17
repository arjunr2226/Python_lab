n = int(input("ENTER NUMBER: "))
# print(n + (n + n*10) + ((n + n*10)+n*100) )
n2 = int("%s%s"%(n,n))
n3 = int("%s%s%s"%(n,n,n))

print(n + n2 + n3)