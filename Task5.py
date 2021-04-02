sttr = 'We are not what we should be! We are not what we need to be. But at least we are not what we used to be (Football Coach)'
# count = 0
# for i in range(len(sttr)):
#     if sttr[i] == " ":
#         count += 1
# print(count + 1)

sttr = sttr.split(' ')
for i in range(len(sttr)):
    sttr[i] = sttr[i].strip('!.()')
print(sttr)

sttr.sort(key=str.lower)
print(*sttr)


def analys(your_list, your_dict):
    for i in your_list:
        if i in your_dict:
            your_dict[i] += 1
        else:
            your_dict[i] = 1


dct = {}

analys(sttr, dct)

for item in sorted(dct):
    print((item, dct[item]))

