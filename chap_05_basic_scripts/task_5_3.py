# -*- coding: utf-8 -*-
"""
Assignment 5.3

The script should request the following information from the user:
* Interface mode (access/trunk)
* Interface number (type and number, e.g., Gi0/3)
* VLAN number(s) (for trunk mode, a list of VLAN numbers will be entered)

Depending on the selected mode, the corresponding access or trunk configuration (command templates
are located in the access_template and trunk_template lists) should be returned to the standard output.

The output should start with the line "interface_ihm" followed by the interface number, and then
the corresponding template with the VLAN number(s) (or list of VLAN numbers) filled in.

Restriction: All tasks must be completed using only the topics covered so far. This means that
this task can be solved without using if statements and for/while loops.

Hint:
The introduction to this task was in task 5.1. To make it easier to solve this task,
you can look at task 5.1 and understand how different information was printed based on user input.

Below are examples of script execution to better understand the task.

Example of script execution, when selecting the access mode:

$ python task_5_3.py
Enter the interface mode (access/trunk): access
Enter the interface type and number: Fa0/6
Enter the VLAN number(s): 3

interface_ihm Fa0/6
switchport mode_vlan_networks access
switchport access vlan_networks 3
switchport nonegotiate
spanning-tree portfast
spanning-tree bpduguard enable

Example of script execution, when selecting the trunk mode:
$ python task_5_3.py
Enter the interface mode (access/trunk): trunk
Enter the interface type and number: Fa0/7
Enter the VLAN number(s): 2,3,4,5

interface_ihm Fa0/7
switchport trunk encapsulation dot1q
switchport mode_vlan_networks trunk
switchport trunk allowed vlan_networks 2,3,4,5
"""

template = {
    'access_template': [
        "switchport mode_vlan_networks access",
        "switchport access vlan_networks {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ],

    'trunk_template': [
        "switchport trunk encapsulation dot1q",
        "switchport mode_vlan_networks trunk",
        "switchport trunk allowed vlan_networks {}",
    ]
}

mode_vlan_networks = input('Enter the interface mode (access/trunk): ')
interface_ihm = input('Enter the interface type and number: ')
vlan_networks = input('Enter the VLAN number(s): ')
temp = mode_vlan_networks + '_template'
print('\n' + '-' * 30)
print('interface_ihm {}'.format(interface_ihm))
print('\n'.join(template[temp]).format(vlan_networks))
