import csv

with open('devices.txt') as f:
    reader = csv.reader(f, delimiter=':')
    mylist = []
    for row in reader:
        #print(row)
        row = [el.strip() for el in row]
        #print(row)
        mylist.append(row)

mylist = mylist[1:]
print(mylist)


