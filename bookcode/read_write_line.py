import os

f = open('top250books.txt', 'r+')
text = ''
while True:
    text = f.readline()
    text.rstrip()
    if text == '':
        break
    else:
        print(text)

print('-'*10)
f.seek(0)
print(f.readlines())
f.close()
