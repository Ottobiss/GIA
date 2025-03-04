from ipaddress import *

count = 0

def counter(ip):
    ip2 = bin(int(ip))[2:].zfill(32)

    return ip2[16:24].count('0') > ip2[24:].count('0')

for bin4 in range(0, 256):
    ip1 = ip_address(f'246.81.65.{bin4}')

    network = ip_network(f'{ip1}/255.255.255.224', False)

    if network[0] != ip1 != network[-1] and all(counter(x) for x in network.hosts()):
        count += 1

print(count)

