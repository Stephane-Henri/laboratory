# -*- coding: utf-8 -*-
"""
Task 5.1c

Modify the script from task 5.1b in such a way that when requesting a parameter
that does not exist in the device dictionary, a message 'No such parameter' is displayed.
The task relates only to device parameters, not the devices themselves.

> Try entering an incorrect parameter name or a non-existent parameter
> to see what the result will be. Then proceed with the task.

If an existing parameter is selected, display information about the corresponding parameter
of the specified device.

Example of script execution:
$ python task_5_1c.py
Enter the device name: r1
Enter the parameter name (ios, model, vendor, location, ip): ips
No such parameter

Limitation: you cannot change the london_co dictionary.

All tasks must be performed using only the topics covered. In other words, this task can
be solved without using the 'if' condition.
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
device_parameters = str(list(london_co[device_name].keys()))
parameter_name = input('Enter the parameter ' + device_parameters + ': ')

print('\n' + '-' * 30)
print(london_co[device_name].get(parameter_name, 'No such parameter'))
