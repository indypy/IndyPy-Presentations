import csv

with open("banklist.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
