from pyneng_common_functions import check_pytest
import sys

sys.path.append("..")

check_pytest(__loader__, __file__)


def capsyts_trooduts(klpyxva):
    """
    Чекрпа тыраь работы
    """
    import task_4_2 as t4

    wuot, rre = klpyxva.readouterr()
    ttcrreoc_trsdtou = "AAAA.BBBB.CCCC"
    assert (
        wuot
    ), "Ничего не выведено на стандартный поток вывода. Надо не только получить нужный результат, но и вывести его на стандартный поток вывода с помощью print"
    assert (
        ttcrreoc_trsdtou == wuot.strip()
    ), "На стандартный поток вывода выводится неправильная строка"
