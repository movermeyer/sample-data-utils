import os
import sys


def pytest_configure(config):
    here = os.path.dirname(__file__)
    # sys.path.insert(0, here)


def runtests(args=None):
    import pytest

    if not args:
        args = []

    if not any(a for a in args[1:] if not a.startswith('-')):
        args.append('sample_data_utils')

    sys.exit(pytest.main(args))


if __name__ == '__main__':
    runtests(sys.argv)
