from PyQt5.QtCore import QRect, QMetaObject
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QWidget, QFrame, QLabel, QLineEdit, QPushButton, QMessageBox
from app import App

class Ui_Dialog(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi()

    def setupUi(self):
        self.setWindowTitle("АДМИН")
        self.setWindowIcon(QIcon('images/profile.png'))
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
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setGeometry(QRect(260, 190, 231, 31))
        self.lineEdit.setStyleSheet("background-color: rgb(209, 207, 255);")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QLineEdit(self.frame)
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
            self.close()
            self.adminform = App()
            self.adminform.show()
        else:
            msg = QMessageBox(self)
            msg.setWindowTitle("Предупреждение!")
            msg.setText("У Вас нет доступа к панели администратора")
            msg.setIcon(QMessageBox.Warning)
            x = msg.exec_()
