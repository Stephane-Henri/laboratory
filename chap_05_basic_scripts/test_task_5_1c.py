from pyneng_common_functions import check_pytest
import sys
from functools import wraps

import pytest

sys.path.append("..")


check_pytest(__loader__, __file__)


def count_calls(foobar):
    @wraps(foobar)
    def foobar2(*args, **kwargs):
        __tracebackhide__ = True
        foobar2.total_calls += 1
        result = foobar(*args, **kwargs)
        return result

    foobar2.total_calls = 0
    return foobar2


@count_calls
def monkey_input_r2(foobar3):
    __tracebackhide__ = True
    if monkey_input_r2.total_calls == 1:
        return "r2"
    elif monkey_input_r2.total_calls == 2:
        return "ip"


@count_calls
def monkey_input_sw1(foobar4):
    __tracebackhide__ = True
    if monkey_input_sw1.total_calls == 1:
        return "sw1"
    elif monkey_input_sw1.total_calls == 2:
        return "произвольная строка"


def test_task_r2_correct_param(capsys, monkeypatch):
    """
    Проверка работы задания при вводе r2
    """
    monkeypatch.setattr("builtins.input", monkey_input_r2)
    import task_5_1c as foobar5

    out, err = capsys.readouterr()
    correct_stdout = "10.255.0.2"

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def test_task_sw1_wrong_param(capsys, monkeypatch):
    """
    Проверка работы задания при вводе sw1
    """
    monkeypatch.setattr("builtins.input", monkey_input_sw1)
    if sys.modules.get("task_5_1c"):
        del sys.modules["task_5_1c"]
    try:
        import task_5_1c as foobar6
    except KeyError:
        pytest.fail(
            "В этом задании должна обрабатываться ситуация, "
            "когда параметр указан неправильный. Не должна возникать ошибка KeyError"
        )

    out, err = capsys.readouterr()
    correct_stdout = "параметра нет"
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout in out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
