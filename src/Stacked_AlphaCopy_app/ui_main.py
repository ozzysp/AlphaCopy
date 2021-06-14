# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_main.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 280)
        MainWindow.setMinimumSize(QtCore.QSize(480, 280))
        MainWindow.setMaximumSize(QtCore.QSize(480, 280))
        MainWindow.setStyleSheet("background-color: rgb(46, 48, 59);\n"
"color:rgb(220, 220, 220);\n"
"border-radius: 10px;")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.initPage = QtWidgets.QWidget()
        self.initPage.setObjectName("initPage")
        self.appTitle = QtWidgets.QLabel(self.initPage)
        self.appTitle.setGeometry(QtCore.QRect(20, 10, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(30)
        self.appTitle.setFont(font)
        self.appTitle.setStyleSheet("color: rgb(33, 188, 162);")
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setObjectName("appTitle")
        self.label = QtWidgets.QLabel(self.initPage)
        self.label.setGeometry(QtCore.QRect(130, 100, 191, 81))
        self.label.setStyleSheet("image: url(:/alphaletter/alphaletter.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.loadingDevicesLb = QtWidgets.QLabel(self.initPage)
        self.loadingDevicesLb.setGeometry(QtCore.QRect(20, 230, 421, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.loadingDevicesLb.setFont(font)
        self.loadingDevicesLb.setStyleSheet("color: rgb(33, 188, 162);")
        self.loadingDevicesLb.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingDevicesLb.setObjectName("loadingDevicesLb")
        self.openSourceLb = QtWidgets.QLabel(self.initPage)
        self.openSourceLb.setGeometry(QtCore.QRect(20, 70, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(10)
        self.openSourceLb.setFont(font)
        self.openSourceLb.setStyleSheet("color: rgb(143, 66, 231);")
        self.openSourceLb.setAlignment(QtCore.Qt.AlignCenter)
        self.openSourceLb.setObjectName("openSourceLb")
        self.devicesProgB = QtWidgets.QProgressBar(self.initPage)
        self.devicesProgB.setGeometry(QtCore.QRect(50, 200, 361, 23))
        self.devicesProgB.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(100, 130, 200);\n"
"    color: rgb(230, 230, 230);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0138249 rgba(0, 0, 0, 255), stop:0.0184332 rgba(143, 66, 231, 255), stop:0.976959 rgba(14, 218, 195, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.devicesProgB.setProperty("value", 36)
        self.devicesProgB.setObjectName("devicesProgB")
        self.stackedWidget.addWidget(self.initPage)
        self.devNotFound = QtWidgets.QWidget()
        self.devNotFound.setObjectName("devNotFound")
        self.notFoundLb = QtWidgets.QLabel(self.devNotFound)
        self.notFoundLb.setGeometry(QtCore.QRect(30, 50, 401, 41))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.notFoundLb.sizePolicy().hasHeightForWidth())
        self.notFoundLb.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.notFoundLb.setFont(font)
        self.notFoundLb.setStyleSheet("color: rgb(255, 0, 4);")
        self.notFoundLb.setAlignment(QtCore.Qt.AlignCenter)
        self.notFoundLb.setObjectName("notFoundLb")
        self.scanAgainPB = QtWidgets.QPushButton(self.devNotFound)
        self.scanAgainPB.setGeometry(QtCore.QRect(100, 130, 251, 61))
        self.scanAgainPB.setStyleSheet("QPushButton {\n"
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
        self.scanAgainPB.setAutoDefault(False)
        self.scanAgainPB.setObjectName("scanAgainPB")
        self.stackedWidget.addWidget(self.devNotFound)
        self.foundDevs = QtWidgets.QWidget()
        self.foundDevs.setObjectName("foundDevs")
        self.foundDevicesLb = QtWidgets.QLabel(self.foundDevs)
        self.foundDevicesLb.setGeometry(QtCore.QRect(10, 20, 421, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.foundDevicesLb.setFont(font)
        self.foundDevicesLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.foundDevicesLb.setAlignment(QtCore.Qt.AlignCenter)
        self.foundDevicesLb.setObjectName("foundDevicesLb")
        self.diskHDDimg = QtWidgets.QFrame(self.foundDevs)
        self.diskHDDimg.setGeometry(QtCore.QRect(272, 59, 120, 71))
        self.diskHDDimg.setStyleSheet("image: url(:/alphaletter/usb-black.png);")
        self.diskHDDimg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.diskHDDimg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.diskHDDimg.setObjectName("diskHDDimg")
        self.arrowLb = QtWidgets.QLabel(self.foundDevs)
        self.arrowLb.setGeometry(QtCore.QRect(182, 80, 79, 31))
        font = QtGui.QFont()
        font.setPointSize(40)
        self.arrowLb.setFont(font)
        self.arrowLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.arrowLb.setAlignment(QtCore.Qt.AlignCenter)
        self.arrowLb.setObjectName("arrowLb")
        self.sdLE = QtWidgets.QLineEdit(self.foundDevs)
        self.sdLE.setGeometry(QtCore.QRect(60, 130, 113, 27))
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
        self.makeCopyPB = QtWidgets.QPushButton(self.foundDevs)
        self.makeCopyPB.setGeometry(QtCore.QRect(100, 170, 251, 61))
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
        self.hdLE = QtWidgets.QLineEdit(self.foundDevs)
        self.hdLE.setGeometry(QtCore.QRect(280, 130, 113, 27))
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
        self.cardSDImg = QtWidgets.QFrame(self.foundDevs)
        self.cardSDImg.setGeometry(QtCore.QRect(52, 50, 120, 81))
        self.cardSDImg.setStyleSheet("image: url(:/alphaletter/Sycamoreent-Storage-Sd.png);")
        self.cardSDImg.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cardSDImg.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cardSDImg.setObjectName("cardSDImg")
        self.stackedWidget.addWidget(self.foundDevs)
        self.progBar = QtWidgets.QWidget()
        self.progBar.setObjectName("progBar")
        self.copyingFileLb = QtWidgets.QLabel(self.progBar)
        self.copyingFileLb.setGeometry(QtCore.QRect(30, 50, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copyingFileLb.setFont(font)
        self.copyingFileLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.copyingFileLb.setAlignment(QtCore.Qt.AlignCenter)
        self.copyingFileLb.setObjectName("copyingFileLb")
        self.copyProgrB = QtWidgets.QProgressBar(self.progBar)
        self.copyProgrB.setGeometry(QtCore.QRect(40, 120, 381, 71))
        self.copyProgrB.setStyleSheet("QProgressBar {\n"
"    background-color: rgb(100, 130, 200);\n"
"    color: rgb(230, 230, 230);\n"
"    border-style: none;\n"
"    border-radius: 35px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk{\n"
"    border-radius: 35px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0138249 rgba(0, 0, 0, 255), stop:0.0184332 rgba(143, 66, 231, 255), stop:0.976959 rgba(14, 218, 195, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.copyProgrB.setMinimum(0)
        self.copyProgrB.setProperty("value", 54)
        self.copyProgrB.setObjectName("copyProgrB")
        self.stackedWidget.addWidget(self.progBar)
        self.successCopy = QtWidgets.QWidget()
        self.successCopy.setObjectName("successCopy")
        self.SuccesfulLb = QtWidgets.QLabel(self.successCopy)
        self.SuccesfulLb.setGeometry(QtCore.QRect(30, 50, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.SuccesfulLb.setFont(font)
        self.SuccesfulLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.SuccesfulLb.setAlignment(QtCore.Qt.AlignCenter)
        self.SuccesfulLb.setObjectName("SuccesfulLb")
        self.DonePB = QtWidgets.QPushButton(self.successCopy)
        self.DonePB.setGeometry(QtCore.QRect(100, 130, 251, 61))
        self.DonePB.setStyleSheet("QPushButton {\n"
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
        self.DonePB.setObjectName("DonePB")
        self.stackedWidget.addWidget(self.successCopy)
        self.errorsFound = QtWidgets.QWidget()
        self.errorsFound.setObjectName("errorsFound")
        self.errorDonePB = QtWidgets.QPushButton(self.errorsFound)
        self.errorDonePB.setGeometry(QtCore.QRect(100, 130, 251, 61))
        self.errorDonePB.setStyleSheet("QPushButton {\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:0.0138249 rgba(0, 0, 0, 255), stop:0.0184332 rgba(143, 66, 231, 255), stop:0.976959 rgba(14, 218, 195, 255), stop:1 rgba(255, 255, 255, 255));\n"
"    color: rgb(255, 0, 4);\n"
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
        self.errorDonePB.setObjectName("errorDonePB")
        self.errorsFoundLb = QtWidgets.QLabel(self.errorsFound)
        self.errorsFoundLb.setGeometry(QtCore.QRect(30, 50, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.errorsFoundLb.setFont(font)
        self.errorsFoundLb.setStyleSheet("color: rgb(255, 0, 4);")
        self.errorsFoundLb.setAlignment(QtCore.Qt.AlignCenter)
        self.errorsFoundLb.setObjectName("errorsFoundLb")
        self.stackedWidget.addWidget(self.errorsFound)
        self.ejectDevs = QtWidgets.QWidget()
        self.ejectDevs.setObjectName("ejectDevs")
        self.ejectPB = QtWidgets.QPushButton(self.ejectDevs)
        self.ejectPB.setGeometry(QtCore.QRect(100, 90, 251, 61))
        self.ejectPB.setStyleSheet("QPushButton {\n"
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
        self.ejectPB.setObjectName("ejectPB")
        self.stackedWidget.addWidget(self.ejectDevs)
        self.newCopy = QtWidgets.QWidget()
        self.newCopy.setObjectName("newCopy")
        self.newCoyPB = QtWidgets.QPushButton(self.newCopy)
        self.newCoyPB.setGeometry(QtCore.QRect(100, 120, 251, 61))
        self.newCoyPB.setStyleSheet("QPushButton {\n"
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
        self.newCoyPB.setObjectName("newCoyPB")
        self.ejectedLb = QtWidgets.QLabel(self.newCopy)
        self.ejectedLb.setGeometry(QtCore.QRect(20, 50, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ejectedLb.setFont(font)
        self.ejectedLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.ejectedLb.setAlignment(QtCore.Qt.AlignCenter)
        self.ejectedLb.setObjectName("ejectedLb")
        self.stackedWidget.addWidget(self.newCopy)
        self.horizontalLayout.addWidget(self.stackedWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.appTitle.setText(_translate("MainWindow", "<strong>Alpha</strong>Copy"))
        self.loadingDevicesLb.setText(_translate("MainWindow", "<strong>LOADING</strong> DEVICES..."))
        self.openSourceLb.setText(_translate("MainWindow", "<strong>OPEN SOURCE</strong> PROJECT"))
        self.notFoundLb.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">DEVICES NOT FOUND!</span></p></body></html>"))
        self.scanAgainPB.setText(_translate("MainWindow", "Scan Again?"))
        self.scanAgainPB.setShortcut(_translate("MainWindow", "Return"))
        self.foundDevicesLb.setText(_translate("MainWindow", "<strong>FOUND DEVICES"))
        self.arrowLb.setText(_translate("MainWindow", ">"))
        self.sdLE.setPlaceholderText(_translate("MainWindow", "SD Label"))
        self.makeCopyPB.setText(_translate("MainWindow", "Make Copy"))
        self.makeCopyPB.setShortcut(_translate("MainWindow", "Return"))
        self.hdLE.setPlaceholderText(_translate("MainWindow", "HDD Label"))
        self.copyingFileLb.setText(_translate("MainWindow", "<strong>COPYING FILES..."))
        self.SuccesfulLb.setText(_translate("MainWindow", "<STRONG>SUCCESFUL COPY"))
        self.DonePB.setText(_translate("MainWindow", "Done"))
        self.DonePB.setShortcut(_translate("MainWindow", "Return"))
        self.errorDonePB.setText(_translate("MainWindow", "Done!"))
        self.errorDonePB.setShortcut(_translate("MainWindow", "Return"))
        self.errorsFoundLb.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">ERRORS FOUND!</span></p></body></html>"))
        self.ejectPB.setText(_translate("MainWindow", "Eject Devices"))
        self.ejectPB.setShortcut(_translate("MainWindow", "Return"))
        self.newCoyPB.setText(_translate("MainWindow", "Make New Copy"))
        self.newCoyPB.setShortcut(_translate("MainWindow", "Return"))
        self.ejectedLb.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-weight:600;\">EJECTED DEVICES</span></p></body></html>"))

import logoalpha

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

