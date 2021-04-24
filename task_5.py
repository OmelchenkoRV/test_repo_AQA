import csv
import collections
import itertools
count = collections.Counter()
with open('convertcsv.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    max_value = 0
    max_salaries = []
    for row in reader:
        count[row['department']] += 1

        if float(row['dollar']) > max_value:
            max_value = float(row['dollar'])

        if row['department'] not in max_salaries:
            max_salaries.append(row)

    print('There are', len(count), 'departments')
    print('Max salary is ', max_value, '$')
    print(type(row))
    newlist = sorted(max_salaries, key=lambda k: k['department'], reverse=True)
    result = []

print(newlist)
