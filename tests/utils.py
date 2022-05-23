import os
import uuid
import shutil
import random
import pytest


@pytest.fixture(scope='function')
def random_tree(tmpdir):
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

    root = tmpdir
    os.makedirs(root)
    try:
        create_folders(root, 3)
        yield root
    except:  # noqa E722
        raise
    finally:
        shutil.rmtree(root)


@pytest.fixture(scope='function')
def random_file(tmpdir):
    try:
        filename = create_random_file(tmpdir)
        yield filename
    except:  # noqa E722
        raise
    finally:
        try:
            os.remove(filename)
        except:  # noqa E722
            pass


def create_random_file(tmpdir):
    """
    This function create a random file at a given location
    The file size ranges from 1 byte to 1 KB
    The function returns a tuple with filename and filesize
    """
    filename = tmpdir / str(uuid.uuid4())
    filesize = random.randint(1, 1024)  # file up to 1 MB
    write_random_data_to_file(filename, filesize)
    return filename


def write_random_data_to_file(filename, size):
    """
    This functions writes random data to file
    """
    with open(filename, 'wb') as f:
        f.write(os.urandom(size))
