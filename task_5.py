import csv

with open('convertcsv.csv') as csvfile:
    reader = csv.reader(csvfile)
    max_value = 0
    max_salary = []
    max_salaries = dict()
    for row in reader:

        if float(row[-1]) > max_value:
            max_value = float(row[-1])

        if row[3] not in max_salary:
            max_salary.append(row[3])
            max_salaries[row[3]] = row[1], row[2], row[-1]
        if row[3] in max_salaries and float(row[-1]) > float(max_salaries[row[3]][-1]):
            max_salaries[row[3]] = row[1], row[2], row[-1]

print(len(max_salaries))
print(max_value)
print(max_salaries)
