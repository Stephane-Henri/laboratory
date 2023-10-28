# -*- coding: utf-8 -*-
"""
Task 7.1

Process lines from the ospf.txt file and output information for each line in the following format to the standard output:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Constraint: All tasks must be completed using only the topics covered so far.

"""

data_name1, data_name2, data_name3, data_name4, data_name5 = [
    "Prefix", "AD/Metric", "Next-Hop", "Last update", "Outbound Interface"]

with open("ospf.txt") as f:
    for line in f:
        line = line.replace(' via', '').replace(',', '')
        line_to_list = line.split()
        data0, data1, data2, data3, data4, data5 = line_to_list

        print("{:22} {:22}".format(data_name1, data1))
        print("{:22} {:22}".format(data_name2, data2.strip('[]')))
        print("{:22} {:22}".format(data_name3, data3))
        print("{:22} {:22}".format(data_name4, data4))
        print("{:22} {:22}".format(data_name5, data5))
        print()
