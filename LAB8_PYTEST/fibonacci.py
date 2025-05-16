import functools
import pytest
from typing import List

@functools.lru_cache
def fibonacci(n: int):
    if n < 0:
        raise ValueError("Unsupported value")
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    

@pytest.mark.parametrize("num, res", [(0,0), (1,1), (2,1), (10, 55), (18,2584)])
def test_fibonacci(num: int, res: int):
    assert fibonacci(num) == res

@pytest.mark.parametrize("num", [-1, -7, -50])
def test_fibonacci_negative(num: int):
    with pytest.raises(ValueError, match="Unsupported value"):
        fibonacci(num)