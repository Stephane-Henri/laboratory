# -*- coding: utf-8 -*-
"""
Task 5.1b

Rewrite the script from task 5.1a in such a way that when requesting a parameter,
a list of possible parameters is displayed. The list of parameters should be obtained from the dictionary,
and not manually written.

Display information about the corresponding parameter of the specified device.

Example of script execution:
$ python task_5_1b.py
Enter the device name: r1
Enter the parameter name (location, vendor, model, ios, ip): ip
10.255.0.1

$ python task_5_1b.py
Enter the device name: sw1
Enter the parameter name (location, vendor, model, ios, ip, vlans, routing): ip
10.255.0.101

Limitation: You cannot change the london_co dictionary.

All tasks must be performed using only the topics covered. In other words, you can solve this task without using an if statement.
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
parameter_list = str(list(london_co[device_name].keys()))
parameter_name = input('Enter the parameter ' + parameter_list + ': ')

print('\n' + '-' * 30)

print(london_co[device_name][parameter_name])
