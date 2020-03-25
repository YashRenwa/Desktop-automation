# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CALIBRATE.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import os
import pyautogui as pg
import time

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(801, 658)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(620, 10, 171, 191))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("C:/Users/yashr/Pictures/logo.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 471, 71))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 80, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 210, 641, 61))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(20, 280, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setText("")
        self.lineEdit.setReadOnly(False)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(680, 280, 93, 28))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 330, 641, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(20, 380, 631, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setText("")
        self.lineEdit_2.setReadOnly(False)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(680, 380, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 430, 751, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(340, 480, 93, 28))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 110, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 551, 31))
        font = QtGui.QFont()
        font.setFamily("Bahnschrift SemiLight")
        font.setPointSize(12)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(20, 520, 751, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(20, 550, 751, 31))
        font = QtGui.QFont()
        font.setFamily("NSimSun")
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 801, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Welcome to the calibration page"))
        self.label_3.setText(_translate("MainWindow", "Here you automate opening applications, pressing keyboard "))
        self.label_4.setText(_translate("MainWindow", "If you want to open any file or application, enter it\'s  path here"))
        self.lineEdit.setPlaceholderText(_translate("MainWindow", "C:\\Programs\\....."))
        self.pushButton.setText(_translate("MainWindow", "Enter"))
        self.pushButton.clicked.connect(self.path_input)
        self.label_5.setText(_translate("MainWindow", "If you want to enter any text or press any shortcut keys."))
        self.lineEdit_2.setPlaceholderText(_translate("MainWindow", "Sample text or shortcucts (ctrl+c)"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter"))
        self.pushButton_2.clicked.connect(self.input)
        self.label_6.setText(_translate("MainWindow", "Take the cursor over the place where you want to click and press Ctrl+G"))
        self.pushButton_3.setText(_translate("MainWindow", "Ctrl+G"))
        self.pushButton_3.setShortcut(_translate("MainWindow", "Ctrl+G"))
        self.pushButton_3.clicked.connect(self.position_map)
        self.label_7.setText(_translate("MainWindow", "shortcuts, enter text, or make your cursor click anywhere"))
        self.label_8.setText(_translate("MainWindow", "on the screen. Close this window when done.. "))
        self.label_9.setText(_translate("MainWindow", "If you want to use this application to automate more than one tasks, feel free to"))
        self.label_10.setText(_translate("MainWindow", "make a duplicate of it and calibrate it once more for your another task."))

    def path_input(self):
        f = open("coordinates and shortcuts.txt", 'w')
        x = f.tell()
        f.write(self.lineEdit.text())
        f.close()
        f = open("coordinates and shortcuts.txt", 'r')
        f.seek(x)
        check = os.path.isfile(f.readline())
        msg = QMessageBox()
        if check is True:
            msg.setWindowTitle("Success :)")
            msg.setText("Given path is found")
            x = msg.exec_()
        else:
            msg.setWindowTitle("Error :(")
            msg.setText("Given path is not found\nTry to enter again")
            x = msg.exec_()
        f.close()
        f = open('coordinates and shortcuts.txt', 'a')
        f.write('\n')
        f.close()

    def input(self):
        f = open("coordinates and shortcuts.txt", 'a')
        f.write(self.lineEdit_2.text())
        f.write('\n')
        f.close()

    def position_map(self):
        f = open("coordinates and shortcuts.txt", 'a')
        l = pg.position()
        f.write(str(l.x))
        f.write("\n")
        f.write(str(l.y))
        f.write('\n')
        f.close()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
