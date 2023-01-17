with open("file.txt", "r") as f:
  with open("file1.txt", "w") as f1:
    count = 1
    for line in f:
        if count%2 != 0:
          f1.write(line)  
        count += 1
      