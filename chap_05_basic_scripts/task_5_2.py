# -*- coding: utf-8 -*-
"""
Task 5.2

Request user input for network_ip_address in the format: 10.1.1.0/24

Then display information about the network and mask in the following format:

network_address:
10        1         1         0
00001010  00000001  00000001  00000000

mask_address:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Test the script with different network/mask combinations.

The output of the network and mask should be ordered in the same way as in the example:
- in columns
- column width 10 characters (in binary format, add two spaces between columns to separate octets)

Hint: You can get the binary format of the mask like this:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'

"""

network_ip_address = input('Enter network_ip_address: ')
# network_ip_address = '10.1.1.0/24'
network_address = network_ip_address.split('/')[0]
mask_address = int(network_ip_address.split('/')[1])
network_address_pieces = network_address.split('.')
mask_address_calc = "1" * mask_address + "0" * (32 - mask_address)

template_address = """
  network_address:
  {2:<8}  {3:<8}  {4:<8}  {5:<8}
  {2:08b}  {3:08b}  {4:08b}  {5:08b}

  mask_address:
  /{1}
  {6:<8}  {7:<8}  {8:<8}  {9:<8}
  {6:08b}  {7:08b}  {8:08b}  {9:08b}
"""

print(template_address.format(network_address, mask_address, int(network_address_pieces[0]), int(network_address_pieces[1]), int(network_address_pieces[2]), int(
    network_address_pieces[3]), int(mask_address_calc[0:8], 2), int(mask_address_calc[8:16], 2), int(mask_address_calc[16:24], 2), int(mask_address_calc[24:32], 2)))
