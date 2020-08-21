# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '01-alphacopyproject.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_GreettingScreen(object):
    def setupUi(self, GreettingScreen):
        GreettingScreen.setObjectName("GreettingScreen")
        GreettingScreen.resize(440, 280)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(GreettingScreen.sizePolicy().hasHeightForWidth())
        GreettingScreen.setSizePolicy(sizePolicy)
        GreettingScreen.setMinimumSize(QtCore.QSize(440, 280))
        GreettingScreen.setMaximumSize(QtCore.QSize(440, 280))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("alphaletter.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon.addPixmap(QtGui.QPixmap("alphaletter.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        icon.addPixmap(QtGui.QPixmap("alphaletter.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        GreettingScreen.setWindowIcon(icon)
        self.splashWdg = QtWidgets.QWidget(GreettingScreen)
        self.splashWdg.setObjectName("splashWdg")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.splashWdg)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.darkBG = QtWidgets.QFrame(self.splashWdg)
        self.darkBG.setStyleSheet("QFrame{\n"
"    background-color: rgb(46, 48, 59);\n"
"    color:rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.darkBG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.darkBG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.darkBG.setObjectName("darkBG")
        self.appTitle = QtWidgets.QLabel(self.darkBG)
        self.appTitle.setGeometry(QtCore.QRect(0, 10, 421, 61))
        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(30)
        self.appTitle.setFont(font)
        self.appTitle.setStyleSheet("color: rgb(33, 188, 162);")
        self.appTitle.setAlignment(QtCore.Qt.AlignCenter)
        self.appTitle.setObjectName("appTitle")
        self.openSourceLb = QtWidgets.QLabel(self.darkBG)
        self.openSourceLb.setGeometry(QtCore.QRect(0, 70, 421, 21))
        font = QtGui.QFont()
        font.setFamily("Laksaman")
        font.setPointSize(10)
        self.openSourceLb.setFont(font)
        self.openSourceLb.setStyleSheet("color: rgb(143, 66, 231);")
        self.openSourceLb.setAlignment(QtCore.Qt.AlignCenter)
        self.openSourceLb.setObjectName("openSourceLb")
        self.devicesProgB = QtWidgets.QProgressBar(self.darkBG)
        self.devicesProgB.setGeometry(QtCore.QRect(30, 200, 361, 23))
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
        self.loadingDevicesLb = QtWidgets.QLabel(self.darkBG)
        self.loadingDevicesLb.setGeometry(QtCore.QRect(0, 230, 421, 21))
        font = QtGui.QFont()
        font.setFamily("DejaVu Sans")
        font.setPointSize(10)
        self.loadingDevicesLb.setFont(font)
        self.loadingDevicesLb.setStyleSheet("color: rgb(33, 188, 162);")
        self.loadingDevicesLb.setAlignment(QtCore.Qt.AlignCenter)
        self.loadingDevicesLb.setObjectName("loadingDevicesLb")
        self.label = QtWidgets.QLabel(self.darkBG)
        self.label.setGeometry(QtCore.QRect(110, 100, 191, 81))
        self.label.setStyleSheet("image: url(:/logo/alphaletter.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.darkBG)
        GreettingScreen.setCentralWidget(self.splashWdg)

        self.retranslateUi(GreettingScreen)
        QtCore.QMetaObject.connectSlotsByName(GreettingScreen)

    def retranslateUi(self, GreettingScreen):
        _translate = QtCore.QCoreApplication.translate
        GreettingScreen.setWindowTitle(_translate("GreettingScreen", "AlphaCopy"))
        self.appTitle.setText(_translate("GreettingScreen", "<strong>Alpha</strong>Copy"))
        self.openSourceLb.setText(_translate("GreettingScreen", "<strong>OPEN SOURCE</strong> PROJECT"))
        self.loadingDevicesLb.setText(_translate("GreettingScreen", "<strong>LOADING</strong> DEVICES..."))

import alphaletter


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    GreettingScreen = QtWidgets.QMainWindow()
    ui = Ui_GreettingScreen()
    ui.setupUi(GreettingScreen)
    GreettingScreen.show()
    sys.exit(app.exec_())

