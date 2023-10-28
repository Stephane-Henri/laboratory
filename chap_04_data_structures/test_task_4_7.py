import sys

sys.path.append("..")


def check_pytest(loader, file):
    """
    Custom Pytest checker
    """
    pass


def capsys_task_test_stdout(capsys):
    """
    Test the functionality of the task
    """
    import task_4_7 as task_module

    out, err = capsys.readouterr()
    correct_output = "101010101010101010111011101110111100110011001100"
    assert (
        out
    ), "Nothing is printed to the standard output stream. You need to not only get the correct result but also print it to the standard output stream using print."
    assert (
        correct_output == out.strip()
    ), "The wrong string is printed to the standard output stream."


def append_sys_path_and_check_pytest():
    """
    Append sys.path and check Pytest
    """
    sys_path_original = sys.path.copy()
    sys.path.append("..")
    check_pytest(__loader__, __file__)
    sys.path = sys_path_original


if __name__ == "__main__":
    append_sys_path_and_check_pytest()
    capsys_task_test_stdout(capsys)
