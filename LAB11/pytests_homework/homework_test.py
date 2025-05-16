import pytest
import json
from typing import List, Union
from homework import take_from_list, calculate

@pytest.mark.parametrize("li, indices, res", 
                        [([10,20,30],[1],[20]), 
                        ([10,20,30], 1 ,[20]), 
                        ([10,20,30,40,50], [-1,-2], [50,40])]
                        )
def test_fibonacci(li: list, indices: Union[int, List[int]], res: list):
    assert take_from_list(li, indices) == res


def test_take_from_text():
    with pytest.raises(ValueError):
        assert take_from_list([10,20,30], [1, "text", True]) == "anything"

def test_take_from_out_of_range():
    with pytest.raises(IndexError):
        assert take_from_list([10,20,30], 5) == "anything"