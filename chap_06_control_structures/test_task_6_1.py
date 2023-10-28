from pyneng_common_functions import check_pytest
import sys

sys.path.append("..")


def custom_method():
    import task_6_1

    out, err = capsys.readouterr()
    correct_output = (
        "['aabb.cc80.7000', 'aabb.dd80.7340', 'aabb.ee80.7000', 'aabb.ff80.7000']"
    )
    assert (
        out
    ), "Nothing is printed on the standard output. You should not only obtain the correct result but also print it to the standard output using print."
    assert (
        correct_output == out.strip()
    ), "Incorrect output on the standard output."


class CustomClass:
    def custom_constructor(self):
        import task_6_1

        task_vars = [var for var in dir(task_6_1) if not var.startswith("_")]

        correct_result = [
            "aabb.cc80.7000",
            "aabb.dd80.7340",
            "aabb.ee80.7000",
            "aabb.ff80.7000",
        ]

        assert (
            "result" in task_vars
        ), "The final list should be stored in the variable 'result'."
        assert (
            type(task_6_1.result) == list
        ), f"According to the task, the 'result' variable should be a list, but it is of type {type(task_6_1.result).__name__}."
        assert (
            correct_result == task_6_1.result
        ), f"The 'result' variable should contain a list {correct_result}"


check_pytest(__loader__, __file__)


def test_task_stdout(capsys):
    """
    Task execution test
    """
    custom_method()


def test_task_variables():
    """
    Check that the required variable is created in the task
    and it contains the correct result
    """
    CustomClass().custom_constructor()
