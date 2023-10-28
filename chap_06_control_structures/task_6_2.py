# -*- coding: utf-8 -*-
"""
Assignment 6.2

Prompt the user to enter an IP address in the format 10.0.1.1
Depending on the type of address (described below), output to the standard output stream:
   'unicast' - if the first byte is in the range 1-223
   'multicast' - if the first byte is in the range 224-239
   'local broadcast' - if the IP address is 255.255.255.255
   'unassigned' - if the IP address is 0.0.0.0
   'unused' - in all other cases

Restriction: All tasks should be performed using only the topics covered.

"""

user_ip_address = input('Enter IP: ')
first_byte_ip = int(user_ip_address.split('.')[0])
if first_byte_ip <= 223 and first_byte_ip > 0:
    print('unicast')
elif first_byte_ip <= 239 and first_byte_ip >= 224:
    print('multicast')
elif user_ip_address == '255.255.255.255':
    print('local broadcast')
elif user_ip_address == '0.0.0.0':
    print('unassigned')
else:
    print('unused')
