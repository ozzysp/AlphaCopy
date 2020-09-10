import os
import alphacopy


def test_copy_ok():
	file_from = "tests/helloworld"
	file_to = "HiPeople"
	alphacopy.copy(file_from, file_to)
	assert os.path.exists(file_to)
	with open(file_to) as f:
		assert f.read() == "Hello world"
	os.remove(file_to)