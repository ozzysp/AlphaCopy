from shutil import copy2
# def copy_folder(folder_from: str, folder_to: str):
# 	"""Copies an entire tree folder from folder_from to folder_to"""

def copy_file(src: str, dst: str):
	"""Copies single file from file_from to file_to"""
	copy2(src, dst)

	# with open(file_from) as f_read:
	# 	with open(file_to, "w") as f_write:
	# 		f_write.write(f_read.read())