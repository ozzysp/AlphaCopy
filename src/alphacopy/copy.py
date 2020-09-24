from shutil import copy2, disk_usage
from os import fsync


def copy_file(src: str, dst: str):
	"""Copies single file from src to dst"""
	copy2(src, dst)
	destin = open(dst, "a")
	fsync(destin)
	destin.close()

def check_disks(src, dst):
	src_disk_usage = disk_usage(src)[1]
	destinaton_disk_free = disk_usage(dst)[2]
	return src_disk_usage <= destinaton_disk_free

