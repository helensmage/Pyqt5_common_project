import os
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QFrame, \
    QLineEdit, QDialog, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QFont, QPixmap, QImage, QColor
from PyQt5.QtCore import Qt, QDateTime, QRect, QMetaObject, QCoreApplication, pyqtSignal
import requests

qss = '''QPushButton{
             border: none;
             font-size: 18px;
             font-style: italic;
         }
         QPushButton:hover{
            color: rgba(0, 82, 136, 1);
         }'''

qss1 = '''QPushButton{
             font-size: 18px;
             font-style: italic;
             letter-spacing: 0.1em;
             background: rgba(115, 194, 246, 1);
         }'''


class Test(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 30, 700, 1000)
        self.setWindowTitle('ПОЛЁТ НА МАРС')

        self.addText('<p style="color:rgba(0, 82, 136, 1);'
                             'font-size:18px;font-style:italic;">'
                             '<span style="font-size:36px;">3000</span>'
                             ' год<br>космических<br>путешествий</p>', 22, 36)
        self.addButton('Марсгородок', qss, 164, 69, 0, 0, 0, self.MarsCity)
        self.addButton('Противопоказания', qss, 303, 69, 0, 0, 0, self.Dontrecommend)
        self.addButton('О Марсе', qss, 477, 69, 1, 85, 20, self.AboutMars)

        self.addImage('Elon.png', 116, 100, 574, 10)
        self.addImage('spaceX.png', 116, 63, 574, 94)

        self.addButton('Администратор', qss1, 250, 125, 1, 187, 46, self.Admin)

        self.addText('<h1>Приветствуем Вас, Дорогие Земляне!</h1>', 100, 235)

        self.addImage('Earth.png', 150, 150, 120, 302)
        self.addImage('people.png', 175, 80, 260, 280)
        self.addImage('arrow.png', 150, 100, 275, 325)
        self.addImage('arrow1.png', 150, 100, 275, 354)
        self.addImage('Mars.png', 140, 140, 434, 307)

        self.addText('<h1>Мы поможем Вам:</h1>', 100, 525)
        self.addText('<h1>Спланировать инопланетный досуг!</h1>', 138, 574)
        self.addText('<h1>Безопасно добраться до Марса!</h1>', 200, 616)
        self.addText('<h1>Выбрать подходящий дом!</h1>', 266, 658)
        self.addText('<h1>Если вы решили сделать шаг навстречу'
                     '<br>Красной Планете, пожалуйста,'
                     '<br>заполните анкету!</h1>', 100, 770)

        self.addButton('Анкета', qss1, 280, 900, 1, 142, 46, self.Anketa)

    def addImage(self, name, a, b, x, y):
        fullname = os.path.join('images', name)
        self.pixmap = QPixmap(fullname).scaled(a, b, Qt.KeepAspectRatio)
        self.image = QLabel(self)
        self.image.move(x, y)
        self.image.setPixmap(self.pixmap)

    def addText(self, txt, x, y):
        self.label1 = QLabel(txt, self)
        self.label1.move(x, y)

    def addButton(self, txt, style, x, y, flag, a, b, func):
        self.button1 = QPushButton(txt, self)
        self.button1.setStyleSheet(style)
        self.button1.clicked.connect(func)
        self.button1.move(x, y)
        if flag:
            self.button1.resize(a, b)

    def MarsCity(self):
        pass

    def Dontrecommend(self):
        pass

    def AboutMars(self):
        pass

    def Anketa(self):
        pass

    def Admin(self):
        self.autorization = Ui_Dialog()
        self.autorization.show()


class Ui_Dialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("Dialog")
        self.setGeometry(500, 30, 812, 632)
        self.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.frame = QFrame(self)
        self.frame.setGeometry(QRect(90, 80, 631, 461))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QLabel("Добро пожаловать!", self.frame)
        self.label.setGeometry(QRect(200, 80, 250, 51))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(0, 0, 0);")
        self.label.setObjectName("label")
        self.label_2 = QLabel("Логин", self.frame)
        self.label_2.setGeometry(QRect(90, 190, 121, 31))
        font = QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QLabel("Пароль", self.frame)
        self.label_3.setGeometry(QRect(90, 260, 121, 21))
        font = QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.lineEdit = QLineEdit(self.frame)#
        self.lineEdit.setGeometry(QRect(260, 190, 231, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(209, 207, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.frame)#
        self.lineEdit_2.setGeometry(QRect(260, 260, 231, 31))
        self.lineEdit_2.setStyleSheet("background-color:#d1cfff;")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QPushButton("Вход", self.frame)
        self.pushButton.setGeometry(QRect(230, 360, 161, 41))
        font = QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(0, 170, 255);")
        self.pushButton.setObjectName("pushButton")

        QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(self.on_click)

    def on_click(self):
        login = 'DreamTeam'
        password = 'admin'
        textboxValue = self.lineEdit.text()
        textboxValue1 = self.lineEdit_2.text()
        if not textboxValue or not textboxValue1:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)
        elif textboxValue == login and textboxValue1 == password:
            self.close
            self.adminform = App()
            self.adminform.show()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Предупреждение!")
            msg.setText("У Вас нет доступа к панели администратора")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()

class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Коллекция фильмов')
        self.setGeometry(100, 300, 500, 500)

        self.sql1 = """SELECT * FROM Users"""

        self.fromDataBase(self.sql1)
        self.createTable()

        self.layout = QGridLayout()
        self.layout.setSpacing(10)
        self.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.setLayout(self.layout)

        self.show()

    def fromDataBase(self, FavGenre):
        try:
            self.con = sqlite3.connect("space.db")
            self.cur = self.con.cursor()
            try:
                self.result = self.cur.execute(FavGenre).fetchmany(50)
            except:
                self.result = self.cur.execute(*FavGenre).fetchmany(50)
            self.con.commit()
            try:
                self.names = [description[0] for description in self.cur.description]
            except:
                pass
            #self.allgenres = self.cur.execute("""SELECT title FROM genres""").fetchall()
            self.con.close()
        except sqlite3.Error as error:
            print("Ошибка при работе с SQLite", error)

    def createTable(self):
        self.tableWidget = QTableWidget()

        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        self.tableWidget.setHorizontalHeaderLabels(self.names)
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.fillMyTable()

    def fillMyTable(self):
        self.tableWidget.setRowCount(len(self.result))
        self.tableWidget.setColumnCount(len(self.result[0]))
        for i in range(len(self.result)):
            for j in range(len(self.result[0])):
                self.item = QTableWidgetItem(str(self.result[i][j]))
                self.item.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                if j == 0:
                    self.tableWidget.setItem(i, j, self.createItem(self.item,
                                                                   Qt.ItemIsSelectable | Qt.ItemIsEnabled))
                else:
                    self.tableWidget.setItem(i, j,
                                             self.createItem(self.item,
                                                             Qt.ItemIsSelectable | Qt.ItemIsEnabled | Qt.ItemIsEditable))
            self.colorRow(i)

    def createItem(self, text, flags):
        tableWidgetItem = QTableWidgetItem(text)
        tableWidgetItem.setFlags(flags)
        return tableWidgetItem

    def colorRow(self, row):
        for i in range(self.tableWidget.columnCount()):
            if row % 2 == 0:
                self.tableWidget.item(row, i).setBackground(QColor(209, 207, 255))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
