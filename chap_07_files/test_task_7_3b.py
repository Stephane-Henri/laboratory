import re
import sys
import pytest

sys.path.append("..")

from custom_common_functions import check_custom_pytest

check_custom_pytest(__loader__, __file__)


def custom_test_output(capsys, monkeypatch, custom_vlan, custom_result):
    """
    Custom test function
    """
    monkeypatch.setattr("builtins.input", lambda x=None: custom_vlan)
    if sys.modules.get("custom_task_7_3b"):
        del sys.modules["custom_task_7_3b"]
    import custom_task_7_3b

    custom_out, custom_err = capsys.readouterr()
    custom_correct_stdout = custom_unified_columns_output(custom_result)
    assert custom_correct_stdout == custom_unified_columns_output(
        custom_out.strip()
    ), "Incorrect output on standard output"


def custom_unified_columns_output(output):
    lines = sorted(
        [re.split(r"  +", line.strip()) for line in output.strip().split("\n")]
    )
    formatted = [("{:25}" * len(line)).format(*line) for line in lines]
    return "\n".join(formatted)


@pytest.mark.parametrize(
    "custom_vlan,custom_result",
    [
        (
            "10",
            "10       0a1b.1c80.7000      Gi0/4\n10       01ab.c5d0.70d0      Gi0/8",
        ),
        (
            "1000",
            "1000     0a4b.c380.7d00      Gi0/9",
        ),
    ],
    ids=["Custom VLAN 10", "Custom VLAN 1000"],
)