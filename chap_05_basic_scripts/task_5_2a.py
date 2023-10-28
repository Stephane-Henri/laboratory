# -*- coding: utf-8 -*-
"""
Exercise 5.2a

Everything as in task 5.2, but if the user enters a host address instead of a network address,
the host address should be converted to a network address and the network address and mask should be displayed, as in task 5.2.

Network address examples (all host bits are set to zero):
* 10.0.1.0/24
* 190.1.0.0/16

Host address examples:
* 10.0.1.1/24 - host from the network 10.0.1.0/24
* 10.0.5.195/28 - host from the network 10.0.5.192/28

If the user enters the address 10.0.1.1/24, the output should be as follows:

host:
10        0         1         0
00001010  00000000  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Test the script on different host/mask combinations, for example:
    10.0.5.195/28, 10.0.1.1/24

The network and mask output should be organized in the same way as in the example:
- in columns
- 10 characters wide (add two spaces in binary format to separate octets)

Hint:
You have a host address in binary format and a 28-bit mask. The network address is the first 28 bits of the host address plus four zeros.
For example, the host address 10.1.1.195/28 in binary format will be
bin_host_ip = "00001010 00000001 00000001 11000011"

And the network address will be the first 28 characters of bin_host_ip plus 0000 (4 because there can be a total of 32 bits in the address, and 32 - 28 = 4).
00001010000000010000000111000000

Limitation: You should complete all tasks using only the topics covered.
"""

user_input_ip = input('Enter the host IP: ')
host_ip = user_input_ip.split('/')[0]
subnet_mask = int(user_input_ip.split('/')[1])
host_ip_parts = host_ip.split('.')
host_ip_part_0_bin = bin(int(host_ip_parts[0]))[2:].zfill(8)
host_ip_part_1_bin = bin(int(host_ip_parts[1]))[2:].zfill(8)
host_ip_part_2_bin = bin(int(host_ip_parts[2]))[2:].zfill(8)
host_ip_part_3_bin = bin(int(host_ip_parts[3]))[2:].zfill(8)
host_ip_bin = host_ip_part_0_bin + host_ip_part_1_bin + host_ip_part_2_bin + host_ip_part_3_bin
network_ip = host_ip_bin[:subnet_mask] + "0" * (32 - subnet_mask)
network_ip = str(int(network_ip[0:8], 2)) + ' ' + str(int(network_ip[8:16], 2)) + ' ' + str(int(network_ip[16:24], 2)) + ' ' + str(int(network_ip[24:32], 2))
network_ip_parts = network_ip.split()
mask_calc = "1" * subnet_mask + "0" * (32 - subnet_mask)

template = """
  host:
  {2:<8}  {3:<8}  {4:<8}  {5:<8}
  {2:08b}  {3:08b}  {4:08b}  {5:08b}

  Mask:
  /{1}
  {6:<8}  {7:<8}  {8:<8}  {9:<8}
  {6:08b}  {7:08b}  {8:08b}  {9:08b}
"""

print(template.format(network_ip, subnet_mask, int(network_ip_parts[0]), int(network_ip_parts[1]), int(network_ip_parts[2]), int(network_ip_parts[3]), int(mask_calc[0:8], 2), int(mask_calc[8:16], 2), int(mask_calc[16:24], 2), int(mask_calc[24:32], 2))
