import pickle
import sys
from functools import partial

from PIL import ImageQt
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget, QLabel, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QDialog, QLineEdit, QMessageBox

import genetic
import image_gen
from image_gen import gen_pic
from ui.SpiritThumb import Ui_SpiritThumb
from ui.borndialog import Ui_BornDialog
from ui.hatchingdialog import Ui_HatchingDialog
from ui.mainwindow import Ui_MainWindow
from ui.spirithouse import Ui_SpiritHouse
from ui.universedialog import Ui_UniverseDialog

USER_DATA_PATH = 'user_data.sav'


def load_user_data():
    try:
        f = open(USER_DATA_PATH, 'rb')
        return pickle.load(f)
    except OSError:
        return {
            'spirits': []
        }


def write_user_data(user_data):
    f = open(USER_DATA_PATH, 'wb')
    return pickle.dump(user_data, f)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.centralWidget()
    
    
    def enter_spirit_house():
        ui = Ui_SpiritHouse()
        ui.setupUi(mainWindow)
        refresh_spirit_house()
        mainWindow.findChild(QWidget, 'SpiritsHouseContent').setLayout(gb)
        mainWindow.findChild(QPushButton, 'SpiritUniverseButton').clicked.connect(meet_new_spirit)
        mainWindow.findChild(QPushButton, 'GoHatchingButton').clicked.connect(hat_dialog.show)
    
    
    mainWindow.findChild(QPushButton, name="StartButton").clicked.connect(enter_spirit_house)
    
    gb = QGridLayout()
    gb.setSpacing(10)
    for i in range(5):
        gb.setColumnMinimumWidth(i, 160)
        gb.setColumnStretch(i, 1)
    gb_tail = 0
    
    
    def refresh_spirit_house():
        global gb_tail
        user_data = load_user_data()
        spirits_num = len(user_data['spirits'])
        for id in range(gb_tail, spirits_num, 1):
            row = id // 5
            col = id - row * 5
            spirit = user_data['spirits'][id]
            img = gen_pic(spirit['gene'])
            img = ImageQt.toqpixmap(img)
            ui = Ui_SpiritThumb()
            thumb = QWidget()
            ui.setupUi(thumb)
            thumb.findChild(QLabel, 'SpiritImg').setPixmap(img)
            thumb.findChild(QLabel, 'SpiritId').setText("No.{:0>5d}".format(id + 1))
            gb.addWidget(thumb, row, col)
        for i in range(max(spirits_num // 5 + 1, 2)):
            gb.setRowMinimumHeight(i, 200)
            gb.setRowStretch(i, 1)
        gb_tail = spirits_num
        hat_dialog.findChild(QLineEdit, 'FatherEdit').setValidator(QIntValidator(0, gb_tail))
        hat_dialog.findChild(QLineEdit, 'MotherEdit').setValidator(QIntValidator(0, gb_tail))
    
    
    ud_ui = Ui_UniverseDialog()
    uni_dialog = QDialog()
    ud_ui.setupUi(uni_dialog)
    uni_dialog.findChild(QPushButton, 'UniverseNoButton').clicked.connect(uni_dialog.close)
    
    
    def meet_new_spirit():
        new_sp = {'gene': genetic.rand_gene_str()}
        img = gen_pic(new_sp['gene']).resize((240, 240))
        img = ImageQt.toqpixmap(img)
        uni_dialog.findChild(QLabel, 'SpiritImgLarge').setPixmap(img)
        try:
            uni_dialog.findChild(QPushButton, 'UniverseYesButton').clicked.disconnect()
        except TypeError:
            pass
        uni_dialog.findChild(QPushButton, 'UniverseYesButton').clicked.connect(
            lambda: (accept_new_spirit(new_sp), uni_dialog.close()))
        uni_dialog.exec_()
    
    
    def accept_new_spirit(spirit):
        user_data = load_user_data()
        user_data['spirits'].append(spirit)
        write_user_data(user_data)
        refresh_spirit_house()
    
    
    def check_breed():
        user_data = load_user_data()
        spirits_num = len(user_data['spirits'])
        try:
            fa_id = int(hat_dialog.findChild(QLineEdit, 'FatherEdit').text()) - 1
            mo_id = int(hat_dialog.findChild(QLineEdit, 'MotherEdit').text()) - 1
            assert 0 <= fa_id < spirits_num and 0 <= mo_id < spirits_num
            assert fa_id != mo_id
        except (AssertionError, TypeError):
            QMessageBox.warning(hat_dialog, 'Warning', '请输入2个不同的合法精灵ID')
        else:
            fa = user_data['spirits'][fa_id]['gene']
            mo = user_data['spirits'][mo_id]['gene']
            child = genetic.reproduce(fa, mo)
            img = gen_pic(child).resize((240, 240))
            img = ImageQt.toqpixmap(img)
            born_ui = Ui_BornDialog()
            born_dialog = QDialog()
            born_ui.setupUi(born_dialog)
            born_dialog.findChild(QLabel, 'SpiritImgLarge').setPixmap(img)
            born_dialog.findChild(QPushButton, 'YesButton').clicked.connect(born_dialog.deleteLater)
            born_dialog.exec_()
            accept_new_spirit({'gene': child})
            hat_dialog.close()
    
    
    hd_ui = Ui_HatchingDialog()
    hat_dialog = QDialog()
    hd_ui.setupUi(hat_dialog)
    hat_dialog.findChild(QPushButton, 'BreedButton').clicked.connect(check_breed)
    
    mainWindow.show()
    sys.exit(app.exec_())
