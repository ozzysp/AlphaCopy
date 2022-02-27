import os
import shutil
from PyQt5.QtCore import QObject, pyqtSignal
from datetime import datetime


class DevicesUtil(QObject):
    file_copied = pyqtSignal()
    VOLUMES_PATH = ''

    def __init__(self):
        super(QObject, self).__init__()
        self.VOLUMES_PATH = '/media/' + os.environ.get('USER')

    def list_disks(self):
        directories = []
        try:
            directories = os.listdir(self.VOLUMES_PATH)
        except FileNotFoundError:
            pass
        return directories

    def disk_size(self, label):
        total, used, free = shutil.disk_usage(self.VOLUMES_PATH + '/' + label)
        return total // (2 ** 30)

    def list_files(self, dir):
        files = os.listdir(dir)
        return files

    def copy_files(self, src, dest):
        try:
            files = self.list_files(src)
            dest = self.make_dir(dest)
        except Exception as e:
            raise e
            return
        for file in files:
            shutil.copy(src + '/' + file, dest + '/' + file)
            self.file_copied.emit()

    def make_dir(self, base_path):
        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H:%M")
        os.chdir(base_path)
        new_folder = dt_string
        os.mkdir(new_folder)
        return base_path + '/' + new_folder

    def eject_disk(self, label):
        command = "umount " + self.VOLUMES_PATH + "/" + label
        return os.system(command) == 0
