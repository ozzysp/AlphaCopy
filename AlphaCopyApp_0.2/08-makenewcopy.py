# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '08-makenewcopy.ui'
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
        self.newCopyWdg = QtWidgets.QWidget(MainWindow)
        self.newCopyWdg.setObjectName("newCopyWdg")
        self.darkBG = QtWidgets.QFrame(self.newCopyWdg)
        self.darkBG.setGeometry(QtCore.QRect(10, 10, 420, 260))
        self.darkBG.setStyleSheet("QFrame{\n"
"    background-color: rgb(46, 48, 59);\n"
"    color:rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.darkBG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.darkBG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.darkBG.setObjectName("darkBG")
        self.newCoyPB = QtWidgets.QPushButton(self.darkBG)
        self.newCoyPB.setGeometry(QtCore.QRect(80, 100, 251, 61))
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
        self.ejectedLb = QtWidgets.QLabel(self.darkBG)
        self.ejectedLb.setGeometry(QtCore.QRect(0, 50, 421, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.ejectedLb.setFont(font)
        self.ejectedLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.ejectedLb.setAlignment(QtCore.Qt.AlignCenter)
        self.ejectedLb.setObjectName("ejectedLb")
        MainWindow.setCentralWidget(self.newCopyWdg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.newCoyPB.setText(_translate("MainWindow", "Make New Copy"))
        self.newCoyPB.setShortcut(_translate("MainWindow", "Return"))
        self.ejectedLb.setText(_translate("MainWindow", "<strong>EJECTED DEVICES"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

