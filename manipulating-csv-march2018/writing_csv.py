import csv

with open("demo.csv", "w") as f:
    writer = csv.writer(f)
    writer.writerow(('Col 1', 'Col 2', 'Col 3'))
    for i in range(3):
        row = (
            i + 1,
            'Hello World {}'.format(i),
            'IndyPy Rocks'
        )
        writer.writerow(row)
