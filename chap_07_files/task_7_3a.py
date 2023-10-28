# -*- coding: utf-8 -*-
"""
Assignment 7.3a

Create a copy of the script from assignment 7.3.

Modify the script: Sort the output by VLAN number.

The desired output should look like this:
10       01ab.c5d0.70d0      Gi0/8
10       0a1b.1c80.7000      Gi0/4
100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
300      a2ab.c5a0.700e      Gi0/3
500      02b1.3c80.7b00      Gi0/5
1000     0a4b.c380.7d00      Gi0/9

Please note the VLAN 1000 - it should be displayed last.
You can achieve the correct sorting by making VLAN a number, not a string.

Hint: It's convenient to first create a list of lists like this and then sort it.

[[100, '01bb.c580.7000', 'Gi0/1'],
 [200, '0a4b.c380.7c00', 'Gi0/2'],
 [300, 'a2ab.c5a0.700e', 'Gi0/3'],
 [10, '0a1b.1c80.7000', 'Gi0/4'],
 [500, '02b1.3c80.7b00', 'Gi0/5'],
 [200, '1a4b.c580.7000', 'Gi0/6'],
 [300, '0a1b.5c80.70f0', 'Gi0/7'],
 [10, '01ab.c5d0.70d0', 'Gi0/8'],
 [1000, '0a4b.c380.7d00', 'Gi0/9']]

The sorting should be based on the first element (VLAN), and if the first element is the same, then sort by the second element. This is how the `sorted` function and the `sort` method work by default when sorting a list of lists.

Limitation: You must perform all tasks using only the topics covered so far.
"""

CAM_file = 'CAM_table.txt'
result = []
with open(CAM_file) as file:
    for line in file:
        list_table = line.split()
        if len(line.split('.')) == 3:
            vlan = list_table[0]
            mac = list_table[1]
            ports = list_table[3]
            result.append([int(vlan), mac, ports])
for vlan, mac, ports in sorted(result):
    print('{:<10} {:<20} {:<15}'.format(vlan, mac, ports))
