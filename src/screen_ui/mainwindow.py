from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from alphacopy.DevicesUtil import DevicesUtil


class MainWindow(QMainWindow):
    devices = DevicesUtil()
    sd_label = ''
    hdd_label = ''

    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('screen_ui/mainwindow.ui', self)
        logo = QPixmap('screen_ui/alphaletter.png')
        self.logoLabel.setPixmap(logo.scaled(QSize(110, 70)))
        hddIcon = QPixmap('screen_ui/usb-black.png')
        self.hddIconLb.setPixmap(hddIcon.scaled(QSize(64, 64)))
        sdIcon = QPixmap('screen_ui/Sycamoreent-Storage-Sd.png')
        self.sdIconLb.setPixmap(sdIcon.scaled(QSize(64, 64)))
        self.scan()

    def scan(self):
        disks = self.devices.list_disks()
        if len(disks) > 0:
            self.stackedWidget.setCurrentIndex(2)
            self.set_sd_hdd(disks)
        else:
            self.stackedWidget.setCurrentIndex(1)

    def set_sd_hdd(self, disks):
        for disk in disks:
            size = self.devices.disk_size(disk)
            if size < 65:
                self.sd_label = disk
            else:
                self.hdd_label = disk
        self.hddLE.setText(self.hdd_label)
        self.sdLE.setText(self.sd_label)

    def copy(self):
        self.stackedWidget.setCurrentIndex(3)
        sd_path = self.devices.VOLUMES_PATH + '/' + self.sd_label
        hdd_path = self.devices.VOLUMES_PATH + '/' + self.hdd_label
        total_files = len(self.devices.list_files(sd_path))
        self.copyProgrB.setMaximum(total_files)

        def incrementProgressBar():
            currentValue = self.copyProgrB.value()
            self.copyProgrB.setValue(currentValue + 1)

        self.devices.file_copied.connect(incrementProgressBar)
        self.devices.copy_files(sd_path, hdd_path)
        self.stackedWidget.setCurrentIndex(4)

    def done(self):
        self.stackedWidget.setCurrentIndex(6)

    def eject(self):
        self.devices.eject_disk(self.sd_label)
        self.stackedWidget.setCurrentIndex(0)
