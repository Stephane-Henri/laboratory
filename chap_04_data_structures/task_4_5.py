# -*- coding: utf-8 -*-
"""
Task 4.5

Get the list of VLANs that are present in both cmd1 and cmd2 commands (intersection).

In this case, the result should be such a list: ['1', '3', '8']

Store the final list in the 'result' variable. (this variable will be tested)

Print the obtained 'result' list to the standard output (stdout) using print.

Constraint: All tasks should be performed using only the topics covered.

Warning: in section 4, tests can be easily "cheated" by making the correct output,
without obtaining the results from the source data using Python.
This does not mean that the task is done correctly, it is just difficult to check the result at this stage.
"""

input_command1 = "switchport trunk allowed vlan 1,2,3,5,8"
input_command2 = "switchport trunk allowed vlan 1,3,8,9"
vlan_set1 = set(input_command1.split()[-1].split(','))
vlan_set2 = set(input_command2.split()[-1].split(','))
result = sorted(list(vlan_set1 & vlan_set2))

print(result)
