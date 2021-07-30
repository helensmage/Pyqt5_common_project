import os
import sqlite3
import sys
from PyQt5.QtWidgets import QLabel, QWidget, QApplication, QPushButton, QHBoxLayout, QListWidget, QListWidgetItem, \
    QVBoxLayout, QGridLayout, QScrollArea, QCheckBox, QSpinBox, QPlainTextEdit, QDateTimeEdit, QDateEdit, QFrame, \
    QLineEdit, QDialog, QMessageBox, QComboBox, QTableWidget, QTableWidgetItem, QHeaderView, QTabWidget
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
        self.setWindowTitle('База данных пользователей')
        self.setGeometry(100, 300, 1000, 1000)

        self.layout = QVBoxLayout(self)
        # Initialize tab screen
        self.tabs = QTabWidget()
        self.tab1 = QWidget()
        self.tab2 = QWidget()
        self.tab3 = QWidget()
        self.tab4 = QWidget()
        self.tab5 = QWidget()
        self.tabs.resize(300, 200)

        # Add tabs
        self.tabs.addTab(self.tab1, "Пользователи")
        self.tabs.addTab(self.tab2, "Место жительства")
        self.tabs.addTab(self.tab3, "Профессия")
        self.tabs.addTab(self.tab4, "Дом на Марсе")
        self.tabs.addTab(self.tab5, "Инопланетный досуг")

        # Create first tab
        self.sql1 = """SELECT * FROM Users"""
        self.fromDataBase(self.sql1)
        self.createTable()
        self.tab1.layout = QGridLayout()
        self.tab1.layout.setSpacing(10)
        self.tab1.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.tab1.setLayout(self.tab1.layout)

        # Create second tab
        self.sql2 = """SELECT * FROM Living_place"""
        self.fromDataBase(self.sql2)
        self.createTable()
        self.tab2.layout = QGridLayout()
        self.tab2.layout.setSpacing(10)
        self.tab2.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.tab2.setLayout(self.tab2.layout)

        # Create third tab
        self.sql3 = """SELECT * FROM profession"""
        self.fromDataBase(self.sql3)
        self.createTable()
        self.tab3.layout = QGridLayout()
        self.tab3.layout.setSpacing(10)
        self.tab3.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.tab3.setLayout(self.tab3.layout)

        # Create forth tab
        self.sql4 = """SELECT * FROM House"""
        self.fromDataBase(self.sql4)
        self.createTable()
        self.tab4.layout = QGridLayout()
        self.tab4.layout.setSpacing(10)
        self.tab4.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.tab4.setLayout(self.tab4.layout)

        # Create fifth tab
        self.sql5 = """SELECT * FROM entertainments"""
        self.fromDataBase(self.sql5)
        self.createTable()
        self.changeVal()
        self.addRecord()
        self.tab5.layout = QGridLayout()
        self.tab5.layout.setSpacing(10)
        self.tab5.layout.addWidget(self.buttonSave, 1, 8)
        self.tab5.layout.addWidget(self.buttonAdd, 1, 9)
        self.tab5.layout.addWidget(self.tableWidget, 2, 0, 2, 11)
        self.tab5.setLayout(self.tab5.layout)

        # Add tabs to widget
        self.layout.addWidget(self.tabs)
        self.setLayout(self.layout)

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
            self.allgenres = self.cur.execute("""SELECT Стоимость FROM voyage""").fetchall()
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

    def changeVal(self):
        self.changevalslist = []
        self.tableWidget.itemChanged.connect(self.update_check)
        self.buttonSave = QPushButton('Сохранить', self)
        self.buttonSave.clicked.connect(self.get_update_check)

    def update_check(self):
        self.row = self.tableWidget.currentRow()
        self.col = self.tableWidget.currentColumn()
        self.value = self.tableWidget.item(self.row, self.col)
        try:
            self.value = self.value.text()
            if self.value:
                self.idd = self.tableWidget.item(self.row, 0).text()
                self.changevalslist.append([self.col, self.value, self.idd])
            else:
                QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)
        except:
            pass

    def get_update_check(self):
        for i in self.changevalslist:
            if i[0] == 1:
                self.changeSql = """UPDATE entertainments
                                                SET Садовый_центр = ?
                                                WHERE id = ? """, (i[1], i[2])
            elif i[0] == 2:
                self.changeSql = """UPDATE entertainments
                                                SET Футуристический_бассейн = ?
                                                WHERE id = ? """, (i[1], i[2])
            elif i[0] == 3:
                self.changeSql = """UPDATE entertainments
                                                SET Дом_искусств = ?
                                                WHERE id = ? """, (i[1], i[2])
            elif i[0] == 4:
                self.changeSql = """UPDATE entertainments
                                                SET Центр_виртуальных_игр = ?
                                                WHERE id = ? """, (i[1], i[2])
            elif i[0] == 5:
                self.changeSql = """UPDATE entertainments
                                                SET Парк = ?
                                                WHERE id = ? """, (i[1], i[2])
            elif i[0] == 6:
                self.changeSql = """UPDATE entertainments
                                                SET Аквапарк = ?
                                                WHERE id = ? """, (i[1], i[2])

            self.fromDataBase(self.changeSql)

    def addRecord(self):
        self.buttonAdd = QPushButton('Добавить', self)
        self.buttonAdd.clicked.connect(self.openSecondForm)

    def openSecondForm(self):
        self.second_form = SecondForm()
        self.second_form.show()

    def deal_emit_slot(self, dateStr):
        self.insertsql = """INSERT INTO Films (title, year, genre, duration)
                                        VALUES (?, ?, ?, ?)""", (dateStr[0], dateStr[1], dateStr[2], dateStr[3])
        self.fromDataBase(self.insertsql)


