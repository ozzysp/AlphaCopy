# !/usr/bin/python
from os import fsync
from shutil import copy2, disk_usage
import sys
import usb.core


def copy_file(src: str, dst: str):
    """Copies single file from src to dst"""
    copy2(src, dst)
    destin = open(dst, "a")
    fsync(destin)
    destin.close()


def check_disks(src: str, dst: str) -> bool:
    """
    Checks whether filesystem on "dst" has enough free space for "src" files
    """
    src_disk_usage = disk_usage(src)[1]
    destinaton_disk_free = disk_usage(dst)[2]
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
        A empy list means that no folder was found
    """
    return
