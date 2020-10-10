
import os
import uuid
import shutil
import random
import filecmp
import itertools
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

    def create_folders(folder: str, child_folders: int):
        for i in range(child_folders + 1):
            new_folder = os.path.join(folder, str(uuid.uuid4()))
            os.mkdir(new_folder)
            create_files(new_folder)
            create_folders(new_folder, child_folders - 1)

    root = 'tmp'
    os.makedirs(root)
    try:
        create_folders(root, 3)
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
    The file size ranges from 1 byte to 1 KB
    The function returns a tuple with filename and filesize
    """

    filename = os.path.join(folder, str(uuid.uuid4()))
    filesize = random.randint(1, 1024)  # file up to 1 MB
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


def test_external_disks_returns_list(random_tree):
    return_value = alphacopy.external_disks(random_tree)
    assert isinstance(return_value, list)


def test_external_disks_raises_value_error_when_src_doesnt_exist():
    src = str(uuid.uuid4())
    with pytest.raises(ValueError):
        _ = alphacopy.external_disks(src)


def test_external_disks_raises_value_error_when_src_is_a_file(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(files) >= 1:
            break
    file = files[0]
    with pytest.raises(ValueError):
        _ = alphacopy.external_disks(file)


def test_external_disks_src_with_no_folders_and_no_files(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(folders) == 0 and len(files) == 0:
            break
    return_value = alphacopy.external_disks(root)
    assert len(return_value) == 0


def test_external_disks_src_with_no_folders_but_some_files(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(folders) == 0 and len(files) > 0:
            break
    return_value = alphacopy.external_disks(root)
    assert len(return_value) == 0


def test_external_disks_src_with_some_folders_not_mounted(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(folders) > 0:
            break
    return_value = alphacopy.external_disks(root)
    assert len(return_value) == 0


def test_external_disks_src_with_one_folder_mounted(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(folders) == 1:
            break
    with patch('alphacopy.copy.os.path.ismount', return_value=True):
        return_value = alphacopy.external_disks(root)
    assert len(return_value) == 1
    assert return_value[0] == os.path.join(root, folders[0])


def test_external_disks_src_with_many_folders_mounted(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(folders) > 1:
            break
    with patch('alphacopy.copy.os.path.ismount', return_value=True):
        return_value = alphacopy.external_disks(root)
    assert len(return_value) == len(folders)
    assert set(return_value) == {os.path.join(root, f) for f in folders}


def test_external_disks_src_with_some_folders_mounted(random_tree):
    for root, folders, files in os.walk(random_tree):
        if len(folders) > 1:
            break
    folders = folders[::2]
    side_effect = itertools.cycle((True, False))
    with patch('alphacopy.copy.os.path.ismount', side_effect=side_effect):
        return_value = alphacopy.external_disks(root)
    assert len(return_value) == len(folders)
    assert set(return_value) == {os.path.join(root, f) for f in folders}
