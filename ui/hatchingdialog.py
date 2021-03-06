# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Seafile\Code\Senior1\HCI2\spirit_gen_demo\ui\hatchingdialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HatchingDialog(object):
    def setupUi(self, HatchingDialog):
        HatchingDialog.setObjectName("HatchingDialog")
        HatchingDialog.setWindowModality(QtCore.Qt.NonModal)
        HatchingDialog.resize(235, 250)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        HatchingDialog.setWindowIcon(icon)
        HatchingDialog.setStyleSheet("#HatchingDialog{background-color: rgb(255, 255, 255);}")
        self.FatherEdit = QtWidgets.QLineEdit(HatchingDialog)
        self.FatherEdit.setGeometry(QtCore.QRect(80, 70, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(12)
        self.FatherEdit.setFont(font)
        self.FatherEdit.setObjectName("FatherEdit")
        self.MotherEdit = QtWidgets.QLineEdit(HatchingDialog)
        self.MotherEdit.setGeometry(QtCore.QRect(80, 150, 120, 20))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(12)
        self.MotherEdit.setFont(font)
        self.MotherEdit.setObjectName("MotherEdit")
        self.SELECTED = QtWidgets.QLabel(HatchingDialog)
        self.SELECTED.setGeometry(QtCore.QRect(20, 20, 136, 14))
        self.SELECTED.setPixmap(QtGui.QPixmap(":/HatchingHouse/SELECTED_.png"))
        self.SELECTED.setScaledContents(True)
        self.SELECTED.setObjectName("SELECTED")
        self.Love = QtWidgets.QLabel(HatchingDialog)
        self.Love.setGeometry(QtCore.QRect(110, 110, 20, 20))
        self.Love.setPixmap(QtGui.QPixmap(":/HatchingHouse/love.png"))
        self.Love.setScaledContents(False)
        self.Love.setObjectName("Love")
        self.pushButton = QtWidgets.QPushButton(HatchingDialog)
        self.pushButton.setGeometry(QtCore.QRect(69, 200, 102, 30))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/HatchingHouse/BREED.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QtCore.QSize(102, 30))
        self.pushButton.setObjectName("BreedButton")
        self.No1 = QtWidgets.QLabel(HatchingDialog)
        self.No1.setGeometry(QtCore.QRect(30, 70, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(12)
        self.No1.setFont(font)
        self.No1.setObjectName("No1")
        self.No2 = QtWidgets.QLabel(HatchingDialog)
        self.No2.setGeometry(QtCore.QRect(30, 150, 60, 20))
        font = QtGui.QFont()
        font.setFamily("Press Start 2P")
        font.setPointSize(12)
        self.No2.setFont(font)
        self.No2.setObjectName("No2")

        self.retranslateUi(HatchingDialog)
        QtCore.QMetaObject.connectSlotsByName(HatchingDialog)

    def retranslateUi(self, HatchingDialog):
        _translate = QtCore.QCoreApplication.translate
        HatchingDialog.setWindowTitle(_translate("HatchingDialog", "Breeding"))
        self.FatherEdit.setText(_translate("HatchingDialog", "00001"))
        self.MotherEdit.setText(_translate("HatchingDialog", "00002"))
        self.No1.setText(_translate("HatchingDialog", "No."))
        self.No2.setText(_translate("HatchingDialog", "No."))
import resources_rc
