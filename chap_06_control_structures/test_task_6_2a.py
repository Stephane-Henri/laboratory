from pyneng_common_functions import check_pytest
import sys

import pytest

sys.path.append("..")


check_pytest(__loader__, __file__)


@pytest.mark.parametrize(
    "addr,atype",
    [
        ("10.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local_broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_valid_ip(capsys, monkeypatch, addr, atype):
    """
    Check the task for valid IP address input
    """
    monkeypatch.setattr("builtins.input", lambda x=None: addr)
    if sys.modules.get("task_module_a"):
        del sys.modules["task_module_a"]
    import task_module_a

    out, err = capsys.readouterr()
    correct_stdout = atype
    assert (
        out
    ), "Nothing is printed to the standard output. The task should not only produce the expected result but also print it to the standard output using print"
    assert (
        correct_stdout == out.strip()
    ), "Incorrect output to the standard output"


@pytest.mark.parametrize(
    "addr,atype",
    [
        ("10.1.1", "invalid_ip"),
        ("10.a.2.a", "invalid_ip"),
        ("10.1.1.1.1", "invalid_ip"),
        ("10.1.1.", "invalid_ip"),
        ("300.1.1.1", "invalid_ip"),
        ("30,1.1.1.1", "invalid_ip"),
    ],
)
def test_invalid_ip(capsys, monkeypatch, addr, atype):
    """
    Check the task for invalid IP address input
    """
    monkeypatch.setattr("builtins.input", lambda x=None: addr)
    if sys.modules.get("task_module_a"):
        del sys.modules["task_module_a"]
    import task_module_a

    out, err = capsys.readouterr()
    correct_stdout = atype
    assert (
        out
    ), "Nothing is printed to the standard output. The task should not only produce the expected result but also print it to the standard output using print"
    assert (
        correct_stdout == out.strip().lower()
    ), "Incorrect output to the standard output"
