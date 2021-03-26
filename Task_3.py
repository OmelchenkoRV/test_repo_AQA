a = ['Sed', 'ut', 'perspiciatis', 'unde', 'omnis', 'iste', 'natus', 'error', 'sit']

print(a[-3])

print(a[1][0])

print(a[-1][-1])

a.append('world')
print(a)

middle = int(len(a) / 2)
a.insert(middle, 'new')
print(a)

a.pop(0)
print(a)

a.remove('world')
print(a)
