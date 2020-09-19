from shutil import copy2

def copy_file(src: str, dst: str):
	"""Copies single file from src to dst"""
	copy2(src, dst)