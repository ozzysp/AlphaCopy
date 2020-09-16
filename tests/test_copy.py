import os
import alphacopy
import filecmp


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
	assert filecmp.cmp(src, dst) == True
	os.remove(dst)

def test_copy_img():
	src = "tests/image_test.jpg"
	dst = "copied_image"
	alphacopy.copy_file(src, dst)
	assert os.path.exists(dst)
	assert filecmp.cmp(src, dst) == True
	os.remove(dst)