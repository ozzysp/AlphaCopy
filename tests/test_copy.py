
import os
import filecmp
from collections import namedtuple

from unittest.mock import patch, call

import alphacopy


def test_copy_read():
    src = "tests/helloworld"
    dst = "HiPeople"
    alphacopy.copy_file(src, dst)
    assert os.path.exists(dst)
    with open(dst) as f:
        assert f.read() == "Hello world"
    os.remove(dst)


def test_copy_system():
    src = "tests/helloworld"
    dst = "HiPeople"
    alphacopy.copy_file(src, dst)
    assert os.path.exists(dst)
    assert filecmp.cmp(src, dst)
    os.remove(dst)


def test_copy_img():
    src = "tests/image_test.jpg"
    dst = "copied_image"
    alphacopy.copy_file(src, dst)
    assert os.path.exists(dst)
    assert filecmp.cmp(src, dst)
    os.remove(dst)


def test_check_disks_returns_bool():
    x = alphacopy.check_disks('.', '.')
    assert isinstance(x, bool)


@patch('alphacopy.copy.disk_usage')
def test_check_disks_disk_usage_calls(mock_disk_usage):
    DiskResponse = namedtuple('DiskResponse', ['total', 'used', 'free'])
    mock_disk_usage.return_value = DiskResponse(2, 1, 1)
    _ = alphacopy.check_disks('a', 'b')
    assert mock_disk_usage.call_count == 2
    assert mock_disk_usage.call_args_list == [call('a'), call('b')]


@patch('alphacopy.copy.disk_usage')
def test_check_disks_space_ok(mock_disk_usage):
    DiskResponse = namedtuple('DiskResponse', ['total', 'used', 'free'])
    mock_disk_usage.return_value = DiskResponse(2, 1, 1)
    assert alphacopy.check_disks('a', 'b')


@patch('alphacopy.copy.disk_usage')
def test_check_disks_space_not_ok(mock_disk_usage):
    DiskResponse = namedtuple('DiskResponse', ['total', 'used', 'free'])
    mock_disk_usage.return_value = DiskResponse(3, 2, 1)
    assert not alphacopy.check_disks('a', 'b')
