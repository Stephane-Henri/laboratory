# -*- coding: utf-8 -*-
"""
Task 5.1a

Modify the script from task 5.1 so that, in addition to the device name,
it also requests the device parameter to display.

Display information about the specified parameter of the specified device.

Example of script execution:
$ python task_5_1a.py
Enter the device name: r1
Enter the parameter name: ios
15.4

Constraint: You cannot modify the london_co dictionary.

All tasks must be completed using only the topics covered. In other words, this task can
be solved without using conditional if statements.
"""

london_co = {
    "r1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.1",
    },
    "r2": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    },
    "sw1": {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    },
}

device_name = input('Enter the device name: ')
parameter_name = input('Enter the parameter name: ')

print('\n' + '-' * 30)
print(london_co[device_name][parameter_name])
