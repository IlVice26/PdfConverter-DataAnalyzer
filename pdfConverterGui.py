# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

class Ui_MainWindow(object):

    file = ''
    azienda = ''
    filesName = []
    files = []
    aziende = []

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 380)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 471, 31))
        self.label.setObjectName("label")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 110, 221, 201))
        self.listWidget.setObjectName("listWidget")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 90, 221, 16))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 121, 32))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 140, 241, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(510, 110, 221, 201))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 59, 16))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 110, 121, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 280, 241, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionGit = QtWidgets.QAction(MainWindow)
        self.actionGit.setObjectName("actionGit")
        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")
        self.actionCome_funziona = QtWidgets.QAction(MainWindow)
        self.actionCome_funziona.setObjectName("actionCome_funziona")
        self.actionAutore_progetto = QtWidgets.QAction(MainWindow)
        self.actionAutore_progetto.setObjectName("actionAutore_progetto")
        self.menuFile.addAction(self.actionGit)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEsci)
        self.menuHelp.addAction(self.actionCome_funziona)
        self.menuHelp.addSeparator()
        self.menuHelp.addAction(self.actionAutore_progetto)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.pushButton_2.setEnabled(False)

        self.pushButton.clicked.connect(self.get_file)
        self.pushButton_2.clicked.connect(self.save)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def get_file(self):
        name = QFileDialog.getOpenFileName(None, 'Open File', '', '*.pdf')
        self.files.append(name[0])
        tempName = str(name[0]).split('/')
        self.file = tempName[-1]
        self.filesName.append(self.file)
        self.pushButton.setEnabled(False)
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.update()

    def save(self):

        if self.file is '':
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Error")
            msg.setInformativeText("Test")
            msg.setWindowTitle("Error")
            msg.exec_()
            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)
        else:
            self.azienda = self.comboBox.currentText()
            self.aziende.append(self.azienda)

            self.listWidget.clear()
            self.listWidget_2.clear()
            self.azienda = ''
            self.file = ''

            self.listWidget.addItems(self.filesName)
            self.listWidget_2.addItems(self.aziende)

            self.pushButton.setEnabled(True)
            self.pushButton_2.setEnabled(False)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pdf Converter & Data Analyzer v. 0.0.1"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Pdf Converter &amp; Data Analyzer </span><span style=\" font-size:24pt; font-weight:600; font-style:italic; vertical-align:sub;\">by Vicentini Elia</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "File pronti per la conversione"))
        self.pushButton.setText(_translate("MainWindow", "Seleziona file"))
        self.pushButton_2.setText(_translate("MainWindow", "Salva scelta"))
        self.label_3.setText(_translate("MainWindow", "Azienda"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Eni"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Esso"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Union"))
        self.pushButton_3.setText(_translate("MainWindow", "Avvia conversione"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionGit.setText(_translate("MainWindow", "Git"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))
        self.actionCome_funziona.setText(_translate("MainWindow", "Come funziona?"))
        self.actionAutore_progetto.setText(_translate("MainWindow", "Autore progetto"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    MainWindow.update()
    sys.exit(app.exec_())
