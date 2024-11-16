
# f = open('configuration.txt')
# content = f.read()
# print(content)
# print()
#
# f = open('configuration.txt')
# content = f.read(5)
# print(content)
# content = f.read(3)
# print(content)
# print()
# print(f.tell())
# f.seek(2)
# content = f.read(3)
# print(content)
# print()
#
# f.seek(0)
# content = f.read(3)
# print(content)


f = open('configuration.txt')
content = f.read()
print(content)
print('#'*50)
print(f.read())

print('#'*50)
f.seek(0)
print(f.read())


