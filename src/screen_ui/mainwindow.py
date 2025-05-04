import sys
import os
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from alphacopy.devicesutil import DevicesUtil

class MainWindow(QMainWindow):
    devices = DevicesUtil()
    sd_label = ''
    hdd_label = ''

    def __init__(self):
        super().__init__()
        if hasattr(sys, '_MEIPASS'):
            base_dir = sys._MEIPASS
            ui_path = os.path.join(base_dir, "screen_ui", "mainwindow.ui")
        else:
            base_dir = os.path.dirname(os.path.abspath(__file__))
            ui_path = os.path.join(base_dir, "mainwindow.ui")
        uic.loadUi(ui_path, self)
        logo = QPixmap(os.path.join(base_dir, '../assets/logos/alphaletter.png'))
        self.logoLabel.setPixmap(logo.scaled(QSize(110, 70)))
        hddIcon = QPixmap(os.path.join(base_dir, '../assets/devices/usb-black.png'))
        self.hddIconLb.setPixmap(hddIcon.scaled(QSize(64, 64)))
        sdIcon = QPixmap(os.path.join(base_dir, '../assets/devices/Sycamoreent-Storage-Sd.png'))
        self.sdIconLb.setPixmap(sdIcon.scaled(QSize(64, 64)))
        self.stackedWidget.setCurrentIndex(0)

    def scan(self):
        disks = self.devices.list_disks()
        if len(disks) > 0:
            self.stackedWidget.setCurrentIndex(2)
            self.set_sd_hdd(disks)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def set_sd_hdd(self, disks):
        sd_found = False
        for disk in disks:
            size = self.devices.disk_size(disk)
            if size < 65:
                sd_found = True
                self.sd_label = disk
            else:
                self.hdd_label = disk

        if sd_found:
            self.hddLE.setText(self.hdd_label)
            self.sdLE.setText(self.sd_label)
        else:
            errorMessage = "A suitable SD card could not be found."
            self.notFoundDescriptionLb.setText(errorMessage)
            self.stackedWidget.setCurrentIndex(1)

    def copy(self):
        self.stackedWidget.setCurrentIndex(3)
        sd_path = self.devices.volumes_path + '/' + self.sd_label
        hdd_path = self.devices.volumes_path + '/' + self.hdd_label
        try:
            total_files = len(self.devices.list_files(sd_path))
        except Exception:
            self.stackedWidget.setCurrentIndex(5)
            return
        self.copyProgrB.setMaximum(total_files)

        def incrementProgressBar():
            currentValue = self.copyProgrB.value()
            self.copyProgrB.setValue(currentValue + 1)

        files = self.devices.list_files(sd_path)

        self.devices.file_copied.connect(incrementProgressBar)
        #try:
        self.devices.copy_files(files, hdd_path)
        #except Exception:
        self.stackedWidget.setCurrentIndex(5)
        self.stackedWidget.setCurrentIndex(4)

    def done(self):
        self.stackedWidget.setCurrentIndex(6)

    def eject(self):
        self.devices.eject_disk(self.sd_label)
        self.stackedWidget.setCurrentIndex(0)

    def abort_copy(self):
        pass
