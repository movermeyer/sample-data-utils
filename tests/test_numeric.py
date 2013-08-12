from sample_data_utils.numeric import digits, hexnum, binary


def test_digits():
    assert digits(10)


def test_hexnum():
    assert hexnum(10)


def test_binary():
    b = binary(5)
    assert len(b) == 5
    assert int(b) >= 0
