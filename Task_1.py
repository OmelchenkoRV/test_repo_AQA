a = '12345'
print(a.isdigit())

b = 'Hello world !'
print(b.count(" "))

c = 'Let.mark.it.with.a.few.dots'
print(c.count("."))

d = 'Homework'
d1 = (d.center(100, ' '))
print(d1)
print(len(d1))

e = 'vary vary long string'
print(e.title())

print(e.endswith('ing'))

print(e.find('a'))

print(e.split(' '))

d1 = d1.lstrip()
d1 = d1.rstrip()
print(d1)
