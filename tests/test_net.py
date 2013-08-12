import pytest
from sample_data_utils.net import ipaddress, ip, ipv4, ipv6, mac_address, node


def test_ipaddress():
    assert ipaddress()
    # with pytest.raises(MaxAttemptException):
    #     ipaddress(range(1, 256))


def test_ip():
    assert ip(private=True, public=True)
    assert ip(private=True, public=False)
    assert ip(private=False, public=True)

    with pytest.raises(ValueError):
        ip(False, False)


def test_ipv4():
    assert ipv4()


def test_ipv6():
    assert ipv6()


def test_node():
    host = node('192.168.10.101/32')  # no sense. just for test
    assert host == '192.168.10.101'

    host = node('192.168.10.101/24')
    assert host.startswith('192.168.10.')


def test_macaddress():
    mac = mac_address()
    assert len(mac) == 17

    mac = mac_address(False)
    assert len(mac) == 17
