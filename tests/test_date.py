import datetime
from time import timezone
import pytest
from sample_data_utils.date import date, day
from dateutil.relativedelta import relativedelta, SU

today = datetime.date.today()

tomorrow = today + relativedelta(days=+1)
next_tomorrow = today + relativedelta(days=+2)
next_month = today + relativedelta(months=+1)
next_year = today + relativedelta(years=+1)


def test_date():
    c = date(today, tomorrow)
    assert c == today

    c = date(today, next_month)
    assert today <= c < next_year

    c = date(today, next_year)
    assert today <= c < next_year


def test_day():
    c = day(today, next_month, [SU])
    assert next_month >= c >= today
    assert c.weekday() == 6

    c = day(today, tomorrow)
    assert next_month >= c >= today
    assert c in [today, tomorrow]

    c = day(today, today)
    assert c == today

    with pytest.raises(IndexError):
        c = day(today, tomorrow, [SU])

