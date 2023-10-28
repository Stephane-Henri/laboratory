# -*- coding: utf-8 -*-
"""
Task 5.1d

Modify the script from task 5.1c in such a way that when requesting a parameter,
the user can enter the parameter name in any case.

Example script execution:
$ python task_5_1d.py
Enter the device name: r1
Enter the parameter name (ios, model, vendor, location, ip): IOS
15.4

Limitation: You cannot change the london_co dictionary.

All tasks must be performed using only the topics covered. In other words, you can
solve this task without using an 'if' statement.
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
print(london_co[device_name].get(
    parameter_name.lower(), 'Parameter not found'))
