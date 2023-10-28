# -*- coding: utf-8 -*-
"""
Task 4.1

Using the prepared string nat_ip, create a new string in which the interface name
is changed from FastEthernet to GigabitEthernet.
Print the resulting new string to the standard output (stdout) using print.

Constraint: All tasks must be performed using only the topics covered.

Warning: In section 4, tests can be easily cheated by making the desired output
without obtaining results from the source data using Python.
This does not mean that the task is done correctly; it is just difficult to check the result at this stage.
"""

new_gigabit_ip = "ip nat inside source list ACL interface FastEthernet0/1 overload"
new_gigabit_ip = new_gigabit_ip.replace('Fast', 'Gigabit')
print(new_gigabit_ip)
