from pyneng_common_functions import check_pytest, unified_columns_output
import sys

sys.path.append("..")


check_pytest(__loader__, __file__)


def capsys_test_task_stdout():
    import task_4_6 as tsk

    out, err = capsys.readouterr()
    c_s = unified_columns_output(
        "Prefix                10.0.24.0/24\n"
        "AD/Metric             110/41\n"
        "Next-Hop              10.0.13.3\n"
        "Last update           3d18h\n"
        "Outbound Interface    FastEthernet0/0\n"
    )
    assert (
        out
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert c_s == unified_columns_output(
        out.strip()
    ), "На стандартный поток вывода выводится неправильная строка"
