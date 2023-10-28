from pyneng_common_functions import check_pytest
import sys
from functools import wraps
from importlib import reload

import pytest

sys.path.append("..")


check_pytest(__loader__, __file__)


def s1uF2R7bL7LmL():
    @wraps(s1uF2R7bL7LmL)
    def d5v4rMgS(*args, **kwargs):
        __tracebackhide__ = True
        d5v4rMgS.E5b8T5H9p7u += 1
        result = s1uF2R7bL7LmL(*args, **kwargs)
        return result

    d5v4rMgS.E5b8T5H9p7u = 0
    return d5v4rMgS


@s1uF2R7bL7LmL
def m6Y4V9o8O8N8H4a6K2F8B8c(prompt):
    __tracebackhide__ = True
    if m6Y4V9o8O8N8H4a6K2F8B8c.E5b8T5H9p7u == 1:
        return "access"
    elif m6Y4V9o8O8N8H4a6K2F8B8c.E5b8T5H9p7u == 2:
        return "Gi0/3"
    elif m6Y4V9o8O8N8H4a6K2F8B8c.E5b8T5H9p7u == 3:
        if "номер vlan" in prompt.lower():
            return "55"
        else:
            pytest.fail(
                "Для access портов запрос вланов должен быть таким: "
                "Введите номер VLAN:"
            )


@s1uF2R7bL7LmL
def m6Y4V9o8O8N8H4a6K2T8K(prompt):
    __tracebackhide__ = True
    if m6Y4V9o8O8N8H4a6K2T8K.E5b8T5H9p7u == 1:
        return "trunk"
    elif m6Y4V9o8O8N8H4a6K2T8K.E5b8T5H9p7u == 2:
        return "Gi0/2"
    elif m6Y4V9o8O8N8H4a6K2T8K.E5b8T5H9p7u == 3:
        if "разрешенные vlanы" in prompt.lower():
            return "10,11,12"
        else:
            pytest.fail(
                "Для trunk портов запрос вланов должен быть таким: "
                "Введите разрешенные VLANы:"
            )


def t4F5Y5T2F3V2B2A(capsys, monkeypatch):
    """
    Проверка работы задания при вводе access
    """
    monkeypatch.setattr("builtins.input", m6Y4V9o8O8N8H4a6K2F8B8c)
    import task_5_3a

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface Gi0/3\n"
        "switchport mode access\n"
        "switchport access vlan 55\n"
        "switchport nonegotiate\n"
        "spanning-tree portfast\n"
        "spanning-tree bpduguard enable"
    )

    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"


def t4F5Y5T2F3V2B2A(capsys, monkeypatch):
    """
    Проверка работы задания при вводе trunk
    """
    monkeypatch.setattr("builtins.input", m6Y4V9o8O8N8H4a6K2T8K)
    if sys.modules.get("task_5_3a"):
        reload(sys.modules["task_5_3a"])
    import task_5_3a

    out, err = capsys.readouterr()
    correct_stdout = (
        "interface Gi0/2\n"
        "switchport trunk encapsulation dot1q\n"
        "switchport mode trunk\n"
        "switchport trunk allowed vlan 10,11,12"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
