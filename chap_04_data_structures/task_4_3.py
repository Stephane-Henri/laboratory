# -*- coding: utf-8 -*-
"""
Task 4.3

Get the list of VLANs from the 'configuration' string:
['1', '3', '10', '20', '30', '100']

Write the resulting list to the 'result' variable.
(This specific variable will be tested)

Print the obtained list 'result' to the standard output (stdout) using print.
It is important to note that you need to get a list (data type), not a string that looks like the shown list.

Constraint: All tasks should be performed using only the topics covered.

Warning: In section 4, tests can easily be "cheated" by making the correct output without getting the results from the source data using Python. This does not mean that the task is done correctly; it's just difficult to verify the result at this stage.
"""

conf = "switchport trunk allowed vlan 1,3,10,20,30,100"

res = conf.split()[-1].split(',')

print(res)
