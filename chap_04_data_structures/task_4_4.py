# -*- coding: utf-8 -*-
"""
Task 4.4

The v_lans_list is a list of VLANs collected from all network devices,
so there are duplicate VLAN numbers in the list.

From the v_lans_list, you need to obtain a new list of unique VLAN numbers,
sorted in ascending order. To obtain the final list,
you cannot manually delete specific VLANs.

Write the list of unique VLAN numbers into the result_vlans variable.
(This is the variable that will be tested.)

Output the obtained result_vlans list to the standard output stream (stdout)
using print.

Limitation: All tasks must be completed using only the topics covered.

Warning: In section 4, tests can easily be "cheated" by making the desired output,
without obtaining results from the original data using Python.
This does not mean that the task is done correctly; it's just difficult to verify the result at this stage.
"""

v_lans_list = [10, 30, 20, 100, 1, 2, 10, 4, 30, 3, 10]

result_vlans = sorted(set(v_lans_list))
print(result_vlans)
