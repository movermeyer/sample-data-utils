from decimal import Decimal
from sample_data_utils.money import currency, amount


def test_currency():
    assert currency()


def test_amount():
    assert amount(10) > 10
    assert 1000 > amount(10, 1000) > 10
    assert isinstance(amount(), Decimal)
