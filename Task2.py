text = input()
l = len(text) + 1
part_1 = text[0:l//2]
part_2 = text[l//2:]
new_text = part_2 + part_1
print(new_text)