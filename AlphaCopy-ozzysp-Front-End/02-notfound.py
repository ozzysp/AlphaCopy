# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '02-notfound.ui'
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
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alphaletter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("alphaletter.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.notFoundDevicesWdg = QtWidgets.QWidget(MainWindow)
        self.notFoundDevicesWdg.setObjectName("notFoundDevicesWdg")
        self.darkBG = QtWidgets.QFrame(self.notFoundDevicesWdg)
        self.darkBG.setGeometry(QtCore.QRect(10, 10, 420, 260))
        self.darkBG.setStyleSheet("QFrame{\n"
"    background-color: rgb(46, 48, 59);\n"
"    color:rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.darkBG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.darkBG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.darkBG.setObjectName("darkBG")
        self.scanAgainPB = QtWidgets.QPushButton(self.darkBG)
        self.scanAgainPB.setGeometry(QtCore.QRect(80, 100, 251, 61))
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
        self.notFoundLb = QtWidgets.QLabel(self.darkBG)
        self.notFoundLb.setGeometry(QtCore.QRect(10, 50, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.notFoundLb.setFont(font)
        self.notFoundLb.setStyleSheet("color: rgb(255, 0, 4);")
        self.notFoundLb.setAlignment(QtCore.Qt.AlignCenter)
        self.notFoundLb.setObjectName("notFoundLb")
        MainWindow.setCentralWidget(self.notFoundDevicesWdg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlphaCopy"))
        self.scanAgainPB.setText(_translate("MainWindow", "Scan Again"))
        self.scanAgainPB.setShortcut(_translate("MainWindow", "Return"))
        self.notFoundLb.setText(_translate("MainWindow", "<strong>DEVICES NOT FOUND"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

