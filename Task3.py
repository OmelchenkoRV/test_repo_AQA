# Subtask1
# i = 0
# acc=[]
# while i <= 10:
#     acc.append(i)
#     i += 1
# print(*acc, sep=', ')
# Subtask2
# j = 20
# ac = []
# while j > 0:
#     ac.append(j)
#     j -= 1
# print(*ac, sep=', ')
# Subtask3
num = int(input())
times = 0
while num % 2 == 0:
      num /= 2
      times += 1
print(times)
