# sttr = 'We are not what we should be! We are not what we need to be. But at least we are not what we used to be (Football Coach)'
# sttr = sttr.split(' ')
#
# acc = 0
# for itm in sttr:
#     if len(itm) % 2 == 1:
#         acc += 1
# print(acc)
#
# SEASONS = {'Winter': "1", 'Spring': "2", 'Summer': "3", 'Autumn': "4"}
#
# for item in SEASONS:
#     print(item, SEASONS[item])
#     print(type(SEASONS[item]))

# while True:
#     txt = input('enter a string without space: ')
#     if ' ' in txt:
#         print('Try once more')
#     else:
#         break

def hypotenusa (katet1, katet2):
    hyp = (katet1**2 + katet2**2)**0.5
    return hyp

print(hypotenusa(3,4))  

