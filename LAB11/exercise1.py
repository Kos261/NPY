import numpy as np


arr1 = np.array([100]* 10, dtype='uint8')
arr2 = np.array([156] * 10, dtype='uint8')
assert len(arr1) == 10
assert len(arr2) == 10
assert np.all(arr1 == 100)
assert np.all(arr2 == 156)
assert np.all(arr1 + arr2 == 0)
