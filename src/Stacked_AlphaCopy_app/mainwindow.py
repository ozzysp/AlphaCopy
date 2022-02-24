from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QSize
from alphacopy.alpha_copy import Devices


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('Stacked_AlphaCopy_app/mainwindow.ui', self)
        hddIcon = QPixmap('Stacked_AlphaCopy_app/usb-black.png')
        self.hddIconLb.setPixmap(hddIcon.scaled(QSize(64, 64)))
        sdIcon = QPixmap('Stacked_AlphaCopy_app/Sycamoreent-Storage-Sd.png')
        self.sdIconLb.setPixmap(sdIcon.scaled(QSize(64, 64)))
        self.scan()

    def scan(self):
        disks = Devices.list_disks()
        if len(disks) > 0:
            self.stackedWidget.setCurrentIndex(2)
        else:
            self.stackedWidget.setCurrentIndex(1)


