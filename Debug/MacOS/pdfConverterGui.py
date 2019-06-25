# -*- coding: utf-8 -*-
"""
    Gui per pdfConverter.py

    Lavoro svolto da Vicentini Elia
"""

import os
import sys
import webbrowser

from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QApplication, QFileDialog, QCheckBox, QLineEdit

import util.setupGui as setupGui
import util.dataCollect as dataCollect
import util.exportData as exportData
import util.pdfConverter as pdfConverter


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
        MainWindow.resize(740, 390)
        MainWindow.setWindowOpacity(1.0)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Titolo
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 471, 31))
        self.label.setObjectName("label")
        
        # Prima lista
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(280, 110, 221, 201))
        self.listWidget.setObjectName("listWidget")
        
        # Titolo prima lista
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(280, 90, 221, 16))
        self.label_2.setObjectName("label_2")
        
        # Bottone Scegli File
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 110, 121, 32))
        self.pushButton.setObjectName("pushButton")
        
        # Bottone Salva File
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 200, 241, 32))
        self.pushButton_2.setObjectName("pushButton_2")
        
        # Seconda lista 
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(510, 110, 221, 201))
        self.listWidget_2.setObjectName("listWidget_2")
        
        # Titolo seconda lista
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(510, 90, 59, 16))
        self.label_3.setObjectName("label_3")
        
        # Combobox (Eni, Esso, Union)
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(140, 109, 121, 32))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        
        # Bottone Avvia Conversione
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 280, 241, 32))
        self.pushButton_3.setObjectName("pushButton_3")
        
        # Bottone Elimina oggetti
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(340, 310, 101, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        
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
        MainWindow.setStatusBar(self.statusbar)
        self.actionGit = QtWidgets.QAction(MainWindow)
        self.actionGit.setObjectName("actionGit")
        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")
        self.actionAutore_progetto = QtWidgets.QAction(MainWindow)
        self.actionAutore_progetto.setObjectName("actionAutore_progetto")
        self.menuFile.addAction(self.actionGit)
        self.menuFile.addAction(self.actionAutore_progetto)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionEsci)
        self.menubar.addAction(self.menuFile.menuAction())

        # Titolo checkBox7 
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(28, 145, 221, 16))
        self.label_4.setObjectName("label_4")

        # CheckBox
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(132, 143, 20, 20))
        self.checkBox.setObjectName("checkBox")
        
        # Titolo dialogText
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(28, 173, 221, 16))
        self.label_5.setObjectName("label_5")

        # DialogTextChiave
        self.dialogText = QtWidgets.QLineEdit(self.centralwidget)
        self.dialogText.setGeometry(QtCore.QRect(78, 171, 175, 20))
        self.dialogText.setObjectName("dialogText")

        # Setup iniziale dei bottoni
        self.pushButton_2.setEnabled(False)
        self.pushButton_3.setEnabled(False)
        self.pushButton_4.setEnabled(False)
        self.label_4.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.label_5.setEnabled(False)
        self.dialogText.setEnabled(False)

        # Azioni di ogni bottone
        self.actionAutore_progetto.triggered.connect(self.openAutoreProgetto)
        self.actionGit.triggered.connect(self.openGitPage)
        self.actionEsci.triggered.connect(self.closeWindow)
        self.pushButton.clicked.connect(self.get_file)
        self.pushButton_2.clicked.connect(self.save)
        self.pushButton_3.clicked.connect(self.avviaConversione)
        self.pushButton_4.clicked.connect(self.eliminaDaLista)
        self.checkBox.clicked.connect(self.checkBoxEncrypted)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pdf Converter & Data Analyzer"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:600; font-style:italic;\">Pdf Converter &amp; Data Analyzer </span><span style=\" font-size:24pt; font-weight:600; font-style:italic; vertical-align:sub;\">by Vicentini Elia</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "File pronti per la conversione"))
        self.pushButton.setText(_translate("MainWindow", "Seleziona file"))
        self.pushButton_2.setText(_translate("MainWindow", "Salva scelta"))
        self.label_3.setText(_translate("MainWindow", "Azienda"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Eni"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Esso"))
        self.comboBox.setItemText(2, _translate("MainWindow", "Union"))
        self.comboBox.setItemText(3, _translate("MainWindow", "Autostrade"))
        self.pushButton_3.setText(_translate("MainWindow", "Avvia conversione"))
        self.pushButton_4.setText(_translate("MainWindow", "Elimina"))
        self.menuFile.setTitle(_translate("MainWindow", "Info"))
        self.actionGit.setText(_translate("MainWindow", "Git"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))
        self.actionAutore_progetto.setText(_translate("MainWindow", "Autore progetto"))
        self.label_4.setText(_translate("Mainwindow", "Il file è criptato?"))
        self.label_5.setText(_translate("Mainwindow", "Chiave"))
        MainWindow.setFixedSize(MainWindow.size())

    def openAutoreProgetto(self):
        """
        Apre la pagina di Instagram dell'autore
        """
        webbrowser.open_new_tab('https://www.instagram.com/eliavicentiniii/')

    def openGitPage(self):
        """
        Apre la pagina web di GitHub
        """
        webbrowser.open_new_tab('https://gitlab.com/furnax/stage/pdfconverter-dataanalyzer')

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
        name = QFileDialog.getOpenFileName(None, 'Open File', '', '*.pdf')
        tempN = name[0]

        # Controllo se il file è stato selezionato
        if not tempN is '':

            # In caso positivo aggiungo la path assoluta ad una lista temporanea
            self.fileTemp.append(name[0])
            
            # Prendo il nome
            tempName = str(name[0]).split('/')
            self.file = tempName[-1]
            self.filesName.append(self.file)
            
            # Setto il bottone per il salvataggio attivo e disattivo quello della selezione
            self.pushButton.setEnabled(False)
            self.pushButton_2.setEnabled(True)
            self.label_4.setEnabled(True)
            self.checkBox.setEnabled(True)
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
        MainWindow.repaint()
        

    def avviaConversione(self):

        DizAziende = {}
        DizAziende['Eni'] = []
        DizAziende['Esso'] = []
        DizAziende['Union'] = []
        DizAziende['Autostrade'] = []

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

        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText('Sei sicuro di convertire questi file?')
        msg.setWindowTitle("Attenzione!")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        val = msg.exec_()
        if val == 1024:
            self.convertFiles(DizAziende)

    def eliminaDaLista(self):
        curItem = self.listWidget.currentRow()
        self.listWidget.takeItem(curItem)
        self.listWidget_2.takeItem(curItem)
        del self.aziende[curItem]
        del self.files[curItem]
        del self.filesName[curItem]


    def convertFiles(self, DizAziende):
        PDFPATH = setupGui.PATHMACOS + '/pdf/'

        lenEni = len(DizAziende['Eni'])
        lenEsso = len(DizAziende['Esso'])
        lenUnion = len(DizAziende['Union'])
        lenAutostrade = len(DizAziende['Autostrade'])

        # Pulizia dei file precedenti
        test = os.listdir(PDFPATH)
        for i in range(len(test)):
            os.popen('rm ' + PDFPATH + test[i])
        
        test = os.listdir(setupGui.PATHMACOS + '/txt/')
        for file in test:
            os.popen('rm ' + setupGui.PATHMACOS + '/txt/' + file)

        try:
            if not lenEni is 0:
                for i in range(lenEni):
                    if self.files[DizAziende['Eni'][i]][1] == False:    
                        path = self.files[DizAziende['Eni'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '.pdf' + ' ' + PDFPATH + 'eni' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Eni'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '-' + str(self.files[DizAziende['Eni'][i]][-1]) +'.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'eni' + str(i) + '-' + str(self.files[DizAziende['Eni'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'eni' + str(i) + '-' + str(self.files[DizAziende['Eni'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass

            if not lenEsso is 0:
                for i in range(lenEsso):
                    if self.files[DizAziende['Esso'][i]][1] == False:    
                        path = self.files[DizAziende['Esso'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '.pdf' + ' ' + PDFPATH + 'esso' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Esso'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '-' + str(self.files[DizAziende['Esso'][i]][-1]) +'.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'esso' + str(i) + '-' + str(self.files[DizAziende['Esso'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'esso' + str(i) + '-' + str(self.files[DizAziende['Esso'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass

            if not lenUnion is 0:
                for i in range(lenUnion):
                    if self.files[DizAziende['Union'][i]][1] == False:    
                        path = self.files[DizAziende['Union'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'union' + str(i) + '.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'union' + str(i) + '.pdf' + ' ' + PDFPATH + 'union' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Union'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'union' + str(i) + '-' + str(self.files[DizAziende['Union'][i]][-1]) +'.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'union' + str(i) + '-' + str(self.files[DizAziende['Union'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'union' + str(i) + '-' + str(self.files[DizAziende['Union'][i]][-1]) + '.pdf'
                        os.system(cmdFinal)
            else:
                pass
            
            if not lenAutostrade is 0:
                for i in range(lenAutostrade):
                    if self.files[DizAziende['Autostrade'][i]][1] == False:    
                        path = self.files[DizAziende['Autostrade'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '.pdf' + ' ' + PDFPATH + 'autostrade' + str(i) + '.pdf'
                        os.system(cmdFinal)
                    else:
                        path = self.files[DizAziende['Autostrade'][i]][0]
                        temp = path.split('/')
                        cmdRename = 'mv -n "' + path + '" ' + path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '-' + str(self.files[DizAziende['Autostrade'][i]][-1]) +'.pdf'
                        os.system(cmdRename)
                        cmdFinal = 'mv -n ' + path[:len(path) - len(temp[-1])] + 'autostrade' + str(i) + '-' + str(self.files[DizAziende['Autostrade'][i]][-1]) + '.pdf' + ' ' + PDFPATH + 'autostrade' + str(i) + '-' + str(self.files[DizAziende['Autostrade'][i]][-1]) + '.pdf'
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
        """
        exportData.exporttofile()
        """

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
        MainWindow.repaint()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
