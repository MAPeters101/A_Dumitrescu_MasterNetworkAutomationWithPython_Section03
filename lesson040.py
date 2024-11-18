
with open('devices.txt', 'r') as f:
    devices = f.read().splitlines()
    #print(devices)

mylist = list()
for item in devices[1:]:
    tmp = item.split(':')
    # print(tmp)
    tmp = [el.strip() for el in tmp]
    # row = []
    # for el in tmp:
    #     row.append(el.strip())
    mylist.append(tmp)

print(mylist)