import os
import random
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QFrame, \
    QLineEdit, QDialog, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QFileDialog, QRadioButton
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor, QPalette, QLinearGradient, QBrush, QIcon
from PyQt5.QtCore import Qt, QDateTime, QRect, QMetaObject, QCoreApplication, pyqtSignal, QDate
import requests
from app import App
from iq import IQ


qss6 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             background: #59942f;
         }'''


class Ent(QWidget):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle('Выбор досуга')
        self.setGeometry(750, 100, 650, 900)
        self.setWindowIcon(QIcon('images/game.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 1200)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(0.5, QColor(255, 236, 139))
        gradient.setColorAt(1.0, QColor(122, 163, 39))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.main_text = QLabel(self)
        self.main_text.setText("Развлечения на Марсе")
        self.main_text.setFont(QFont("Times", 13, QFont.Bold))
        self.main_text.move(40, 20)
        self.main_text.adjustSize()

        self.entlist = []

        self.text1 = QCheckBox(self)
        self.text1.setText("Садовый центр")
        self.text1.setFont(QFont("Times", 11, QFont.Bold))
        self.text1.move(90, 280)
        self.text1.adjustSize()
        self.entlist.append(self.text1)

        self.text1 = QCheckBox(self)
        self.text1.setText("Футуристический бассейн")
        self.text1.setFont(QFont("Times", 11, QFont.Bold))
        self.text1.move(340, 280)
        self.text1.adjustSize()
        self.entlist.append(self.text1)

        self.text1 = QCheckBox(self)
        self.text1.setText("Дом искусств")
        self.text1.setFont(QFont("Times", 11, QFont.Bold))
        self.text1.move(100, 540)
        self.text1.adjustSize()
        self.entlist.append(self.text1)

        self.text1 = QCheckBox(self)
        self.text1.setText("Центр виртуальных игр")
        self.text1.setFont(QFont("Times", 11, QFont.Bold))
        self.text1.move(360, 540)
        self.text1.adjustSize()
        self.entlist.append(self.text1)

        self.text1 = QCheckBox(self)
        self.text1.setText("Парк")
        self.text1.setFont(QFont("Times", 11, QFont.Bold))
        self.text1.move(125, 800)
        self.text1.adjustSize()
        self.entlist.append(self.text1)

        self.text1 = QCheckBox(self)
        self.text1.setText("Аквапарк")
        self.text1.setFont(QFont("Times", 11, QFont.Bold))
        self.text1.move(430, 800)
        self.text1.adjustSize()
        self.entlist.append(self.text1)

        self.line = QLabel(self)
        self.line.move(310, 15)
        self.line.setStyleSheet("margin:20px 0;padding: 0;height: 0;border: none;border-top: 1px solid #333")
        self.line.setFixedWidth(300)

        self.se = QPushButton('Отправить', self)
        self.se.clicked.connect(self.send)
        self.se.move(270, 850)
        self.se.setStyleSheet(qss6)

        self.initUI()

    def send(self):
        self.Signal_OneParameter.connect(App().deal_emit_slot)
        self.sqql = """INSERT INTO entertainments(Садовый_центр, Футуристический_бассейн, Дом_искусств, Центр_виртуальных_игр,
        Парк, Аквапарк) VALUES(0,0,0,0,0,0)"""
        App().deal_emit_slot(self.sqql)
        for i in range(len(self.entlist)):
            if self.entlist[i].isChecked():
                if i == 0:
                    self.updatesql = """UPDATE entertainments SET Садовый_центр = 1
                                                            WHERE id = (SELECT max(id) FROM entertainments)"""
                elif i == 1:
                    self.updatesql = """UPDATE entertainments SET Футуристический_бассейн = 1
                                                            WHERE id = (SELECT max(id) FROM entertainments)"""
                elif i == 2:
                    self.updatesql = """UPDATE entertainments SET Дом_искусств = 1
                                                            WHERE id = (SELECT max(id) FROM entertainments)"""
                elif i == 3:
                    self.updatesql = """UPDATE entertainments SET Центр_виртуальных_игр = 1
                                                            WHERE id = (SELECT max(id) FROM entertainments)"""
                elif i == 4:
                    self.updatesql = """UPDATE entertainments SET Парк = 1
                                                            WHERE id = (SELECT max(id) FROM entertainments)"""
                elif i == 5:
                    self.updatesql = """UPDATE entertainments SET Аквапарк = 1
                                                            WHERE id = (SELECT max(id) FROM entertainments)"""
                App().deal_emit_slot(self.updatesql)
        self.updatesql = """UPDATE Users SET Досуг = (SELECT max(id) FROM entertainments)
                                        WHERE id = (SELECT max(id) FROM Users)"""
        App().deal_emit_slot(self.updatesql)
        self.close()
        self.goforiq = IQ()
        self.goforiq.show()


    def initUI(self):
        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/ent/садовый центр.jpg")
        lbl = QLabel(self)
        lbl.move(40, 80)
        lbl.setPixmap(pixmap)
        lbl.setFixedWidth(260)
        lbl.setFixedHeight(195)

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/ent/Футуристический бассейн.jpg")
        lbl = QLabel(self)
        lbl.move(350, 80)
        lbl.setPixmap(pixmap)
        lbl.setFixedWidth(260)
        lbl.setFixedHeight(195)

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/ent/дом искусств.jpg")
        lbl = QLabel(self)
        lbl.move(40, 340)
        lbl.setPixmap(pixmap)
        lbl.setFixedWidth(260)
        lbl.setFixedHeight(195)

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/ent/центр вертуальных игр.jpg")
        lbl = QLabel(self)
        lbl.move(350, 340)
        lbl.setPixmap(pixmap)
        lbl.setFixedWidth(260)
        lbl.setFixedHeight(195)

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/ent/парк.jpg")
        lbl = QLabel(self)
        lbl.move(40, 600)
        lbl.setPixmap(pixmap)
        lbl.setFixedWidth(260)
        lbl.setFixedHeight(195)

        hbox = QHBoxLayout(self)
        pixmap = QPixmap("images/ent/Аква парк.jpg")
        lbl = QLabel(self)
        lbl.move(350, 600)
        lbl.setPixmap(pixmap)
        lbl.setFixedWidth(260)
        lbl.setFixedHeight(195)

        self.setLayout(hbox)
        self.show()
