dict_s = {'title': 'cake', 'price': 1000, 'ingridients': ['eggs', 'flour', 'sugar']}
dict_s['description'] = 'tasty'
print(dict_s)

dict_s['price'] = dict_s['price'] + 100
print(dict_s)

dict_s['ingridients'].append('water')
print(dict_s)

print(len(dict_s['ingridients']))

del dict_s['description']
print(dict_s)