import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QTableView, QApplication
from PyQt5 import uic


class CoffeeTable(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('main.ui', self)
        self.initUI()

    def initUI(self):
        db = QSqlDatabase.addDatabase('QSQLITE')
        db.setDatabaseName('coffee.db')
        db.open()

        model = QSqlTableModel(self, db)
        model.setTable('Coffee_info')
        model.select()

        self.view.setModel(model)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = CoffeeTable()
    ex.show()
    sys.exit(app.exec())
