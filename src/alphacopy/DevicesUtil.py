import os
import shutil
from PyQt5.QtCore import QObject, pyqtSignal


class DevicesUtil(QObject):
    copying_started = pyqtSignal()
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
        return total // (2**30)

    def list_files(self, dir):
        files = os.listdir(dir)
        return files

    def copy_files(self, src, dest):
        files = self.list_files(src)
        self.copying_started.emit()
        for file in files:
            shutil.copy(src + '/' + file, dest + '/' + file)
            self.file_copied.emit()
