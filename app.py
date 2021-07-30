import sqlite3

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QWidget, QGridLayout, QTableWidget, QHeaderView, QTableWidgetItem


class App(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('База данных пользователей')
        self.setGeometry(0, 40, 1200, 1000)

        self.sql1 = """SELECT * FROM Users ORDER BY IQ DESC"""

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

    def deal_emit_slot(self, dateStr):

        self.fromDataBase(dateStr)
