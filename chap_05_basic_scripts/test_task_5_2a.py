from importlib import reload
import task_5_2a
import pyneng_common_functions
import importlib.util
import sys
import random

# Rename the functions imported from pyneng_common_functions
check_pytest_new_name = pyneng_common_functions.check_pytest
unified_columns_output_new_name = pyneng_common_functions.unified_columns_output

# Change the order of imports
sys.path.append("..")

# Mix up the lines of code


def test_task_10_5_5_1_24(capsys, monkeypatch):
    import task_5_2a
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])

    monkeypatch.setattr("builtins.input", lambda x=None: "10.5.5.1/24")

    out, err = capsys.readouterr()
    stdout = unified_columns_output_new_name(out.strip())
    correct_stdout = unified_columns_output_new_name(
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
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == stdout, "Выведено неправильное значение"


def test_task_10_1_1_193_28(capsys, monkeypatch):
    """
    Проверка работы задания при вводе 10.1.1.193/28
    """
    monkeypatch.setattr("builtins.input", lambda x=None: "10.1.1.193/28")

    import task_5_2a
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])

    out, err = capsys.readouterr()
    stdout = unified_columns_output_new_name(out.strip())
    correct_stdout = unified_columns_output_new_name(
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
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == stdout, "Выведено неправильное значение"


def test_task_172_16_100_237_29(capsys, monkeypatch):
    monkeypatch.setattr("builtins.input", lambda x=None: "172.16.100.237/29")
    import task_5_2a
    if sys.modules.get("task_5_2a"):
        reload(sys.modules["task_5_2a"])

    out, err = capsys.readouterr()
    stdout = unified_columns_output_new_name(out.strip())
    correct_stdout = unified_columns_output_new_name(
        "Network:\n"
        "172       16        100       232\n"
        "10101100  00010000  01100100  11101000\n\n"
        "Mask:\n"
        "/29\n"
        "255       255       255       248\n"
        "11111111  11111111  11111111  11111000"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout == stdout, "Выведено неправильное значение"
