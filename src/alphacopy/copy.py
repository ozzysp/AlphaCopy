#!/usr/bin/python
import os
from shutil import copy2, disk_usage
import sys
import usb.core


def copy_file(src: str, dst: str):
    """Copies single file from src to dst"""
    copy2(src, dst)
    destin = open(dst, "a")
    fsync(destin)
    destin.close()


def check_space(src: str, dst: str) -> bool:
    """
    Checks whether filesystem on "dst" has enough free space for "src" files
    """
    src_disk_usage = disk_usage(src)[1]
    destinaton_disk_free = disk_usage(dst)[2]
    return src_disk_usage <= destinaton_disk_free

def scan_disks():
    """
    Check for all USB devices connected to de Raspberry PI ports
    """
    usb_devices = os.system("lsusb")
    print(usb_devices)

scan_disks()

