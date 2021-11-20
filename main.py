import sys

from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtWidgets import QWidget, QApplication
from addEditCoffeeForm import AddEdit_Form
from coffeeInfoTable import CoffeeTable_Form


class EditCoffeeTable(QWidget, AddEdit_Form):
    def __init__(self, parent, model):
        super().__init__()
        self.setupUi(self)
        self.model = model
        self.initUI()

    def initUI(self):
        self.add_btn.clicked.connect(self.addRow)
        self.save_btn.clicked.connect(self.save)

        self.model.setEditStrategy(QSqlTableModel.OnManualSubmit)
        self.model.select()
        self.view.setModel(self.model)

    def addRow(self):
        self.model.insertRow(self.model.rowCount())

    def save(self):
        self.model.submitAll()


class CoffeeTable(QWidget, CoffeeTable_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.model = QSqlTableModel(self, self.db)
        self.initUI()

    def initUI(self):
        self.edit_btn.clicked.connect(self.edit)

        self.db.setDatabaseName('coffee.db')
        self.db.open()

        self.model.setTable('Coffee_info')
        self.model.select()

        self.view.setModel(self.model)

    def edit(self):
        self.edit_from = EditCoffeeTable(self, self.model)
        self.edit_from.show()

    def closeEvent(self, event):
        self.db.close()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = CoffeeTable()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())

