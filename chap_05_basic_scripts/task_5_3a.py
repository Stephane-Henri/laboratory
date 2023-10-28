# -*- coding: utf-8 -*-
"""
Exercise 5.3a

Extend the script from task 5.3 in such a way that, depending on the selected mode,
different questions are asked in the request for the VLAN number or list of VLANs:
* for access: 'Enter VLAN number:'
* for trunk: 'Enter allowed VLANs:'

Restriction: All tasks must be completed using only the topics covered.
This means that this task can be solved without using if statements and for/while loops.
"""

config_templates = {
    'access_template': [
        "switchport mode access",
        "switchport access vlan {}",
        "switchport nonegotiate",
        "spanning-tree portfast",
        "spanning-tree bpduguard enable",
    ],

    'trunk_template': [
        "switchport trunk encapsulation dot1q",
        "switchport mode trunk",
        "switchport trunk allowed vlan {}",
    ]
}

network_mode = input('Enter the interface mode (access/trunk): ')
interface = input('Enter the type and number of the interface: ')
questions = {
    'access': 'Enter VLAN number: ',
    'trunk': 'Enter allowed VLANs: '
}
vlan_input = input(questions[network_mode])
template_type = network_mode + '_template'
print('\n' + '-' * 30)
print('interface {}'.format(interface))
print('\n'.join(config_templates[template_type]).format(vlan_input))
