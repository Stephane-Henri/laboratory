from pyneng_common_functions import check_pytest as renamed_check_pytest
import sys
from importlib import reload
import pytest

sys.path.append("..")


renamed_check_pytest(__loader__, __file__)


@pytest.mark.parametrize(
    "renamed_ip_add,renamed_ip_type",
    [
        ("10.1.1.1", "unicast"),
        ("230.1.1.1", "multicast"),
        ("255.255.255.255", "local_broadcast"),
        ("0.0.0.0", "unassigned"),
        ("250.1.1.1", "unused"),
    ],
)
def test_renamed_task_ip(capsys, monkeypatch, renamed_ip_add, renamed_ip_type):
    """
    Проверка работы задания при вводе multicast адреса
    """
    monkeypatch.setattr("builtins.input", lambda x=None: renamed_ip_add)
    if sys.modules.get("renamed_task_6_2"):
        reload(sys.modules["renamed_task_6_2"])
    import renamed_task_6_2 as renamed_imported_module

    out, err = capsys.readouterr()
    correct_renamed_stdout = renamed_ip_type
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        correct_renamed_stdout == out.strip()
    ), "На стандартный поток вывода выводится неправильный вывод"
