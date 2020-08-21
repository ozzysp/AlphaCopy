# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '03-founddevices.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(440, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(440, 280))
        MainWindow.setMaximumSize(QtCore.QSize(440, 280))
        self.foundDevicesWdg = QtWidgets.QWidget(MainWindow)
        self.foundDevicesWdg.setObjectName("foundDevicesWdg")
        self.darkBG = QtWidgets.QFrame(self.foundDevicesWdg)
        self.darkBG.setGeometry(QtCore.QRect(10, 10, 420, 260))
        self.darkBG.setStyleSheet("QFrame{\n"
"    background-color: rgb(46, 48, 59);\n"
"    color:rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.darkBG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.darkBG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.darkBG.setObjectName("darkBG")
        self.diskHDDimg = QtWidgets.QFrame(self.darkBG)
        self.diskHDDimg.setGeometry(QtCore.QRect(260, 59, 120, 71))
        self.diskHDDimg.setStyleSheet("image: url(:/hdd/Icons/hdd.qrc);")
        self.diskHDDimg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diskHDDimg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diskHDDimg.setObjectName("diskHDDimg")
        self.arrowLb = QtWidgets.QLabel(self.darkBG)
        self.arrowLb.setGeometry(QtCore.QRect(170, 80, 79, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.arrowLb.setFont(font)
        self.arrowLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.arrowLb.setAlignment(QtCore.Qt.AlignCenter)
        self.arrowLb.setObjectName("arrowLb")
        self.cardSDImg = QtWidgets.QFrame(self.darkBG)
        self.cardSDImg.setGeometry(QtCore.QRect(40, 50, 120, 81))
        self.cardSDImg.setStyleSheet("image: url(:/sd/Icons/sd.qrc);")
        self.cardSDImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cardSDImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cardSDImg.setObjectName("cardSDImg")
        self.makeCopyPB = QtWidgets.QPushButton(self.darkBG)
        self.makeCopyPB.setGeometry(QtCore.QRect(79, 180, 251, 61))
        self.makeCopyPB.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0138249 rgba(0, 0, 0, 255), stop:0.0184332 rgba(143, 66, 231, 255), stop:0.976959 rgba(14, 218, 195, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 30px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton::pressed {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(222, 151, 255, 255), stop:1 rgba(54, 237, 216, 255));\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 30px;\n"
"    text-align: center;\n"
"}")
        self.makeCopyPB.setObjectName("makeCopyPB")
        self.foundDevicesLb = QtWidgets.QLabel(self.darkBG)
        self.foundDevicesLb.setGeometry(QtCore.QRect(-2, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.foundDevicesLb.setFont(font)
        self.foundDevicesLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.foundDevicesLb.setAlignment(QtCore.Qt.AlignCenter)
        self.foundDevicesLb.setObjectName("foundDevicesLb")
        self.sdLE = QtWidgets.QLineEdit(self.darkBG)
        self.sdLE.setGeometry(QtCore.QRect(40, 130, 113, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.sdLE.setFont(font)
        self.sdLE.setStyleSheet("QLineEdit {\n"
"    \n"
"    color: rgb(200, 200, 200);\n"
"    background-color: rgb(46, 48, 69);\n"
"\n"
"}")
        self.sdLE.setText("")
        self.sdLE.setAlignment(QtCore.Qt.AlignCenter)
        self.sdLE.setObjectName("sdLE")
        self.hdLE = QtWidgets.QLineEdit(self.darkBG)
        self.hdLE.setGeometry(QtCore.QRect(260, 130, 113, 27))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.hdLE.setFont(font)
        self.hdLE.setStyleSheet("QLineEdit {\n"
"    \n"
"    color: rgb(200, 200, 200);\n"
"    background-color: rgb(46, 48, 69);\n"
"\n"
"}")
        self.hdLE.setText("")
        self.hdLE.setAlignment(QtCore.Qt.AlignCenter)
        self.hdLE.setObjectName("hdLE")
        MainWindow.setCentralWidget(self.foundDevicesWdg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.arrowLb.setText(_translate("MainWindow", ">"))
        self.makeCopyPB.setText(_translate("MainWindow", "Make Copy"))
        self.makeCopyPB.setShortcut(_translate("MainWindow", "Return"))
        self.foundDevicesLb.setText(_translate("MainWindow", "<strong>FOUND DEVICES"))
        self.sdLE.setPlaceholderText(_translate("MainWindow", "SD Label"))
        self.hdLE.setPlaceholderText(_translate("MainWindow", "HDD Label"))

import devices

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

