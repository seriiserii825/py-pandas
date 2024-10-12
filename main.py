import csv
file_path = 'data.csv'

data = []

with open(file_path) as file:
    data = csv.reader(file)
    temperatures = []
    for index, row in enumerate(data):
        if index != 0:
            temperatures.append(int(row[1]))
print(temperatures)

