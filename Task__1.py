def get_value(*args):
    return list(set(args))[1]


print(get_value(1, 2, 3, 2, 4, 5, 3, 6, 3))
