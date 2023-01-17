import csv

with open("names.csv", "r") as f:
  csv_reader = csv.DictReader(f, delimiter=",")
  # next(csv_reader)
  for line in csv_reader:
    print(line)