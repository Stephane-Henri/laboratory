from pyneng_common_functions import check_pytest
import sys
from importlib import reload

sys.path.append("..")

check_pytest(__loader__, __file__)


def r2_task(capsys, monkeypatch):
    """
    Check the operation of the task when 'r2' is entered
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "r2")
    import task_5_1

    out, err = capsys.readouterr()
    r2_device = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "4451",
        "ios": "15.4",
        "ip": "10.255.0.2",
    }

    assert out, "Nothing is printed to the standard output. You need to not only get the correct result but also print it to the standard output using print"
    assert str(r2_device) in out.strip(
    ), "Incorrect output on the standard output"


def sw1_task(capsys, monkeypatch):
    """
    Check the operation of the task when 'sw1' is entered
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "sw1")
    if sys.modules.get("task_5_1"):
        reload(sys.modules["task_5_1"])
    import task_5_1

    out, err = capsys.readouterr()
    sw1_device = {
        "location": "21 New Globe Walk",
        "vendor": "Cisco",
        "model": "3850",
        "ios": "3.6.XE",
        "ip": "10.255.0.101",
        "vlans": "10,20,30",
        "routing": True,
    }
    assert out, "Nothing is printed to the standard output. You need to not only get the correct result but also print it to the standard output using print"
    assert str(sw1_device) in out.strip(
    ), "Incorrect output on the standard output"
