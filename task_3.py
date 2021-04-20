
document_text = open('simple_text.txt', 'r')
text_string = (document_text.read()).split()
text_string.sort()
result = {i: text_string.count(i) for i in text_string}
document_text.close()
with open('output.txt', 'w') as fl:
    for k, v in result.items():
        fl.write('{}:{}\n'.format(k, v))
