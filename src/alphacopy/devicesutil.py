import os
import shutil
import psutil
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime
from humanize import naturalsize
from pathlib import Path


class DevicesUtil(QObject):
    file_copied = pyqtSignal()
    volumes_path = ''

    def __init__(self):
        super(QObject, self).__init__()
        self.volumes_path = '/media/' + os.environ.get('USER')

    def list_disks(self):
        directories = []
        try:
            directories = os.listdir(self.volumes_path)
        except FileNotFoundError:
            pass
        return directories

    def disk_size(self, label):
        total, used, free = shutil.disk_usage(self.volumes_path + '/' + label)
        return total // (2 ** 30)

    def list_files(self, dir):
        files = [str(item) for item in list(Path(dir).rglob("*"))]
        return files

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
                shutil.copy2(file, dest_path)
                self.file_copied.emit()
            else:
                path.mkdir(exist_ok=True)

    # Creates a new directory in the target disk with current date and hour
    # by @ozzysp, with later modifications by @nicmorais
    def make_dir(self, base_path):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H:%M")
        os.chdir(base_path)
        new_folder = dt_string
        os.mkdir(new_folder)
        return base_path + '/' + new_folder

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
