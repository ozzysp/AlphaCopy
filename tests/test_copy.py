import pytest
import filecmp
from .utils import *
from alphacopy.devicesutil import DevicesUtil

devices = DevicesUtil("test_user")


def test_copy_file(random_file):
    src = random_file
    dst = 'output_file'
    devices.copy_file(src, dst)

    assert os.path.exists(dst)
    assert filecmp.cmp(src, dst)

    os.remove(dst)


def test_compare_hash(random_file):

    src = random_file
    dst = 'output_file'
    devices.copy_file(src, dst)

    # Check if the hash is the same
    assert devices.compare_hash(src, dst) is True

    # Change the dst contents and see if the hash is different
    write_random_data_to_file(dst, 1000)
    assert devices.compare_hash(src, dst) is False

    # Clean up
    os.remove(dst)


def test_list_disks(tmpdir):

    # Make a temporary volumes path
    volumes_path = tmpdir / "test_user"
    devices.volumes_path = volumes_path
    os.mkdir(volumes_path)

    # Make sure it exists
    assert os.path.exists(volumes_path)

    test_disks = ["test_disk_1", "test_disk_2"]

    for test_disk in test_disks:
        test_disk_path = volumes_path / test_disk
        os.mkdir(test_disk_path)

    disks = devices.list_disks()

    assert len(disks) == len(test_disks)

    for disk in disks:
        assert disk in test_disks

    shutil.rmtree(volumes_path)
