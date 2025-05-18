import pytest
from unittest import mock
import json
from typing import List, Union
from homework import take_from_list, calculate
import tempfile
import os

@pytest.mark.parametrize("li, indices, res", 
                        [([10,20,30],        [1],    [20]), 
                         ([10,20,30],         1 ,    [20]), 
                         ([10,20,30,40,50], [-1,-2], [50,40])])
def test_take_from_list(li: list, indices: Union[int, List[int]], res: list):
    assert take_from_list(li, indices) == res


def test_take_from_text():
    with pytest.raises(ValueError):
        assert take_from_list([10,20,30], [1, "text", True]) == "anything" # type: ignore

def test_take_from_out_of_range():
    with pytest.raises(IndexError):
        assert take_from_list([10,20,30], 5) == "anything"



def test_calculate():
    with tempfile.TemporaryDirectory() as tmpdir:
        in_path = os.path.join(tmpdir, "input.json")
        out_path = os.path.join(tmpdir, "output.json")

        input_data = {
            "list":[1,5,10],
            "indices": 0
        }

        with open(in_path, mode='w') as f:
            json.dump(input_data, f)

        # Changing return value
        with mock.patch("homework.take_from_list", return_value=["MOCKED"]):
            calculate(in_path, out_path)

        with open(out_path, mode='r') as f:
            result = json.load(f)
            print(result)
        
        assert result == ["MOCKED"]


if __name__ == "__main__":
    test_calculate()
