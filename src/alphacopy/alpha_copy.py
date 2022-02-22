#!/usr/bin/env python3

import os
import shutil
import psutil
from checksumdir import dirhash
from datetime import datetime
from pathlib import Path
from humanize import naturalsize

VOLUMES_PATH = '/media/pi/'


# This class defines devices functions and charateristics
class Devices:
    SIZE = 0
    REM_SIZE = 0
    DATE = '00/00/0000'

    # This function list all volumes mounted in system
    @staticmethod
    def list_disks():
        directories = os.listdir(VOLUMES_PATH)
        return directories

    # This function returns used space in choosed hd
    @staticmethod
    def used_disk():
        used_disk = psutil.disk_usage(VOLUMES_PATH)
        used_space = str(used_disk[1])
        used_bytes = str(used_space[:6])
        natural_bytes = (naturalsize(used_bytes))
        return natural_bytes

    # This function display free space in chosen hd
    @staticmethod
    def free_disk():
        free_disk = psutil.disk_usage(VOLUMES_PATH)
        free_space = str(free_disk[2])
        free_bytes: str = free_space[:3]
        info_free = (free_bytes + ' GB Free')
        return info_free

    # This function select each hd
    def select_from(self):
        # found_volumes = directories
        # return found_volumes
        pass

    # This function make new directory in target hd
    @staticmethod
    def make_new_dir():
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H:%M")
        path = '/Users/ozz/Desktop'
        os.chdir(path)
        new_folder = dt_string
        os.mkdir(new_folder)

    # This function copy all content from original hd to destination hd
    @staticmethod
    def copy_files(src: str, dst: str):
        shutil.copy2(src, dst)
        with open(dst, 'a') as f:
            os.fsync(f)

# This function show progress bar bytes
        def progress_bar_be():
            try:
                while True:
                    file_copy = (sum([f.stat().st_size for f in Path('/media/pi/').glob("**/*")]))
                    file_origin = (sum([f.stat().st_size for f in Path('/media/pi/new').glob("**/*")]))
                    if file_origin == file_copy:
                        break
            except FileNotFoundError:
                pass

        # This function checks integrity of copied files
        def check_hashes(self):
            directoryin = '/media/pi/'
            directoryout = '/media/pi/'
            md5hashin = dirhash(directoryin, 'md5')
            md5hashout = dirhash(directoryout, 'md5')
            if md5hashin == md5hashout:
                print('This copy is ok')
            else:
                print('Error while copying')

# This function eject all devices on mount point
        def eject_usb(self):
            command = "sudo udevadm info -q path -p /devices/pci0000:00/0000:00:1d.0/usb1/1-3/1-3.2/1-3.2.2/1-3.2.2.2/1-3.2.2.2:1.0/"
            popen = os.popen(command)
            output = popen.read()
            popen.close()
            output = output.split()
            output = output[1]
            if os.path.exists(output):
                os.remove(output)
                return output


def threading():
    pass


# This function eject all devices on mount point
def eject_usb():
    command = "sudo udevadm info -q path -p /devices/pci0000:00/0000:00:1d.0/usb1/1-3/1-3.2/1-3.2.2/1-3.2.2.2/1-3.2.2.2:1.0/"
    popen = os.popen(command)
    output = popen.read()
    popen.close()
    output = output.split()
    output = output[1]
    if os.path.exists(output):
        os.remove(output)
        return output


# Call class
devices = Devices()





# **** Old code for future use ****

# def copy_file(src: str, dst: str):
#     """Copies single file from src to dst"""
#     shutil.copy2(src, dst)
#     with open(dst, 'a') as f:
#         os.fsync(f)

# def check_disks(src: str, dst: str) -> bool:
#     """
#     Checks whether filesystem on "dst" has enough free space for "src" files
#     """
#     src_disk_usage = shutil.disk_usage(src)[1]
#     destinaton_disk_free = shutil.disk_usage(dst)[2]
#     return src_disk_usage <= destinaton_disk_free
#
#
# def external_disks(src: str = '/media/pi/'):
#     """
#     Find directories that are mounted on the given folder
#     Raises a ValueError if the given folder doesn't exists
#     Raises a ValueError if the given folder is, actually, a file
#     src -> str
#         The given folder in which this function should scan
#     returns: list[str]
#         Each element in the list is a string with the full path of the folder
#         A empty list means that no folder was found
#     """
#     return
