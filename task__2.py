from math import sqrt
# def is_year_leap(year):
#     return year % 4 == 0 and year % 100 != 0 or year % 400 == 0
#
#
# print(is_year_leap(2001))
#
#
# def is_triangle_exist(a, b, c):
#     return a + b > c and a + c > b and b + c > a
#
#
# print(is_triangle_exist(1, 3, 5))
#
# TRIANGLE_TYPES = {1: "Equilateral", 2: "Isosceles", 3: "Versatile", 4: "Not a"}
#
#
# def type_of_triangle(a, b, c):
#     if a == b and b == c:
#         return TRIANGLE_TYPES[1]
#     elif a == b or b == c or a == c:
#         return TRIANGLE_TYPES[2]
#     elif a != b or b != c or a != c:
#         return TRIANGLE_TYPES[3]
#     else:
#         return TRIANGLE_TYPES[4]
#
#
# print(type_of_triangle(5, 6, 7))

x1 = float(input('Enter x1: '))
y1 = float(input('Enter x2: '))
x2 = float(input('Enter y1: '))
y2 = float(input('Enter y2: '))


def distance(x1, x2, y1, y2):
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


print(distance(x1, x2, y1, y2))