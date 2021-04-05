# def enter_number():
#     number = input('enter a number: ')
#     while type(number) != float:
#         try:
#             number = float(number)
#         except ValueError:
#             number = input('entered value is not a number. try once more: ')
#     print(number)
#
#
# enter_number()


def is_space():
    while True:
        txt = input('enter a string without space in the middle: ')
        if ' ' in txt.strip():
            print('Try once more')
        else:
            return txt


print(is_space())
