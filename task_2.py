file_template = open('template.txt')

for line in file_template:
    print(line.rstrip() + "!")
file_template.close()

with open('template.txt', 'r') as f:
    data = str(f.read())
with open('template1.txt', 'w') as f2:
    f2.write(data)

f = open('template.txt')
ints = []
try:
    for line in f:
        ints.append(int(line))
except ValueError:
    print('This is not a number.')
except Exception:
    print('Unknown error')
else:
    print('I did it.')
finally:
    f.close()
    print('File has been closed.')
