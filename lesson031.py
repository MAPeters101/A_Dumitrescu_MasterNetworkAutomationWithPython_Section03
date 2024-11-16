with open('configuration.txt') as f:
    content = f.read().splitlines()
    print(content)
print('#'*50)


with open('configuration.txt') as f:
    content = f.readlines()
    print(content)
print('#'*50)


with open('configuration.txt') as f:
    print(f.readline(), end='')
    print(f.readline())
print('#'*50)


with open('configuration.txt') as f:
    content = list(f)
    print(content)
print('#'*50)


with open('configuration.txt') as f:
    for line in f:
        print(line, end='')
print()
print('#'*50)







