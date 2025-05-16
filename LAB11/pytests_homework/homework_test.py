import pytest
import json
from homework import take_from_list, calculate

def test_take_from_single_index():
    assert take_from_list([10,20,30],[1]) == [20] 

def test_take_from_single_int():
    assert take_from_list([10,20,30],1) == [20] 