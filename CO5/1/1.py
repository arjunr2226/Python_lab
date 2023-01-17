with open("file.txt", "r") as f:
  f = f.readlines()
  l =[]
  for line in f:
    l.append(line.strip())
  print(l)