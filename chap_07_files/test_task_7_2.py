from common_functions import check_pytest
import re
import sys

sys.path.append("..")


check_pytest(__loader__, __file__)


def function_test(param1, param2):
    """
    Checking the task with 'access' input
    """
    param2.setattr("sys.argv", ["task_7_2.py", "config_sw1.txt"])
    import task_7_2

    out, err = param1.readouterr()
    correct_output = (
        "Current configuration : 2033 bytes\n"
        "version 15.0\n"
        "service timestamps debug datetime msec\n"
        "service timestamps log datetime msec\n"
        "no service password-encryption\n"
        "hostname sw1\n"
        "interface Ethernet0/0\n"
        " duplex auto\n"
        "interface Ethernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " switchport mode trunk\n"
        " duplex auto\n"
        " spanning-tree portfast edge trunk\n"
        "interface Ethernet0/2\n"
        " duplex auto\n"
        "interface Ethernet0/3\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " duplex auto\n"
        " switchport mode trunk\n"
        " spanning-tree portfast edge trunk\n"
    )
    config_section = re.search(
        r"(Current configuration.*?)interface Ethernet1/0", out, re.DOTALL
    ).group(1)

    assert (
        out
    ), "Nothing is printed to the standard output. The desired result should not only be obtained but also printed to the standard output using print"
    assert (
        correct_output == config_section
    ), "Incorrect output is printed to the standard output"
