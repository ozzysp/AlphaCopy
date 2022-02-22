#!/usr/bin/env python3


import os
import shutil


def copy_file(src: str, dst: str):
    """Copies single file from src to dst"""
    shutil.copy2(src, dst)
    with open(dst, 'a') as f:
        os.fsync(f)


def check_disks(src: str, dst: str) -> bool:
    """
    Checks whether filesystem on "dst" has enough free space for "src" files
    """
    src_disk_usage = shutil.disk_usage(src)[1]
    destinaton_disk_free = shutil.disk_usage(dst)[2]
    return src_disk_usage <= destinaton_disk_free


def external_disks(src: str = '/media/pi/'):
    """
    Find directories that are mounted on the given folder
    Raises a ValueError if the given folder doesn't exists
    Raises a ValueError if the given folder is, actually, a file
    src -> str
        The given folder in which this function should scan
    returns: list[str]
        Each element in the list is a string with the full path of the folder
        A empty list means that no folder was found
    """
    return
