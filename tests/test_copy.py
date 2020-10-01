
import os
import uuid
import shutil
import random
import filecmp
from collections import namedtuple
from unittest.mock import patch, call

import pytest

import alphacopy


@pytest.fixture(scope='function')
def random_tree():
    """
    This fixture creates a random folder tree in ./tmp/ filled with files
    It deletes the entire tree after the test
    The tree is unique for each test run and each test function
    """

    def create_files(folder: str):
        for i in range(random.randint(1, 3)):
            _ = create_random_file(folder=folder)

    def create_folders(folder: str, min_: int, max_: int):
        for i in range(random.randint(min_, max_)):
            new_folder = os.path.join(folder, str(uuid.uuid4()))
            os.mkdir(new_folder)
            create_files(new_folder)
            create_folders(new_folder, max(min_ - 1, 0), max(max_ - 1, 0))

    root = 'tmp'
    os.makedirs(root)
    try:
        create_folders(root, min_=1, max_=3)
        yield root
    except:  # noqa E722
        raise
    finally:
        shutil.rmtree(root)


@pytest.fixture(scope='function')
def random_file():
    try:
        filename = create_random_file('.')
        yield filename
    except:  # noqa E722
        raise
    finally:
        try:
            os.remove(filename)
        except:  # noqa E722
            pass


def create_random_file(folder: str = '.'):
    """
    This function create a random file at a given location
    The file size ranges from 1 byte to 1 MB
    The function returns a tuple with filename and filesize
    """

    filename = os.path.join(folder, str(uuid.uuid4()))
    filesize = random.randint(1, 1024 ** 2)  # file up to 1 MB
    with open(filename, 'wb') as f:
        f.write(os.urandom(filesize))
    return filename


def test_copy_binary(random_file):
    src = random_file
    dst = 'output_file'
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
