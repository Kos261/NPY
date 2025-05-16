def mask_sum(data, mask):
    res = 0
    for val, mask_val in zip(data, mask):
       if mask_val != 0:
            res += val
    return res


def test_mask_sum():
    assert(mask_sum(data=[1,2,3], mask=[0,0,0]) == 0)

def test_mask_sum2():
    assert(mask_sum(data=[1,2,3], mask=[1,1,1]) == 6)