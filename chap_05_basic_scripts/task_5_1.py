# -*- coding: utf-8 -*-
"""
Exercise 5.1

In the task, a dictionary with information about different devices is created.

It is necessary to request the user to enter the name of the device (r1, r2, or sw1).
And display information about the corresponding device on the standard output
(information will be in the form of a dictionary).

Example of script execution:
$ python task_5_1.py
Enter the device name: r1
{'location': '21 New Globe Walk', 'vendor': 'Cisco', 'model': '4451', 'ios': '15.4', 'ip': '10.255.0.1'}

Limitation: you cannot change the london_co dictionary.

All tasks must be performed using only the topics covered. In other words, this task can
be solved without using the 'if' statement.
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
print('\n' + '-' * 30)
print(dict(london_co[device_name]))
