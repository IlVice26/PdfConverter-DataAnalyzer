# -*- coding: utf-8 -*-
"""
    Gui per pdfConverter.py
    Lavoro svolto da Vicentini Elia
"""

import os
LIBRARIES = ['pyqt5', 'openpyxl']
com_d = os.popen('python -m pip list --disable-pip-version-check')
listd = com_d.read()
for i in range(len(LIBRARIES)):
    if LIBRARIES[i] in listd:
        pass
    else:
        os.system('python -m pip install ' + LIBRARIES[i] + ' -q --disable-pip-version-check')

import util.setupGui as setupGui
import util.dataCollect as dataCollect
import util.exportData as exportData
import util.pdfConverter as pdfConverter

import sys
import time

from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog, QCheckBox, QLineEdit, QLabel
from PyQt5.QtGui import QPainter, QPen, QBrush, QPixmap, QColor
from PyQt5.QtCore import Qt


class Ui_MainWindow(object):
    
    files = []
    filesName = []
    aziende = []
    file = ''
    azienda = ''
    
    fileTemp = []
    isEncrypted = False

    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(740, 440)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        # Sfondo programma
        self.titoloImage = QLabel(self.centralwidget)
        self.titoloImage.setPixmap(QPixmap("img\\testTitoloprogramma.png"))
        self.titoloImage.setGeometry(0, 0, 740, 85)

        self.sfondoImmagine = QLabel(self.centralwidget)
        self.sfondoImmagine.setPixmap(QPixmap('img\\sfondoBianco1.png'))
        self.sfondoImmagine.setGeometry(0, 85, 740, 340)

        # Titolo programma
        self.titolo = QLabel(self.centralwidget)
        self.titolo.setGeometry(QtCore.QRect(18, 90, 1000, 50))
        self.titolo.setObjectName('titolo')
        self.titolo.setStyleSheet('color: rgb(56, 56, 56)')
        self.titolo.setFont(QtGui.QFont('Raleway', 30))

        # Prima lista
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(270, 165, 221, 201))
        self.listWidget.setObjectName("listWidget")
        self.listWidget.setStyleSheet('background-color:white')
        self.listWidget.setFont(QtGui.QFont('Roboto'))

        # Titolo prima lista
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(270, 145, 221, 16))
        self.label_2.setObjectName("label_2")
        self.label_2.setStyleSheet('color: rgb(56, 56, 56)')
        self.label_2.setFont(QtGui.QFont('Roboto'))
        
        # Bottone Scegli File
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 164, 119, 20))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.setStyleSheet('color: rgb(56, 56, 56)')
        self.pushButton.setFont(QtGui.QFont('Roboto'))
        
        # Bottone Salva File
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 243, 241, 20))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setFont(QtGui.QFont('Roboto'))

        # Seconda lista 
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(500, 165, 221, 201))
        self.listWidget_2.setObjectName("listWidget_2")
        self.listWidget_2.setStyleSheet('background-color: white')
        self.listWidget_2.setFont(QtGui.QFont('Roboto'))
        
        # Titolo seconda lista
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(500, 145, 59, 16))
        self.label_3.setObjectName("label_3")
        self.label_3.setStyleSheet('color: rgb(56, 56, 56)')
        self.label_3.setFont(QtGui.QFont('Roboto'))
        
        # Combobox (Eni, Esso, Union)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(141, 165, 119, 18))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setFont(QtGui.QFont('Roboto'))
        self.comboBox.setStyleSheet('color: rgb(56, 56, 56)')
        
        # Bottone Avvia Conversione
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 347, 241, 20))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setFont(QtGui.QFont('Roboto'))
        
        # Bottone Elimina oggetti
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(332, 372, 101, 20))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_3.setFont(QtGui.QFont('Roboto'))

        # Menu bar
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 740, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        self.statusbar.setStyleSheet('color: rgb(56, 56, 56)')
        MainWindow.setStatusBar(self.statusbar)
        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")
        self.actionDatabase = QtWidgets.QAction(MainWindow)
        self.actionDatabase.setObjectName('actionDatabase')
        self.menuFile.addAction(self.actionDatabase)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEsci)
        self.menubar.addAction(self.menuFile.menuAction())

        # Titolo checkBox7 
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(21, 190, 221, 16))
        self.label_4.setObjectName("label_4")
        self.label_4.setFont(QtGui.QFont('Roboto'))

        # CheckBox
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(107, 188, 20, 20))
        self.checkBox.setObjectName("checkBox")
        
        # Titolo dialogText
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(21, 215, 221, 16))
        self.label_5.setObjectName("label_5")
        self.label_5.setFont(QtGui.QFont('Roboto'))

        # DialogTextChiave
        self.dialogText = QtWidgets.QLineEdit(self.centralwidget)
        self.dialogText.setGeometry(QtCore.QRect(60, 215, 200, 16))
        self.dialogText.setObjectName("dialogText")
        self.dialogText.setFont(QtGui.QFont('Roboto'))

        # Setup iniziale dei bottoni
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.label_4.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.label_5.setEnabled(False)
        self.dialogText.setEnabled(False)

        # Azioni di ogni bottone
        self.actionDatabase.triggered.connect(self.changeDatabase)
        self.actionEsci.triggered.connect(self.closeWindow)
        self.pushButton.clicked.connect(self.get_file)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.avviaConversione)
        self.pushButton_4.clicked.connect(self.eliminaDaLista)
        self.checkBox.clicked.connect(self.checkBoxEncrypted)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.statusbar.showMessage('Pronto')



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pdf Converter & Data Analyzer"))
        self.label_2.setText(_translate("MainWindow", "File pronti per la conversione"))
        self.pushButton.setText(_translate("MainWindow", "Seleziona file"))
        self.pushButton_2.setText(_translate("MainWindow", "Salva scelta"))
        self.label_3.setText(_translate("MainWindow", "Azienda"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Eni"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Esso"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Union"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Autostrade"))
        self.comboBox.setItemText(4, _translate("MainWindow", "VWL"))
        self.comboBox.setItemText(5, _translate("MainWindow", "Arval"))
        self.pushButton_3.setText(_translate("MainWindow", "Avvia conversione"))
        self.pushButton_4.setText(_translate("MainWindow", "Elimina"))
        self.menuFile.setTitle(_translate("MainWindow", "Opzioni"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))
        self.actionDatabase.setText(_translate('MainWindow', 'Seleziona Database'))
        self.label_4.setText(_translate("Mainwindow", "Il file è criptato?"))
        self.label_5.setText(_translate("Mainwindow", "Chiave"))
        self.titolo.setText(_translate("Mainwindow", "Pdf Converter & Data Analyzer"))
        MainWindow.setFixedSize(MainWindow.size())
        MainWindow.setWindowIcon(QtGui.QIcon('img\\icon.png'))

    def changeDatabase(self):
        db = QFileDialog.getOpenFileName(None, 'Seleziona il database', '', '*.xlsx')
        path = db[0]
        if path == '':
            alert = QMessageBox()
            alert.setWindowIcon(QtGui.QIcon('img\\icon.png'))
            alert.setText('Attenzione')
            alert.setInformativeText('Nessun database selezionato!')
            alert.setIcon(QMessageBox.Critical)
            alert.setWindowTitle('Attenzione')
            alert.exec_()
        else:
            os.rename(path, 'database.xlsx')
            temp = path.split('\\')
            cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'database.xlsx' + ' ' + setupGui.PATHWIN32 + '\\database\\database.xlsx'
            os.system(cmdFinal)
            alert = QMessageBox()
            alert.setWindowIcon(QtGui.QIcon('img\\icon.png'))
            alert.setText('Informazione')
            alert.setInformativeText('Database salvato correttamente!')
            alert.setIcon(QMessageBox.Information)
            alert.setWindowTitle('Informazione')
            alert.exec_()

    def closeWindow(self):
        """
        Chiude la finestra
        """
        MainWindow.close()

    def checkBoxEncrypted(self):
        """
        Permette l'inserimento di una chiave per decriptare il file pdf
        """
        if self.checkBox.isChecked():
            self.label_5.setEnabled(True)
            self.dialogText.setEnabled(True)
            self.isEncrypted = True
        else:
            self.label_5.setEnabled(False)
            self.dialogText.setEnabled(False)
            self.isEncrypted = False


    def get_file(self):
        name = QFileDialog.getOpenFileName(None, 'Open File', '', 'Pdf (*.pdf);; Xml (*.xml)')
        tempN = name[0]

        # Controllo se il file è stato selezionato
        if not tempN is '':

            # In caso positivo aggiungo la path assoluta ad una lista temporanea
            self.fileTemp.append(name[0])
            
            # Prendo il nome
            tempName = str(name[0]).split('\\')
            self.file = tempName[-1]
            self.filesName.append(self.file)
            
            # Setto il bottone per il salvataggio attivo e disattivo quello della selezione
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.label_4.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.statusbar.showMessage("Seleziona l'azienda e salva la scelta")
            MainWindow.repaint()
        else:

            # In caso l'utente non ha selezionato alcun file, verrà visualizzato un msg di errore
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Errore")
            msg.setInformativeText("Non hai selezionato alcun file!")
            msg.setWindowTitle("Errore")
            msg.exec_()


    def save(self):
        self.azienda = self.comboBox.currentText()
        self.aziende.append(self.azienda)
        self.fileTemp.append(self.isEncrypted)

        if self.isEncrypted:
            self.fileTemp.append(self.dialogText.text())
        else:
            self.fileTemp.append('')

        self.files.append(self.fileTemp)

        # Reset dei widget e variabili
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.azienda = ''
        self.file = ''
        self.fileTemp = []

        self.listWidget.addItems(self.filesName)
        self.listWidget_2.addItems(self.aziende)
        self.listWidget.update()
        self.listWidget_2.update()
        MainWindow.repaint()

        self.pushButton.setEnabled(True)
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(True)
        self.pushButton_4.setEnabled(True)
        self.label_4.setEnabled(False)
        self.checkBox.setEnabled(False)
        MainWindow.repaint()
        self.label_5.setEnabled(False)
        self.dialogText.setEnabled(False)
        self.dialogText.setText('')
        self.statusbar.showMessage('Salvato')
        MainWindow.repaint()
        self.statusbar.showMessage('Avvia la conversione o seleziona un nuovo file')
        

    def avviaConversione(self):
        """
        Preparazione del programma alla conversione e raccolta
        del dati dai file .pdf e .xml
        """
    
        DizAziende = {}
        DizAziende['Eni'] = []
        DizAziende['Esso'] = []
        DizAziende['Union'] = []
        DizAziende['Autostrade'] = []
        DizAziende['VWL'] = []
        DizAziende['Arval'] = []

        # Conto le aziende
        for i in range(len(self.aziende)):
            if self.aziende[i] == 'Eni':
                DizAziende['Eni'].append(i)
            if self.aziende[i] == 'Esso':
                DizAziende['Esso'].append(i)
            if self.aziende[i] == 'Union':
                DizAziende['Union'].append(i)
            if self.aziende[i] == 'Autostrade':
                DizAziende['Autostrade'].append(i)
            if self.aziende[i] == "VWL":
                DizAziende['VWL'].append(i)
            if self.aziende[i] == 'Arval':
                DizAziende['Arval'].append(i)

        # Controllo della presenza del database
        canProceed = False
        files = os.listdir(setupGui.PATHWIN32 + '\\database\\')
        for file in files:
            if file.__contains__('database.xlsx'):
                canProceed = True

        if canProceed:
            # Conferma della conversione
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText('Sei sicuro di convertire questi file?')
            msg.setWindowTitle("Attenzione!")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            val = msg.exec_()
            if val == 1024:
                self.convertFiles(DizAziende)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Attenzione")
            msg.setInformativeText("Nessun database trovato!\nPer inserire un database: Opzioni -> Seleziona Database")
            msg.setWindowTitle("Attenzione!")
            msg.exec_()


    def eliminaDaLista(self):
        """
        Elimina dalla lista l'elemento selezionato
        """
        curItem = self.listWidget.currentRow()
        self.listWidget.takeItem(curItem)
        self.listWidget_2.takeItem(curItem)
        del self.aziende[curItem]
        del self.files[curItem]
        del self.filesName[curItem]


    def convertFiles(self, DizAziende):
        PDFPATH = setupGui.PATHWIN32 + '\\pdf\\'
        TXTPATH = setupGui.PATHWIN32 + '\\txt\\'    
        
        lenEni = len(DizAziende['Eni'])
        lenEsso = len(DizAziende['Esso'])
        lenUnion = len(DizAziende['Union'])
        lenAutostrade = len(DizAziende['Autostrade'])
        lenVWL = len(DizAziende['VWL'])
        lenArval = len(DizAziende['Arval'])

        # Pulizia dei file precedenti
        test = os.listdir(PDFPATH)
        for i in range(len(test)):
            os.popen('del ' + PDFPATH + test[i])
        
        test = os.listdir(setupGui.PATHWIN32 + '\\txt\\')
        for file in test:
            os.popen('del ' + setupGui.PATHWIN32 + '\\txt\\' + file)

        try:
            if not lenEni is 0:
                for i in range(lenEni):
                    if self.files[DizAziende['Eni'][i]][1] == False:    
                        path = self.files[DizAziende['Eni'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '.pdf' + ' ' + PDFPATH + 'eni' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Eni'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '-' + str(self.files[DizAziende['Eni'][i]][-1]) +'.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '-' + str(self.files[DizAziende['Eni'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'eni' + str(i) + '-' + str(self.files[DizAziende['Eni'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass

            if not lenEsso is 0:
                for i in range(lenEsso):
                    if self.files[DizAziende['Esso'][i]][1] == False:    
                        path = self.files[DizAziende['Esso'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '.pdf' + ' ' + PDFPATH + 'esso' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Esso'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '-' + str(self.files[DizAziende['Esso'][i]][-1]) +'.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '-' + str(self.files[DizAziende['Esso'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'esso' + str(i) + '-' + str(self.files[DizAziende['Esso'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass

            if not lenUnion is 0:
                for i in range(lenUnion):
                    if self.files[DizAziende['Union'][i]][1] == False:    
                        path = self.files[DizAziende['Union'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'union' + str(i) + '.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'union' + str(i) + '.pdf' + ' ' + PDFPATH + 'union' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Union'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'union' + str(i) + '-' + str(self.files[DizAziende['Union'][i]][-1]) +'.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'union' + str(i) + '-' + str(self.files[DizAziende['Union'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'union' + str(i) + '-' + str(self.files[DizAziende['Union'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass
            
            if not lenAutostrade is 0:
                for i in range(lenAutostrade):
                    if self.files[DizAziende['Autostrade'][i]][1] == False:    
                        path = self.files[DizAziende['Autostrade'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '.pdf' + ' ' + PDFPATH + 'autostrade' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Autostrade'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '-' + str(self.files[DizAziende['Autostrade'][i]][-1]) +'.pdf')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '-' + str(self.files[DizAziende['Autostrade'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'autostrade' + str(i) + '-' + str(self.files[DizAziende['Autostrade'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass

            if not lenVWL is 0:
                for i in range(lenVWL):
                    if self.files[DizAziende['VWL'][i]][1] == False:    
                        path = self.files[DizAziende['VWL'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'vwl' + str(i) + '.xml')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'vwl' + str(i) + '.xml' + ' ' + TXTPATH + 'vwl' + str(i) + '.xml'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['VWL'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'vwl' + str(i) + '-' + str(self.files[DizAziende['VWL'][i]][-1]) +'.xml')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'vwl' + str(i) + '-' + str(self.files[DizAziende['VWL'][i]][-1]) + '.xml' + ' ' + TXTPATH + 'vwl' + str(i) + '-' + str(self.files[DizAziende['VWL'][i]][-1]) + '.xml'
                        os.system(cmdFinal)
            else:
                pass

            if not lenArval is 0:
                for i in range(lenArval):
                    if self.files[DizAziende['Arval'][i]][1] == False:    
                        path = self.files[DizAziende['Arval'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'arval' + str(i) + '.xml')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'arval' + str(i) + '.xml' + ' ' + TXTPATH + 'arval' + str(i) + '.xml'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Arval'][i]][0]
                        temp = path.split('\\')
                        os.rename(path, path[:len(path) - len(temp[-1])] + 'arval' + str(i) + '-' + str(self.files[DizAziende['Arval'][i]][-1]) +'.xml')
                        cmdFinal = 'move ' + path[:len(path) - len(temp[-1])] + 'arval' + str(i) + '-' + str(self.files[DizAziende['Arval'][i]][-1]) + '.xml' + ' ' + TXTPATH + 'arval' + str(i) + '-' + str(self.files[DizAziende['Arval'][i]][-1]) + '.xml'
                        os.system(cmdFinal)
            else:
                pass
        except Exception:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Errore")
            msg.setInformativeText("C'è stato un errore durante lo spostamento dei file!")
            msg.setWindowTitle("Errore")
            msg.exec_()    


        pdfConverter.start()
        dataCollect.start()
        exportData.exporttofile()

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText("Conversione completata!")
        msg.setWindowTitle("Fine conversione")
        msg.exec_()
        
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.files = []
        self.filesName = []
        self.aziende = []
        self.pushButton_4.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.statusbar.showMessage('Pronto')
        MainWindow.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
