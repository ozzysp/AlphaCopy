# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '04-progress.ui'
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
        self.progressBarWdg = QtWidgets.QWidget(MainWindow)
        self.progressBarWdg.setObjectName("progressBarWdg")
        self.darkBG = QtWidgets.QFrame(self.progressBarWdg)
        self.darkBG.setGeometry(QtCore.QRect(10, 10, 420, 260))
        self.darkBG.setStyleSheet("QFrame{\n"
"    background-color: rgb(46, 48, 59);\n"
"    color:rgb(220, 220, 220);\n"
"    border-radius: 10px;\n"
"}")
        self.darkBG.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.darkBG.setFrameShadow(QtWidgets.QFrame.Raised)
        self.darkBG.setObjectName("darkBG")
        self.copyProgrB = QtWidgets.QProgressBar(self.darkBG)
        self.copyProgrB.setGeometry(QtCore.QRect(20, 90, 381, 71))
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
        self.copyingFileLb = QtWidgets.QLabel(self.darkBG)
        self.copyingFileLb.setGeometry(QtCore.QRect(10, 40, 401, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.copyingFileLb.setFont(font)
        self.copyingFileLb.setStyleSheet("color: rgb(35, 175, 136);")
        self.copyingFileLb.setAlignment(QtCore.Qt.AlignCenter)
        self.copyingFileLb.setObjectName("copyingFileLb")
        MainWindow.setCentralWidget(self.progressBarWdg)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "AlphaCopy"))
        self.copyingFileLb.setText(_translate("MainWindow", "<strong>COPYING FILES..."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

