
with open('configuration.txt') as file:
    content = file.read()
    print(content)
print()
print(file.closed)
#file.seek(0)
#print(file.read())
print('-'*20)

with open('configuration.txt') as file:
    content = file.read()
    print(content)
    print()
    print(file.closed)
    print()
    file.seek(0)
    print(file.read())
print('-'*20)


