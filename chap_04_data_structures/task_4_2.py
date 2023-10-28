# -*- coding: utf-8 -*-
"""
Exercise 4.2

Transform the string in the variable mac_os from the format XXXX:XXXX:XXXX
to the format XXXX.XXXX.XXXX
Print the resulting new string to the standard output (stdout) using print.

Constraint: All tasks should be done using only the topics covered so far.

Warning: In section 4, the tests can easily be "cheated" by making the correct output,
without obtaining the results from the source data using Python.
This does not mean that the task is done correctly, it is just difficult to verify
the result at this stage.
"""

# Define the initial MAC address string
initial_mac = "AAAA:BBBB:CCCC"

# Transform the MAC address to the desired format
mac_address = initial_mac.replace(':', '.')

# Print the new MAC address
print(mac_address)
