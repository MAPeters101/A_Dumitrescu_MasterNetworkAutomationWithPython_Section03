
with open('myfile.txt', 'w') as f:
    f.write('Just a line.\n')
    f.write('Just a 2nd line.\n')


with open('myfile.txt', 'a') as f:
    f.write('Some text here.\n')
    f.write('Another text.')


with open('myfile.txt', 'r+') as f:
    f.seek(5)
    f.write('100')
    f.write('Line added with r+.\n')
    f.seek(10)
    print(f.read())

# with open('myfile11.txt', 'r+') as f:
#     f.write('Line added with r+.\n')

