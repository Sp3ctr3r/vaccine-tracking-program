from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
import sqlite3 as sql

connect = sql.connect("database.db")
myCursor = connect.cursor()

myCursor.execute("create table if not exists my_table(TCNO text not null unique, ADI text not null, SOYADI text not null, TELEFON text not null, KAN text not null, AŞI text not null, ADRES text not null, MEDENİ text not null)")

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1107, 754)
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        MainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.socialSecurityNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.socialSecurityNumberLineEdit.setGeometry(QtCore.QRect(10, 80, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.socialSecurityNumberLineEdit.setFont(font)
        self.socialSecurityNumberLineEdit.setObjectName("socialSecurityNumberLineEdit")
        self.nameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.nameLineEdit.setGeometry(QtCore.QRect(10, 140, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.nameLineEdit.setFont(font)
        self.nameLineEdit.setObjectName("nameLineEdit")
        self.surnameLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.surnameLineEdit.setGeometry(QtCore.QRect(10, 200, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.surnameLineEdit.setFont(font)
        self.surnameLineEdit.setObjectName("surnameLineEdit")
        self.bloodGroupComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.bloodGroupComboBox.setGeometry(QtCore.QRect(10, 309, 69, 22))
        self.bloodGroupComboBox.setObjectName("bloodGroupComboBox")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.bloodGroupComboBox.addItem("")
        self.maritalStatusCheckBox = QtWidgets.QCheckBox(self.centralwidget)
        self.maritalStatusCheckBox.setGeometry(QtCore.QRect(10, 349, 61, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.maritalStatusCheckBox.setFont(font)
        self.maritalStatusCheckBox.setObjectName("maritalStatusCheckBox")
        self.authorLabel = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel.setGeometry(QtCore.QRect(450, 16, 470, 41))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.authorLabel.setFont(font)
        self.authorLabel.setObjectName("authorLabel")
        self.vaccineComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.vaccineComboBox.setGeometry(QtCore.QRect(100, 309, 81, 22))
        self.vaccineComboBox.setObjectName("vaccineComboBox")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.vaccineComboBox.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(250, 390, 841, 321))
        self.tableWidget.setRowCount(50)
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setObjectName("tableWidget")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setGeometry(QtCore.QRect(560, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.addButton.setFont(font)
        self.addButton.setObjectName("addButton")
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setGeometry(QtCore.QRect(720, 130, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.deleteButton.setFont(font)
        self.deleteButton.setObjectName("deleteButton")
        self.updateButton = QtWidgets.QPushButton(self.centralwidget)
        self.updateButton.setGeometry(QtCore.QRect(560, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.updateButton.setFont(font)
        self.updateButton.setObjectName("updateButton")
        self.viewButton = QtWidgets.QPushButton(self.centralwidget)
        self.viewButton.setGeometry(QtCore.QRect(720, 190, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.viewButton.setFont(font)
        self.viewButton.setObjectName("viewButton")
        self.searchbutton = QtWidgets.QPushButton(self.centralwidget)
        self.searchbutton.setGeometry(QtCore.QRect(560, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.searchbutton.setFont(font)
        self.searchbutton.setObjectName("searchbutton")
        self.addressTextEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.addressTextEdit.setGeometry(QtCore.QRect(10, 390, 231, 321))
        self.addressTextEdit.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.addressTextEdit.setFont(font)
        self.addressTextEdit.setInputMethodHints(QtCore.Qt.ImhNone)
        self.addressTextEdit.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.addressTextEdit.setObjectName("addressTextEdit")
        self.authorLabel2 = QtWidgets.QLabel(self.centralwidget)
        self.authorLabel2.setGeometry(QtCore.QRect(240, 10, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.authorLabel2.setFont(font)
        self.authorLabel2.setObjectName("authorLabel2")
        self.quitButton = QtWidgets.QPushButton(self.centralwidget)
        self.quitButton.setGeometry(QtCore.QRect(720, 250, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.quitButton.setFont(font)
        self.quitButton.setObjectName("quitButton")
        self.phoneNumberLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.phoneNumberLineEdit.setGeometry(QtCore.QRect(10, 260, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.phoneNumberLineEdit.setFont(font)
        self.phoneNumberLineEdit.setObjectName("phoneNumberLineEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1107, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        def add():
            try:
                addSSN = ui.socialSecurityNumberLineEdit.text()
                addName = ui.nameLineEdit.text()
                addSurname = ui.surnameLineEdit.text()
                addPhone = ui.phoneNumberLineEdit.text()
                addBlood = ui.bloodGroupComboBox.currentText()
                addVaccine = ui.vaccineComboBox.currentText()
                addAddress = ui.addressTextEdit.text()

                if ui.maritalStatusCheckBox.isChecked():
                    addMarital = "Evli"
                else:
                    addMarital = "Bekar"

                myCursor.execute("insert into my_table(TCNO, ADI, SOYADI, TELEFON, KAN, AŞI, ADRES, MEDENİ) values('{}','{}','{}','{}','{}','{}','{}','{}')".format(addSSN, addName, addSurname, addPhone, addBlood, addVaccine, addAddress, addMarital))
                connect.commit()
                
                ui.socialSecurityNumberLineEdit.clear()
                ui.nameLineEdit.clear()
                ui.surnameLineEdit.clear()
                ui.phoneNumberLineEdit.clear()
                ui.addressTextEdit.clear()

                show()

                QMessageBox.information(MainWindow, "Bilgi", "Kayıt işlemi başarılı!")

            except sql.IntegrityError:
                QMessageBox.warning(MainWindow, "Uyarı", "Gerekli alanları boş bırakmayın")


        def delete():
            try:
                addSSN = ui.socialSecurityNumberLineEdit.text()

                myCursor.execute("delete from my_table where TCNO = '{}'".format(addSSN))
                connect.commit()

                ui.socialSecurityNumberLineEdit.clear()
                ui.nameLineEdit.clear()
                ui.surnameLineEdit.clear()
                ui.phoneNumberLineEdit.clear()
                ui.addressTextEdit.clear()

                show()

                QMessageBox.information(MainWindow, "Bilgi", "Silme işlemi başarılı!")

            except sql.IntegrityError:
                QMessageBox.warning(MainWindow, "Uyarı", "Tc Kimlik numarasını girin!")
        
        def show():
            try:
                ui.tableWidget.clear()
                ui.tableWidget.setHorizontalHeaderLabels(('TC Kimlik No', 'Adı', 'Soyadı', 'Telefon', 'Kan Grubu', 'Aşı Durumu', 'Adres','Medeni Hal'))
                ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch) #  *!*

                myCursor.execute("select * from my_table")
                connect.commit()

                ui.socialSecurityNumberLineEdit.clear()
                ui.nameLineEdit.clear()
                ui.surnameLineEdit.clear()
                ui.phoneNumberLineEdit.clear()
                ui.addressTextEdit.clear()
                
                for lineIndex, lineData in enumerate(myCursor):
                    for columnIndex, columnData in enumerate(lineData):
                        ui.tableWidget.setItem(lineIndex, columnIndex, QTableWidgetItem(str(columnData)))

            except sql.IntegrityError:
                QMessageBox.warning(MainWindow, "Uyarı", "Lütfen geçerli değerler girin!")
        
        def update():
            try:
                addSSN = ui.socialSecurityNumberLineEdit.text()
                addPhone = ui.phoneNumberLineEdit.text()
                addAddress = ui.addressTextEdit.text()
                addVaccine = ui.vaccineComboBox.currentText()

                if ui.maritalStatusCheckBox.isChecked():
                    addMarital = "Evli"
                else:
                    addMarital = "Bekar"

                myCursor.execute("update my_table set TELEFON = '{}', ADRES = '{}', AŞI = '{}', MEDENİ = '{}' where TCNO = '{}'".format(addPhone, addAddress, addVaccine, addMarital, addSSN))
                connect.commit()

                ui.socialSecurityNumberLineEdit.clear()
                ui.nameLineEdit.clear()
                ui.surnameLineEdit.clear()
                ui.phoneNumberLineEdit.clear()
                ui.addressTextEdit.clear()

                show()
                
                QMessageBox.information(MainWindow, "Bilgi", "Güncelleme işlemi başarılı!")

            except sql.IntegrityError:
                QMessageBox.warning(MainWindow, "Uyarı", "Tc Kimlik numarasını girin!")
        
        def search():
            try:
                ui.tableWidget.clear()

                addSSN = ui.socialSecurityNumberLineEdit.text()

                myCursor.execute("select * from my_table where TCNO = '{}'".format(addSSN))
                connect.commit()

                ui.socialSecurityNumberLineEdit.clear()
                ui.nameLineEdit.clear()
                ui.surnameLineEdit.clear()
                ui.phoneNumberLineEdit.clear()
                ui.addressTextEdit.clear()

                for lineIndex, lineData in enumerate(myCursor):
                    for columnIndex, columnData in enumerate(lineData):
                        ui.tableWidget.setItem(lineIndex, columnIndex, QTableWidgetItem(str(columnData)))
                        
            except sql.IntegrityError:
                QMessageBox.warning(MainWindow, "Uyarı", "Lütfen geçerli değerler girin!")

        def quit():
            sys.exit()

        ui.addButton.clicked.connect(add)
        ui.deleteButton.clicked.connect(delete)
        ui.viewButton.clicked.connect(show)
        ui.updateButton.clicked.connect(update)
        ui.searchbutton.clicked.connect(search)
        ui.quitButton.clicked.connect(quit)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Aşı Takip Programı"))
        self.socialSecurityNumberLineEdit.setPlaceholderText(_translate("MainWindow", "TC Kimlik No"))
        self.nameLineEdit.setPlaceholderText(_translate("MainWindow", "Adı"))
        self.surnameLineEdit.setPlaceholderText(_translate("MainWindow", "Soyadı"))
        self.bloodGroupComboBox.setItemText(0, _translate("MainWindow", "0 RH +"))
        self.bloodGroupComboBox.setItemText(1, _translate("MainWindow", "0 RH -"))
        self.bloodGroupComboBox.setItemText(2, _translate("MainWindow", "A RH +"))
        self.bloodGroupComboBox.setItemText(3, _translate("MainWindow", "A RH -"))
        self.bloodGroupComboBox.setItemText(4, _translate("MainWindow", "B RH +"))
        self.bloodGroupComboBox.setItemText(5, _translate("MainWindow", "B RH -"))
        self.bloodGroupComboBox.setItemText(6, _translate("MainWindow", "AB RH +"))
        self.bloodGroupComboBox.setItemText(7, _translate("MainWindow", "AB RH -"))
        self.maritalStatusCheckBox.setText(_translate("MainWindow", "Evli"))
        self.vaccineComboBox.setItemText(0, _translate("MainWindow", "Aşı Olmadı"))
        self.vaccineComboBox.setItemText(1, _translate("MainWindow", "Biontech"))
        self.vaccineComboBox.setItemText(2, _translate("MainWindow", "Pfizer"))
        self.vaccineComboBox.setItemText(3, _translate("MainWindow", "Sinovac"))
        self.vaccineComboBox.setItemText(4, _translate("MainWindow", "Coronavac"))
        self.vaccineComboBox.setItemText(5, _translate("MainWindow", "Astrazeneca"))
        self.vaccineComboBox.setItemText(6, _translate("MainWindow", "Moderna"))
        self.vaccineComboBox.setItemText(7, _translate("MainWindow", "Sputnik V"))
        self.vaccineComboBox.setItemText(8, _translate("MainWindow", "Sinophram"))
        self.vaccineComboBox.setItemText(9, _translate("MainWindow", "J&J"))
        self.addButton.setText(_translate("MainWindow", "Ekle"))
        self.deleteButton.setText(_translate("MainWindow", "Sil"))
        self.updateButton.setText(_translate("MainWindow", "Güncelle"))
        self.viewButton.setText(_translate("MainWindow", "Görüntüle"))
        self.searchbutton.setText(_translate("MainWindow", "Ara"))
        self.addressTextEdit.setPlaceholderText(_translate("MainWindow", "Adres"))
        self.quitButton.setText(_translate("MainWindow", "Çık"))
        self.phoneNumberLineEdit.setPlaceholderText(_translate("MainWindow", "Telefon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
