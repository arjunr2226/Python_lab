import csv

with open("names.csv", "r") as f:
  csv_reader = csv.reader(f)
  next(csv_reader)
  total = 0
  for line in csv_reader:
    total = total +int(line[0]) + int(line[2])
  print(total)