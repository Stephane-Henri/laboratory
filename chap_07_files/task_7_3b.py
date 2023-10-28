# -*- coding: utf-8 -*-
"""
Assignment 7.3b

Create a copy of the script from assignment 7.3a.

Revise the script:
- Request the user to input a VLAN number.
- Display information only for the specified VLAN.

Example of script operation:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Limitation: All tasks should be completed using only the topics covered.

"""

CAM_file = 'CAM_table.txt'
result = []
with open(CAM_file) as file:
    for line in file:
        list_data = line.split()
        if len(line.split('.')) == 3:
            vlan = list_data[0]
            mac = list_data[1]
            ports = list_data[3]
            result.append([int(vlan), mac, ports])

vlan_input = input('Enter VLAN number: ')
print(type(vlan_input))
for vlan, mac, ports in sorted(result):
    if int(vlan_input) == vlan:
        print('{:<10} {:<20} {:<15}'.format(vlan, mac, ports))
