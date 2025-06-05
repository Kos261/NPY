from homework_exercise import some_calculation_function, some_calculation_function2
import numpy as np

def test_some_calculation_function():
    result = some_calculation_function()
    assert np.all(result == 0)
    assert result.shape == (4, 7)


def test_some_calculation_function2():
    assert some_calculation_function2() == 18
