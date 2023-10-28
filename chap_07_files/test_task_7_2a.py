from pyneng_common_functions import check_pytest
import sys
sys.path.append("..")
check_pytest(__loader__, __file__)


def task_test(capsys, monkeypatch):
    """
    Check task functionality when input is 'access'
    """
    monkeypatch.setattr("sys.argv", ["task_7_2a.py", "config_sw1.txt"])
    import task_7_2a
    out, err = capsys.readouterr()
    correct_stdout = (
        "version 15.0\n"
        "service timestamps debug datetime msec\n"
        "service timestamps log datetime msec\n"
        "no service password-encryption\n"
        "hostname sw1\n"
        "interface Ethernet0/0\n"
        "interface Ethernet0/1\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " switchport mode trunk\n"
        " spanning-tree portfast edge trunk\n"
        "interface Ethernet0/2\n"
        "interface Ethernet0/3\n"
        " switchport trunk encapsulation dot1q\n"
        " switchport trunk allowed vlan 100\n"
        " switchport mode trunk\n"
        " spanning-tree portfast edge trunk\n"
        "interface Ethernet1/0\n"
        "interface Ethernet1/1\n"
        "interface Ethernet1/2\n"
        "interface Ethernet1/3\n"
        "interface Vlan100\n"
        " ip address 10.0.100.1 255.255.255.0\n"
        "line con 0\n"
        " exec-timeout 0 0\n"
        " privilege level 15\n"
        " logging synchronous\n"
        "line aux 0\n"
        "line vty 0 4\n"
        " login\n"
        " transport input all\n"
        "end"
    )
    assert (
        out
    ), "Nothing is printed to the standard output. You need to not only get the correct result but also print it to the standard output using print"
    assert (
        correct_stdout == out.strip()
    ), "The standard output does not match the expected output"
