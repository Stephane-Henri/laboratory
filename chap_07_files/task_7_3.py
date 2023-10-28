# -*- coding: utf-8 -*-
"""
Assignment 7.3

The script should process entries in the CAM_table.txt file. Each line
containing a MAC address should be processed to display a table on the
standard output in the following format:

100      01bb.c580.7000      Gi0/1
200      0a4b.c380.7c00      Gi0/2
300      a2ab.c5a0.700e      Gi0/3
10       0a1b.1c80.7000      Gi0/4
500      02b1.3c80.7b00      Gi0/5
200      1a4b.c580.7000      Gi0/6
300      0a1b.5c80.70f0      Gi0/7
10       01ab.c5d0.70d0      Gi0/8
1000     0a4b.c380.7d00      Gi0/9

Limitation: All tasks should be done using only the topics covered.

"""

cam_file = 'CAM_table.txt'
with open(cam_file) as file:
    for line in file:
        line_items = line.split()
        for element in line_items:
            if len(element.split('.')) == 3:
                print('{:<10} {:<20} {:<15}'.format(line_items[0], line_items[1], line_items[3])
