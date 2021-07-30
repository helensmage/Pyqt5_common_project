import os
import random
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QFrame, \
    QLineEdit, QDialog, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QRadioButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor, QPalette, QLinearGradient, QBrush, QIcon
from PyQt5.QtCore import Qt, QDateTime, QRect, QMetaObject, QCoreApplication, pyqtSignal, QDate
from app import App
from voya import Voyage

qss2 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             color: white;
             background: #183bd9;
         }'''

class Window(QWidget):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle("Анкета")
        self.setGeometry(300, 50, 700, 950)
        self.setWindowIcon(QIcon('images/anket.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 750)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(0, 191, 255))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.main_text = QLabel(self)
        self.main_text.setText("Анкета жителей Марса")
        self.main_text.setFont(QFont("Times", 13, QFont.Bold))
        self.main_text.move(225, 20)
        self.main_text.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("*Загрузите фото")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(230, 70)
        self.text2.adjustSize()

        self.text1 = QLabel(self)
        self.text1.setText("Персональные данные")
        self.text1.setFont(QFont("Times", 13, QFont.Bold))
        self.text1.move(50, 250)
        self.text1.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Фамилия:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 290)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Имя:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 330)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Отчество:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 370)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Пол:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 410)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Вес:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 450)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Дата рождения:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 490)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Гражданство:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 530)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Место жительства")
        self.text2.setFont(QFont("Times", 13, QFont.Bold))
        self.text2.move(50, 570)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Страна:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 610)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Город:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 650)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Адрес:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 690)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Профессия")
        self.text2.setFont(QFont("Times", 13, QFont.Bold))
        self.text2.move(50, 730)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Место работы:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 770)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Должность:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 810)
        self.text2.adjustSize()

        self.text2 = QLabel(self)
        self.text2.setText("Зарплата:")
        self.text2.setFont(QFont("Times", 12, QFont.Bold))
        self.text2.move(50, 850)
        self.text2.adjustSize()

        self.btn = QPushButton(self)
        self.btn.move(480, 880)
        self.btn.setText("Отправить")
        self.btn.setFont(QFont("Times", 12, QFont.Bold))
        self.btn.setFixedWidth(170)
        self.btn.setFixedHeight(40)
        self.btn.setStyleSheet(qss2)

        self.line = QLabel(self)
        self.line.move(320, 245)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 2px solid #333")
        self.line.setFixedWidth(330)

        self.line = QLabel(self)
        self.line.move(270, 565)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 2px solid #333")
        self.line.setFixedWidth(380)

        self.line = QLabel(self)
        self.line.move(190, 725)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 2px solid #333")
        self.line.setFixedWidth(460)

        self.pushButton = QPushButton('Выбрать', self)
        self.pushButton.setStyleSheet(qss2)
        self.pushButton.move(230, 100)
        self.pushButton_2 = QPushButton('Загрузить', self)
        self.pushButton_2.setStyleSheet(qss2)
        self.pushButton_2.move(400, 100)
        self.pushButton.clicked.connect(self.openImage)
        self.cherr = 0
        self.file_name = ''
        self.pushButton_2.clicked.connect(self.saveImage)
        self.image = QLabel(self)
        self.image.move(55, 30)
        self.image.resize(150, 187)

        self.initUI()

    def openImage(self):
        # выбрать фото
        self.imagePath = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')
        self.pixmap = QPixmap(self.imagePath[0])
        self.image.setPixmap(self.pixmap.scaled(150, 187))

    def saveImage(self):
        if not self.cherr:
            current_dir = os.getcwd()
            self.file_name = str(random.random()) + '.png'
            if self.file_name:
                path = os.path.join(current_dir + '/UsersImages', self.file_name)
                self.image.pixmap().save(path)
                self.cherr = 1
        else:
            QMessageBox.critical(self, "Неверный ввод", "Вы уже отправили фото.", QMessageBox.Ok)


    def initUI(self):

        self.lbl = QLabel(self)
        self.surname = QLineEdit(self)
        self.surname.move(230, 285)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.weight = QLineEdit(self)
        self.weight.move(230, 445)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.fathername = QLineEdit(self)
        self.fathername.move(230, 370)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.name = QLineEdit(self)
        self.name.move(230, 325)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.citizenship = QLineEdit(self)
        self.citizenship.move(230, 530)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.country = QLineEdit(self)
        self.country.move(230, 610)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.city = QLineEdit(self)
        self.city.move(230, 650)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.adress = QLineEdit(self)
        self.adress.move(230, 690)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)


        self.lbl = QLabel(self)
        self.workplace = QLineEdit(self)
        self.workplace.move(230, 765)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.profession = QLineEdit(self)
        self.profession.move(230, 810)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.lbl = QLabel(self)
        self.salary = QLineEdit(self)
        self.salary.move(230, 850)
        self.lbl.move(200, 285)
        self.lbl.setFixedWidth(400)

        self.gender = QComboBox(self)
        self.gender.addItems(["М", "Ж"])
        self.gender.move(230, 410)

        self.dateofbirth = QDateEdit(self)
        self.dateofbirth.setCalendarPopup(True)
        self.dateofbirth.setDate(QDate.currentDate())
        self.dateofbirth.move(230, 490)
        self.dateofbirth.setFixedWidth(137)

        self.setGeometry(300, 50, 700, 950)
        self.setWindowTitle('Анкета')

        self.btn.clicked.connect(self.send_a_signal)

    def send_a_signal(self):
        self.Signal_OneParameter.connect(App().deal_emit_slot)

        self.additionlist = []
        self.livinglist = []
        self.prolist = []

        self.checkerror(self.surname.text(), self.additionlist)
        self.checkerror(self.name.text(), self.additionlist)
        self.checkerror(self.fathername.text(), self.additionlist)
        self.checkerror(self.gender.currentText(), self.additionlist)
        self.checkerror(self.weight.text(), self.additionlist)
        self.val = str(self.dateofbirth.date())
        for r in (('PyQt5.QtCore.QDate(', ''), (')', ''), (', ', '.')):
            self.val = self.val.replace(*r)
        self.checkerror(self.val, self.additionlist)
        self.checkerror(self.citizenship.text(), self.additionlist)
        self.checkerror(self.country.text(), self.livinglist)
        self.checkerror(self.city.text(), self.livinglist)
        self.checkerror(self.adress.text(), self.livinglist)
        self.checkerror(self.workplace.text(), self.prolist)
        self.checkerror(self.profession.text(), self.prolist)
        self.checkerror(self.salary.text(), self.prolist)

        if len(self.additionlist) == 7 and len(self.livinglist) == 3 and len(self.prolist) == 3:
            if self.file_name:
                self.insertsql = """INSERT INTO Users (Фото, Фамилия, Имя, Отчество, Пол, Вес_кг, Дата_рождения, Гражданство)
                                                                VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", \
                                 (self.file_name, self.additionlist[0], self.additionlist[1], self.additionlist[2],
                                  self.additionlist[3], \
                                  self.additionlist[4], self.additionlist[5], self.additionlist[6])
                App().deal_emit_slot(self.insertsql)
                self.insertsql = """INSERT INTO Living_place (Страна, Город, Адрес) VALUES (?, ?, ?)""", \
                                 (self.livinglist[0], self.livinglist[1], self.livinglist[2])
                App().deal_emit_slot(self.insertsql)
                self.insertsql = """UPDATE Users SET Место_жительства = (SELECT max(id) FROM Living_place) 
                                                where id = (SELECT max(id) FROM Users)"""
                App().deal_emit_slot(self.insertsql)
                self.insertsql = """INSERT INTO profession (Место_работы, Должность, Зарплата) VALUES (?, ?, ?)""", \
                                 (self.prolist[0], self.prolist[1], self.prolist[2])
                App().deal_emit_slot(self.insertsql)
                self.insertsql = """UPDATE Users SET Профессия = (SELECT max(id) FROM profession) 
                                                        where id = (SELECT max(id) FROM Users)"""

                App().deal_emit_slot(self.insertsql)
                self.close()
                self.anotherrr_form = Voyage()
                self.anotherrr_form.show()
            else:
                QMessageBox.critical(self, "Неверный ввод", "Вы не загрузили картинку.", QMessageBox.Ok)

    def checkerror(self, param, listic):
        if param:
            listic.append(param)
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)
