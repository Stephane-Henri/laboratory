# -*- coding: utf-8 -*-
"""
Task 4.7

Convert the mac_address address in the mac_address string to a binary string of the following format:
'101010101010101010111011101110111100110011001100'

Output the resulting new string to the standard output (stdout) using print.

Limitation: All tasks should be performed using only the topics covered.

Warning: In section 4, tests can be easily "tricked" by making the correct output
without obtaining results from the source data using Python.
This does not mean that the task is done correctly, it's just difficult to verify the result at this stage.
"""

mac_address = "AAAA:BBBB:CCCC"
mac_address = mac_address.replace(':', '')
bin_result = bin(int(mac_address, 16))
mixed_bin_result = ''.join([bin_result[i] + bin_result[i + 1]
                           for i in range(2, len(bin_result), 2)])
print(mixed_bin_result)
