# -*- coding: utf-8 -*-
"""
Assignment 6.2a

Make a copy of the script from assignment 6.2.

Add validation for the entered ip_address.
An address is considered correctly specified if it:
   - consists of 4 numbers (not letters or other characters)
   - numbers are separated by dots
   - each number is in the range from 0 to 255

If the address is specified incorrectly, display the message: 'Incorrect ip_address address'

The message "Incorrect ip_address address" should be displayed only once,
even if several points above are not met.

Constraint: All tasks should be performed using only the topics covered so far.
"""

ip_address = input('Enter ip_address: ')
octets = ip_address.split('.')
flag = True

if len(octets) == 4:
    for octet in octets:
        if not (octet.isdigit() and int(octet) >= 0 and int(octet) <= 255):
            flag = False
            break
else:
    flag = False

if not (flag):
    print('Incorrect ip_address address')
else:
    first_octet = int(octets[0])
    if first_octet <= 223 and first_octet > 0:
        print('unicast')
    elif first_octet <= 239 and first_octet >= 224:
        print('multicast')
    elif ip_address == '255.255.255.255':
        print('local broadcast')
    elif ip_address == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
