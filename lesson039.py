import csv

with open('devices.txt', 'r') as f:
    reader = csv.reader(f, delimiter=':')
    devices = []
    for row in reader:
        devices.append(row)

    devices = devices[1:]
    my_devices = []
    for row in devices:
        new_row = []
        for item in row:
            new_row.append(item.strip())
        my_devices.append(new_row)

    print(my_devices)




