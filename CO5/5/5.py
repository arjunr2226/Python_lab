import csv

fieldnames = ['id', 'name', 'age', 'course']
di = [{'id': '1', 'name': 'arjun', 'age': '21', 'course': 'mca'},{'id': '2', 'name': 'aswin', 'age': '21', 'course': 'mca'},
{'id': '3', 'name': 'ayash', 'age': '22', 'course': 'btech'},
 {'id': '4', 'name': 'amal', 'age': '19', 'course': 'mtech '}]

with open("names.csv", "w") as f:
  csv_writer = csv.DictWriter(f, fieldnames=fieldnames, delimiter=",")
  csv_writer.writeheader()
  csv_writer.writerows(di)

with open("names.csv", "r") as f:
  csv_reader = csv.DictReader(f)
  h = csv_reader.fieldnames
  print(h)
  for line in csv_reader:
    print(line)