class SecondForm(QWidget):
    Signal_OneParameter = pyqtSignal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Добавление')

        self.sadlabel = QLabel(self)
        self.sadlabel.setText('Садовый центр')
        self.title1 = QPlainTextEdit(self)

        self.yearlabel = QLabel(self)
        self.yearlabel.setText('Футуристический бассейн')
        self.title2 = QPlainTextEdit(self)

        self.genrelabel = QLabel(self)
        self.genrelabel.setText('Дом искусств')
        self.title3 = QPlainTextEdit(self)


        self.durationlabel = QLabel(self)
        self.durationlabel.setText('Центр виртуальных игр')
        self.title4 = QPlainTextEdit(self)

        self.durationlabel1 = QLabel(self)
        self.durationlabel1.setText('Парк')
        self.title5 = QPlainTextEdit(self)

        self.durationlabel2 = QLabel(self)
        self.durationlabel2.setText('Аквапарк')
        self.title6 = QPlainTextEdit(self)

        self.buttonadd = QPushButton('Добавить', self)
        self.buttonadd.clicked.connect(self.send_a_signal)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.sadlabel, 1, 0)
        grid.addWidget(self.title1, 1, 1)

        grid.addWidget(self.yearlabel, 2, 0)
        grid.addWidget(self.year1, 2, 1)

        grid.addWidget(self.genrelabel, 3, 0)
        grid.addWidget(self.genre1, 3, 1)

        grid.addWidget(self.durationlabel, 4, 0)
        grid.addWidget(self.duration1, 4, 1)

        grid.addWidget(self.durationlabel, 4, 0)
        grid.addWidget(self.duration1, 4, 1)

        grid.addWidget(self.durationlabel, 4, 0)
        grid.addWidget(self.duration1, 4, 1)

        grid.addWidget(self.buttonadd, 5, 1)

        self.setLayout(grid)

    def send_a_signal(self):
        self.Signal_OneParameter.connect(ex.deal_emit_slot)

        self.additionlist = []

        self.checkerror(self.title1)
        self.checkerror(self.title2)
        self.checkerror(self.title3)
        self.checkerror(self.title4)
        self.checkerror(self.title5)
        self.checkerror(self.title6)

        if len(self.additionlist) == 6:
            ex.deal_emit_slot(self.additionlist)
            self.close()

    def checkerror(self, param):
        if param.toPlainText():
            self.additionlist.append(param.toPlainText())
        else:
            QMessageBox.critical(self, "Неверный ввод", "Заполните, пожалуйста, поле!", QMessageBox.Ok)







if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Test()
    ex.show()
    sys.exit(app.exec())
