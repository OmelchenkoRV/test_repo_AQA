num1 = input("Enter first value: ")
num2 = input("Enter second value: ")

try:
    res = int(float(num1)) + int(float(num2))
except:
    res = num1 + num2

print(res)
