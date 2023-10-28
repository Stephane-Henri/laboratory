# -*- coding: utf-8 -*-
"""
Task 6.2b

Make a copy of the script from task 6.2a.

Extend the script: If the address was entered incorrectly, request the address again.

If the address is entered incorrectly, display the message: 'Incorrect ip_address address'
The message "Incorrect ip_address address" should be displayed only once,
even if the points above are not met.

Restriction: All tasks must be performed using only the topics covered.
"""
ip_address = input('Enter ip_address: ')
octets = ip_address.split('.')
is_address_valid = True

if len(octets) == 4:
    for octet in octets:
        if not (octet.isdigit() and int(octet) >= 0 and int(octet) <= 255):
            is_address_valid = False
            break
else:
    is_address_valid = False

while not is_address_valid:
    print('Incorrect ip_address address')
    ip_address = input('\nEnter ip_address: ')
    octets = ip_address.split('.')
    is_address_valid = True
    if len(octets) == 4:
        for octet in octets:
            if not (octet.isdigit() and int(octet) >= 0 and int(octet) <= 255):
                is_address_valid = False
                break
    else:
        is_address_valid = False

if is_address_valid:
    f_ip_address = int(octets[0])
    if f_ip_address > 0 and f_ip_address <= 223:
        print('unicast')
    elif f_ip_address >= 224 and f_ip_address <= 239:
        print('multicast')
    elif ip_address == '255.255.255.255':
        print('local broadcast')
    elif ip_address == '0.0.0.0':
        print('unassigned')
    else:
        print('unused')
