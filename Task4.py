lst = [1, 5, 3, 11, 9, 10, 7]
# while lst:
#     print(lst)
#     lst.pop(0)
# print(lst)
#
# srng = 'this is string'
# for i in range(len(srng)):
#     print(srng[i:])
while lst:
    lst.remove(min(lst))
    print(lst)


def longest_sequence(s):
    lng, tmp = 1, 1

    for i in range(len(s) - 1, 0, -1):
        if s[i] == s[i - 1]:
            tmp += 1
        else:
            if tmp > lng:
                lng = tmp
            tmp = 1

    if tmp > lng:
        lng = tmp

    print('the longest same sequence are(is)', lng)


longest_sequence("12233344445555566666677777778888888899999999")



