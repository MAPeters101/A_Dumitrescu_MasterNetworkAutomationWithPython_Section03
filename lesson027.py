
#f = open('configuration.txt')
#f = open('configuration.txt', 'r')
f = open('configuration.txt', 'rt')
content = f.read()
print(content)
print(f.closed)
f.close()
print(f.closed)









