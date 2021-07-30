from PyQt5.QtGui import QLinearGradient, QColor, QBrush, QIcon, QPalette
from PyQt5.QtWidgets import QLabel, QListWidget, QVBoxLayout, QListWidgetItem, QWidget


class DontFly(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setGeometry(700, 300, 500, 500)
        self.setWindowTitle('Противопоказания')
        self.setWindowIcon(QIcon('images/Mars.png'))
        p = QPalette()
        gradient = QLinearGradient(0, 0, 0, 750)
        gradient.setColorAt(0.0, QColor(255, 255, 255))
        gradient.setColorAt(1.0, QColor(102, 0, 255))
        p.setBrush(QPalette.Window, QBrush(gradient))
        self.setPalette(p)

        self.label = QLabel('<h4>К полёту не допускаются:</h4>', self)

        self.listWidget = QListWidget(self)
        QListWidgetItem('Лица младше 18 лет и старше 45 лет', self.listWidget)
        QListWidgetItem('Лица с весом меньше 50 кг и больше 90 кг', self.listWidget)
        QListWidgetItem('Наличие тяжёлых хронических заболеваний', self.listWidget)
        QListWidgetItem('Наличие патологий, выявленных томографией', self.listWidget)

        window_layout = QVBoxLayout()
        window_layout.addWidget(self.label)
        window_layout.addWidget(self.listWidget)
        self.setLayout(window_layout)
