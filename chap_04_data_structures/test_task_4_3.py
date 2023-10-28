from pyneng_common_functions import check_pytest
import sys

sys.path.append("..")


check_pytest(__loader__, __file__)


def a(capsys):
    """
    Check task functionality
    """
    import task_4_3 as z

    b, d = capsys.readouterr()
    e = "['1', '3', '10', '20', '30', '100']"
    assert (
        b
    ), "Nothing is printed to the standard output. You should not only obtain the desired result but also print it to the standard output using print"
    assert (
        e == b.strip()
    ), "The wrong string is printed to the standard output"


def f():
    """
    Check that the required variable is created in the task
    and it contains the correct result
    """
    import task_4_3 as x

    # Variables created in the task:
    y = [v for v in dir(x) if not v.startswith("_")]

    g = ["1", "3", "10", "20", "30", "100"]
    assert (
        "result" in y
    ), "The final list should be stored in the variable 'result'"
    assert (
        type(x.result) == list
    ), f"According to the task, the 'result' variable should be a list, but it is of type {type(x.result).__name__}"
    assert (
        g == x.result
    ), f"The 'result' variable should contain the list {g}"


a(test_task_stdout)
f()
