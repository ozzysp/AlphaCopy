import os
import shutil
import psutil
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from humanize import naturalsize
from pathlib import Path
import hashlib


class DevicesUtil(QObject):
    file_copied = pyqtSignal()
    volumes_path = ''

    def __init__(self, user = os.environ.get('USER')):
        super(QObject, self).__init__()
        self.volumes_path = '/media/' + user

    # This function is used to get the list of all the volumes by @nicmorais
    def list_disks(self):
        directories = []
        try:
            directories = os.listdir(self.volumes_path)
        except FileNotFoundError:
            pass
        return directories

    # This function is used to get size in a volume by @nicmorais
    def disk_size(self, label):
        total, used, free = shutil.disk_usage(self.volumes_path + '/' + label)
        return total // (2 ** 30)

    # This function is used to get the list files in volume by @nicmorais
    def list_files(self, dir):
        files = [str(item) for item in list(Path(dir).rglob("*"))]
        return files

    def get_hash(self, filename):
        sha256_hash = hashlib.sha256()
        with open(filename, "rb") as f:
            # Read and update hash string value in blocks of 4K
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()

    def compare_hash(self, file1, file2):
        return self.get_hash(file1) == self.get_hash(file2)

    # This function copies all files from one volume to another by @nicmorais
    def copy_files(self, files, dest):
        try:
            dest = self.make_dir(dest)
        except Exception as e:
            raise e
            return
        for file in files:
            dest_path = dest + '/' + '/'.join(file.split('/')[4:])
            path = Path(dest_path)
            if Path(file).is_file():
                self.copy_file(file, dest_path)
            else:
                path.mkdir(exist_ok=True)

    # Creates a new directory in the target disk with current date and hour
    # by @ozzysp, with later modifications by @nicmorais
    def make_dir(self, base_path):
        now = datetime.now()
        dt_string = now.strftime('%Y_%m_%d_%H-%M-%S')
        os.chdir(base_path)
        new_folder = dt_string
        os.mkdir(base_path + '/' + new_folder)
        return base_path + '/' + new_folder

    def copy_file(self, file, dest_path):
        shutil.copy2(file, dest_path)
        if self.compare_hash(file, dest_path):
            self.file_copied.emit()
            return True
        else:
            error_msg = "Error: " + file
            raise Exception(error_msg)

    # Ejects disk by label (by @nicmorais)
    def eject_disk(self, label):
        command = "umount " + self.volumes_path + "/" + label
        return os.system(command) == 0

    # This function returns used space in choosed hdd (by @ozzysp)
    def used_disk(self):
        used_disk = psutil.disk_usage(self.volumes_path)
        used_space = str(used_disk[1])
        used_bytes = str(used_space[:6])
        natural_bytes = (naturalsize(used_bytes))
        return natural_bytes

    # This function display free space in chosen hdd (by @ozzysp)
    def free_disk(self):
        free_disk = psutil.disk_usage(self.volumes_path)
        free_space = str(free_disk[2])
        free_bytes: str = free_space[:3]
        info_free = (free_bytes + ' GB Free')
        return info_free
