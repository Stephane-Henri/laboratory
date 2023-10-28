import sys
from pyneng_common_functions import check_pytest

check_pytest(__file__, __loader__)


class TestFunctionInverted:
    def test_inverted_function(self, writer):
        import task_4_1 as scrambled_module
        expected_output = "nat overload GigabitEthernet0/1 interface ACL list source inside ip"

        output, error = writer.readouterr()

        assert output, "No output is generated. Make sure the function generates output with 'print'."
        assert expected_output == output.strip(
        ), "Incorrect output is generated."


inverted_test_function(capsys)
sys.path.append("..")
