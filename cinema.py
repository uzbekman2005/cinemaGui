# Form implementation generated from reading ui file 'cinema.ui'
#
# Created by: PyQt6 UI code generator 6.3.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(927, 762)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tablewidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tablewidget.setGeometry(QtCore.QRect(20, 121, 881, 501))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tablewidget.setFont(font)
        self.tablewidget.setLineWidth(2)
        self.tablewidget.setObjectName("tablewidget")
        self.tablewidget.setColumnCount(5)
        self.tablewidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tablewidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tablewidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tablewidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tablewidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(15)
        item.setFont(font)
        self.tablewidget.setHorizontalHeaderItem(4, item)
        self.tablewidget.horizontalHeader().setDefaultSectionSize(177)
        self.tablewidget.horizontalHeader().setMinimumSectionSize(65)
        self.tablewidget.verticalHeader().setDefaultSectionSize(30)
        self.tablewidget.verticalHeader().setMinimumSectionSize(21)
        self.lname = QtWidgets.QLineEdit(self.centralwidget)
        self.lname.setGeometry(QtCore.QRect(20, 30, 240, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lname.setFont(font)
        self.lname.setObjectName("lname")
        self.lgenre = QtWidgets.QLineEdit(self.centralwidget)
        self.lgenre.setGeometry(QtCore.QRect(270, 30, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lgenre.setFont(font)
        self.lgenre.setObjectName("lgenre")
        self.lyear = QtWidgets.QLineEdit(self.centralwidget)
        self.lyear.setGeometry(QtCore.QRect(440, 30, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lyear.setFont(font)
        self.lyear.setObjectName("lyear")
        self.lcinema = QtWidgets.QLineEdit(self.centralwidget)
        self.lcinema.setGeometry(QtCore.QRect(530, 30, 160, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lcinema.setFont(font)
        self.lcinema.setObjectName("lcinema")
        self.ltime = QtWidgets.QLineEdit(self.centralwidget)
        self.ltime.setGeometry(QtCore.QRect(700, 30, 80, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.ltime.setFont(font)
        self.ltime.setObjectName("ltime")
        self.btnadd = QtWidgets.QPushButton(self.centralwidget)
        self.btnadd.setGeometry(QtCore.QRect(800, 30, 90, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnadd.setFont(font)
        self.btnadd.setStyleSheet("background-color: rgb(87, 227, 137);")
        self.btnadd.setObjectName("btnadd")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 0, 240, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(270, 0, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(440, 0, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(530, 0, 160, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(700, 0, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.btnshowall = QtWidgets.QPushButton(self.centralwidget)
        self.btnshowall.setGeometry(QtCore.QRect(20, 80, 131, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.btnshowall.setFont(font)
        self.btnshowall.setStyleSheet("background-color: rgb(88, 255, 43);")
        self.btnshowall.setObjectName("btnshowall")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 630, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(27)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(153, 193, 241);")
        self.label.setObjectName("label")
        self.lsearch = QtWidgets.QLineEdit(self.centralwidget)
        self.lsearch.setGeometry(QtCore.QRect(60, 630, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lsearch.setFont(font)
        self.lsearch.setObjectName("lsearch")
        self.btndelete = QtWidgets.QPushButton(self.centralwidget)
        self.btndelete.setGeometry(QtCore.QRect(340, 630, 120, 40))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btndelete.setFont(font)
        self.btndelete.setStyleSheet("background-color: rgb(249, 0, 0);")
        self.btndelete.setObjectName("btndelete")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(10, 690, 451, 41))
        self.frame.setStyleSheet("background-color: rgb(214, 252, 226);")
        self.frame.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frame.setObjectName("frame")
        self.rbname = QtWidgets.QRadioButton(self.frame)
        self.rbname.setGeometry(QtCore.QRect(10, 4, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rbname.setFont(font)
        self.rbname.setChecked(True)
        self.rbname.setObjectName("rbname")
        self.rbgenre = QtWidgets.QRadioButton(self.frame)
        self.rbgenre.setGeometry(QtCore.QRect(100, 5, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rbgenre.setFont(font)
        self.rbgenre.setObjectName("rbgenre")
        self.rbyear = QtWidgets.QRadioButton(self.frame)
        self.rbyear.setGeometry(QtCore.QRect(190, 5, 81, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rbyear.setFont(font)
        self.rbyear.setObjectName("rbyear")
        self.rbcinema = QtWidgets.QRadioButton(self.frame)
        self.rbcinema.setGeometry(QtCore.QRect(270, 5, 101, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rbcinema.setFont(font)
        self.rbcinema.setObjectName("rbcinema")
        self.rbtime = QtWidgets.QRadioButton(self.frame)
        self.rbtime.setGeometry(QtCore.QRect(370, 5, 77, 34))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.rbtime.setFont(font)
        self.rbtime.setObjectName("rbtime")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tablewidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Name"))
        item = self.tablewidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Genre"))
        item = self.tablewidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Year"))
        item = self.tablewidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Cinema"))
        item = self.tablewidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Start time"))
        self.btnadd.setText(_translate("MainWindow", "Add"))
        self.label_2.setText(_translate("MainWindow", "Name"))
        self.label_3.setText(_translate("MainWindow", "Genre"))
        self.label_4.setText(_translate("MainWindow", "Year"))
        self.label_5.setText(_translate("MainWindow", "Cinema"))
        self.label_6.setText(_translate("MainWindow", "Time"))
        self.btnshowall.setText(_translate("MainWindow", "Show all"))
        self.label.setText(_translate("MainWindow", "????"))
        self.btndelete.setText(_translate("MainWindow", "???? Delete"))
        self.rbname.setText(_translate("MainWindow", "Name"))
        self.rbgenre.setText(_translate("MainWindow", "Genre"))
        self.rbyear.setText(_translate("MainWindow", "Year"))
        self.rbcinema.setText(_translate("MainWindow", "Cinema"))
        self.rbtime.setText(_translate("MainWindow", "Time"))
