import csv

with open("Demographic_Statistics_By_Zip_Code.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
