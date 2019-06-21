# -*- coding: utf-8 -*-
"""
    Gui Setup.py
"""

import getpass
import sys
import os
import ssl
from PyQt5 import QtCore, QtWidgets
from lib.Wget import wget
ssl._create_default_https_context = ssl._create_unverified_context


# -- Link per il download dei files utili --
LINKPDFTOTEXTWIN = 'https://drive.google.com/uc?export=download&id=19BTAN7mleq7yz2r48GaLPky_q_bvcEuJ'

# Variabili globali 
USERNAME = getpass.getuser()

PATHDOCUMENTSWIN32 = 'C:\\Users\\' + USERNAME + '\\Documents'

PATHWIN32 = PATHDOCUMENTSWIN32 + '\\PdfConverter-DataAnalyzer'

PATHSWIN = ['\\lib', '\\pdf','\\txt', '\\output']

class Ui_MainWindow(object):
    
    def setupUi(self, MainWindow):
        """
            Setup del programma
        """
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 164)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 291, 31))
        self.label.setObjectName("label")
        
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 80, 591, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.progressBar.update()
        
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 181, 16))
        self.label_2.setObjectName("label_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        
        MainWindow.setStatusBar(self.statusbar)
        
        self.actionEsci = QtWidgets.QAction(MainWindow)
        self.actionEsci.setObjectName("actionEsci")
       
        self.menuFile.addAction(self.actionEsci)
       
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        self.actionEsci.triggered.connect(MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Setup"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Setup PdfConverter &amp; DataAnalyzer</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "Sto installando il programma"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))

    def main(self):
        self.checkFirstInstallationWin()
        self.progressBar.setValue(100)
    

    def downloadUtilities(self):
        """
            Scarica tutte i file necessari per il corretto funzionamento del programma
        """
        
        if sys.platform.__contains__('win32'):
            wget.download(LINKPDFTOTEXTWIN, PATHWIN32 + '\\lib\\pdftotxt.exe')


    def checkFirstInstallationWin(self):

        dirPCDA = False
        dirLib = False 
        dirOut = False
        dirPdf = False
        dirTxt = False
        checkDir = False
        checkExe = False

        files = os.listdir(PATHDOCUMENTSWIN32)

        for file in files:
            if file == 'PdfConverter-DataAnalyzer':
                dirPCDA = True
                break

        if dirPCDA:
            files = os.listdir(PATHWIN32)
            
            for file in files:
                if file == 'lib':
                    dirLib = True
                if file == 'pdf':
                    dirPdf = True
                if file == 'txt':
                    dirTxt = True
                if file == 'output':
                    dirOut = True
            
            if dirLib is True and dirPdf is True and dirTxt is True and dirOut is True:
                checkDir = True
            else:
                if not dirLib:
                    os.mkdir(PATHWIN32 + '\\lib')
                if not dirPdf:
                    os.mkdir(PATHWIN32 + '\\pdf')
                if not dirTxt:
                    os.mkdir(PATHWIN32 + '\\txt')
                if not dirOut:
                    os.mkdir(PATHWIN32 + '\\output')

            if checkDir:
                fileExe = os.listdir(PATHWIN32 + '\\lib')
                for file in fileExe:
                    if file == 'pdftotxt.exe':
                        checkExe = True
                        break
            
            if not checkExe:
                wget.download(LINKPDFTOTEXTWIN, PATHWIN32 + '\\lib\\pdftotxt.exe')

        else:
            os.mkdir(PATHWIN32)
            for p in PATHWIN32:
                os.mkdir(PATHWIN32 + p)
            self.downloadUtilities()
            os.popen('chmod +x ' + PATHWIN32 + '/lib/pdftotxt')


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(MainWindow)
ui.main()

