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


def scan_disks():
    """
    Find USB devices
    """
    dev = usb.core.find(find_all=True)
    # loop through devices, printing vendor and product ids in decimal and hex
    for cfg in dev:
        sys.stdout.write('Hexadecimal VendorID=' + hex(cfg.idVendor) + ' & ProductID=' + hex(cfg.idProduct) + '\n\n')
