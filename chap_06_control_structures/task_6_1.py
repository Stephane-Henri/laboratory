# -*- coding: utf-8 -*-
"""
Assignment 6.1

The mac_list contains MAC addresses in the format XXXX:XXXX:XXXX. However, Cisco
equipment uses MAC addresses in the format XXXX.XXXX.XXXX.

Write code that transforms the MAC addresses into Cisco format and adds them to a new
list called result. Print the resulting list 'result' to the standard output (stdout)
using the print function.

Constraint: Perform all tasks using only the topics covered.

"""

mac_list = ["aabb:cc80:7000", "aabb:dd80:7340",
            "aabb:ee80:7000", "aabb:ff80:7000"]
result = []

for mac_address in mac_list:
    result.append(mac_address.replace(':', '.'))

print(result)
