# -*- coding: utf-8 -*-
"""
Task 6.3

A configuration generator for access ports is provided in the script.
Create a similar configuration generator for trunk ports.

In trunks, the situation is complicated because there can be many VLANs, and it is necessary to understand
what to do with them (add, delete, rewrite).

Therefore, for each port, there is a list, and the first (zero) element of the list indicates how to interpret
the VLAN numbers that follow.

Example of value and the corresponding command:
* ['add', '10', '20'] - the command switchport trunk allowed vlan add 10,20
* ['del', '17'] - the command switchport trunk allowed vlan remove 17
* ['only', '11', '30'] - the command switchport trunk allowed vlan 11,30

The task for ports 0/1, 0/2, 0/4, 0/5, 0/7:
- generate configuration based on the trunk_template template
- taking into account the keywords add, del, only

The code should not be tied to specific port numbers. In other words,
if there are other interface numbers in the trunk dictionary, the code should work.

For the data in the trunk_template dictionary, the output to the standard output should be as follows:
interface FastEthernet0/1
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,20
interface FastEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 11,30
interface FastEthernet0/4
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan remove 17
interface FastEthernet0/5
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan add 10,21
interface FastEthernet0/7
 switchport trunk encapsulation dot1q
 switchport mode trunk
 switchport trunk allowed vlan 30

Limitation: All tasks should be performed using only the topics covered.
Only trunk configuration commands should be output to the standard output, and access should be commented out.
"""

access_config = [
    "switchport mode access",
    "switchport access vlan",
    "spanning-tree portfast",
    "spanning-tree bpduguard enable",
]

trunk_config = [
    "switchport trunk encapsulation dot1q",
    "switchport mode trunk",
    "switchport trunk allowed vlan",
]

access_ports = {"0/12": "10", "0/14": "11", "0/16": "17", "0/17": "150"}
trunk_ports = {
    "0/1": ["add", "10", "20"],
    "0/2": ["only", "11", "30"],
    "0/4": ["del", "17"],
    "0/5": ["add", "10", "21"],
    "0/7": ["only", "30"],
}

for interface, vlan in access_ports.items():
    print("interface FastEthernet" + interface)
    for command in access_config:
        if command.endswith("access vlan"):
            print(f" {command} {vlan}")
        else:
            print(f" {command}")

print()

for interface, value in trunk_ports.items():
    print("interface FastEthernet" + interface)
    action = value[0]
    for command in trunk_config:
        if command.endswith('allowed vlan'):
            vlans = ",".join(value[1:])
            if action == "add":
                print(f" {command} add {vlans}")
            elif action == "only":
                print(f" {command} {vlans}")
            elif action == "del":
                print(f" {command} remove {vlans}")
        else:
            print(f" {command}")
