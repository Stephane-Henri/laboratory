# -*- coding: utf-8 -*-
"""
Task 7.2

Create a script that processes a configuration file config_sw1.txt.
The file name is passed as an argument to the script.

The script should output commands from the provided configuration file to the standard output, excluding lines that start with '!'.

The output should be without empty lines.

Limitation: All tasks should be performed using only the topics covered.

Example output:
$ python task_7_2.py config_sw1.txt
Current configuration: 2033 bytes
version 15.0
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
hostname sw1
interface Ethernet0/0
duplex auto
interface Ethernet0/1
switchport trunk encapsulation dot1q
switchport trunk allowed vlan 100
switchport mode trunk
duplex auto
spanning-tree portfast edge trunk
interface Ethernet0/2
duplex auto
interface Ethernet0/3
switchport trunk encapsulation dot1q
switchport trunk allowed vlan 100
duplex auto
switchport mode trunk
spanning-tree portfast edge trunk
...

"""

from sys import argv
file_name = argv[1]

with open(file_name) as file:
    for file_line in file:
        if file_line[0] != '!':
            print(file_line.rstrip())
