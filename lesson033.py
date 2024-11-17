
with open('devices.txt', 'r') as f:
    content = f.read().splitlines()
    #print(content)
    devices = list()
    for line in content[1:]:
        line = line.strip()
        devices.append(line.split(':'))

    print(devices)

    for device in devices:
        print(f'pinging {device[0]} at {device[1]}')


