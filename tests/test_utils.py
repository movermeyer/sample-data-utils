from random import choice
import mock
import pytest
from sample_data_utils.exception import MaxAttemptException
from sample_data_utils.utils import unique, sequence


def test_unique():
    def func():
        values = (1, 2)
        return choice(values)
    with mock.patch('sample_data_utils.utils._cache_unique', {}):
        f = unique(func)
        assert f() != f()


def test_unique_fail():
    def func():
        values = (1, 2)
        return choice(values)

    f = unique(func)
    with pytest.raises(MaxAttemptException):
        f()
        f()
        f()


def test_sequence():
    with mock.patch('sample_data_utils.utils._sequence_counters', dict()):
        assert next(sequence('abc')) == 'abc-0'
        assert next(sequence('abc')) == 'abc-1'

        c = {}
        assert next(sequence('abc', c)) == 'abc-0'
        assert next(sequence('abc', c)) == 'abc-1'

        assert next(sequence('abc', {})) == 'abc-0'
        assert next(sequence('abc', {})) == 'abc-0'

        assert next(sequence('abc', None)) == 'abc-0'
        assert next(sequence('abc', None)) == 'abc-0'

def test_unique_cache():
    def func():
        values = (1, 2)
        return choice(values)

    f1 = unique(func, cache={})
    f2 = unique(func, cache={})

    assert f1() != f1()
    assert f2() != f2()
