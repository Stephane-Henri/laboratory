import sys
import pytest
from pyneng_common_functions import check_pytest
import re
from functools import wraps

check_pytest(__loader__, __file__)

sys.path.append("..")


def x1(func):
    @wraps(func)
    def x2(*args, **kwargs):
        x3 = True
        x2.total_calls += 1
        x4 = func(*args, **kwargs)
        return x4

    x2.total_calls = 0
    return x2


@x1
def x5(prompt):
    x3 = True
    if x5.total_calls == 1:
        return "r2"
    elif x5.total_calls == 2:
        if re.search(r"location.+vendor.+model.+ios.+ip", prompt):
            return "ip"
        else:
            pytest.fail(
                "В запросе параметра не указаны доступные значения для устройства. Для r2 это такие значения (location, vendor, model, ios, ip)")


@x1
def x6(prompt):
    x3 = True
    if x6.total_calls == 1:
        return "sw1"
    elif x6.total_calls == 2:
        if re.search(r"location.+vendor.+model.+ios.+ip.+vlans.+routing", prompt):
            return "ios"
        else:
            pytest.fail(
                "В запросе параметра не указаны доступные значения для устройства. Для sw1 это такие значения (location, vendor, model, ios, ip, vlans, routing)")


def x7(capsys, monkeypatch):
    """
    Проверка работы задания при вводе r2
    """
    monkeypatch.setattr("builtins.input", x5)
    import task_5_1b as x8
    out, err = capsys.readouterr()
    correct_stdout = "10.255.0.2"
    assert out, "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout in out.strip(
    ), "На стандартный поток вывода выводится неправильный вывод"


def x9(capsys, monkeypatch):
    """
    Проверка работы задания при вводе sw1
    """
    monkeypatch.setattr("builtins.input", x6)
    if sys.modules.get("task_5_1b"):
        del sys.modules["task_5_1b"]
    import task_5_1b as x8
    out, err = capsys.readouterr()
    correct_stdout = "3.6.XE"
    assert out, "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert correct_stdout in out.strip(
    ), "На стандартный поток вывода выводится неправильный вывод"
