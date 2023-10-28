from pyneng_common_functions import check_pytest, unified_columns_output
import sys
from importlib import reload

sys.path.append("..")

check_pytest(__loader__, __file__)


def test_5_2_task_10_5_5_0_24(capsys, monkeypatch):
    """
    Checking the task with input 10.5.5.0/24
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.0/24")
    import task_5_2 as task

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        5         5         0\n"
        "00001010  00000101  00000101  00000000\n\n"
        "Mask:\n"
        "/24\n"
        "255       255       255       0\n"
        "11111111  11111111  11111111  00000000"
    )

    assert (
        out
    ), "Nothing is printed on the standard output. You should not only get the correct result but also print it to the standard output using print"
    assert correct_stdout == stdout, "Incorrect output"


def test_5_2_task_10_1_1_192_28(capsys, monkeypatch):

    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.192/28")
    if sys.modules.get("task_5_2"):
        reload(sys.modules["task_5_2"])
    import task_5_2 as task

    out, err = capsys.readouterr()
    stdout = unified_columns_output(out.strip())
    correct_stdout = unified_columns_output(
        "Network:\n"
        "10        1         1         192\n"
        "00001010  00000001  00000001  11000000\n\n"
        "Mask:\n"
        "/28\n"
        "255       255       255       240\n"
        "11111111  11111111  11111111  11110000"
    )

    assert (
        out
    ), "Nothing is printed on the standard output. You should not only get the correct result but also print it to the standard output using print"
    assert correct_stdout == stdout, "Incorrect output"
