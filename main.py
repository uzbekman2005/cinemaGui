from PyQt6.QtWidgets import QMainWindow,QApplication, QMessageBox
from cinema import *
from Database import *
import sys


class Window(QMainWindow):
    def __init__(self,parent=None):
        super(Window, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.loadDataToTable()
        self.ui.btnadd.clicked.connect(self.addClicked)
        self.ui.btnshowall.clicked.connect(self.showAllData)
        self.ui.lsearch.textChanged.connect(self.search)
        self.ui.btndelete.clicked.connect(self.deleteFilm)
    def deleteFilm(self):
        length = len(database)
        i = 0
        name = self.ui.lsearch.text().lower()
        while i < length:
            if database[i].get("Name").lower() == name:
                database.pop(i)
                length -=1
            else:
                i +=1
        else:
            print("Ma'lumot topilamdi")
        updateDatabase()
        self.search()
        self.ui.lsearch.setText("")

    def search(self):
        searched = self.ui.lsearch.text().lower()
        res = []
        if self.ui.rbname.isChecked():
            res = list(filter(lambda x:searched in x["Name"].lower(), database))
        elif self.ui.rbgenre.isChecked():
            res = list(filter(lambda x: searched in x["Genre"].lower(), database))
        elif self.ui.rbcinema.isChecked():
            res = list(filter(lambda x: searched in x["Cinema"].lower(), database))
        elif self.ui.rbtime.isChecked():
            if not searched.isdigit() and searched != "":
                self.addWarning()
            else:
                if searched == "":
                    searched = "0"
                res = list(filter(lambda x: int(x["Starts"].split(":")[0]) >= int(searched.split(":")[0]), database))
        elif self.ui.rbyear.isChecked():
            if not searched.isdigit() and searched != "":
                self.addWarning()
            else:
                if searched == "":
                    searched = "0"
                res = list(filter(lambda x: int(x["Year"].split(":")[0]) >= int(searched.split(":")[0]), database))

        self.showSearchedDate(res)


    def addWarning(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Information)
        msg.setText("Iltimos ma'lumotlarni to'g'ri kiriting Katta ehtimol bilan "
                    "Birorta katakni bo'sh qoldirgansiz, vaqtni xator kiritgansiz yoki yilni")
        msg.setWindowTitle("ERROR!!!")
        msg.setStandardButtons(QMessageBox.StandardButton.Ok | QMessageBox.StandardButton.Close)
        res = msg.exec()

    def clearAddText(self):
        self.ui.ltime.setText("")
        self.ui.lname.setText("")
        self.ui.lyear.setText("")
        self.ui.lcinema.setText("")
        self.ui.lgenre.setText("")

    def addClicked(self):
        if self.ui.lname.text() == "" or self.ui.lgenre.text() == "" or \
            not self.ui.lyear.text().isdigit():
            self.addWarning()
        elif len(self.ui.ltime.text().split(":")) != 2:
            self.addWarning()
        else:
            res = {
            "Name":self.ui.lname.text(),
            "Genre":self.ui.lgenre.text(),
            "Year":self.ui.lyear.text(),
            "Cinema":self.ui.lcinema.text(),
            "Starts":self.ui.ltime.text()
            }
            self.clearAddText()
            database.append(res)
            updateDatabase()
            self.showAllData()

    def showSearchedDate(self, res):
        row = 0
        self.ui.tablewidget.setRowCount(len(res))
        for data in res:
            self.ui.tablewidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data["Name"]))
            self.ui.tablewidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data["Genre"]))
            self.ui.tablewidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data["Year"]))
            self.ui.tablewidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data["Cinema"]))
            self.ui.tablewidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data["Starts"]))
            row+=1

    def showAllData(self):
        self.loadDataToTable()

    def loadDataToTable(self):
        row = 0
        self.ui.tablewidget.setRowCount(len(database))
        for data in database:
            self.ui.tablewidget.setItem(row, 0, QtWidgets.QTableWidgetItem(data["Name"]))
            self.ui.tablewidget.setItem(row, 1, QtWidgets.QTableWidgetItem(data["Genre"]))
            self.ui.tablewidget.setItem(row, 2, QtWidgets.QTableWidgetItem(data["Year"]))
            self.ui.tablewidget.setItem(row, 3, QtWidgets.QTableWidgetItem(data["Cinema"]))
            self.ui.tablewidget.setItem(row, 4, QtWidgets.QTableWidgetItem(data["Starts"]))
            row+=1



def main():
    app = QApplication([])
    window = Window()
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()