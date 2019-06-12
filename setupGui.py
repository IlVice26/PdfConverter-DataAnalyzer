# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
import getpass
import sys
import os
import wget
import ssl
import time
ssl._create_default_https_context = ssl._create_unverified_context

# -- Link per il download dei files utili --
LINKPDFTOTEXTWIN = 'https://drive.google.com/uc?export=download&id=19BTAN7mleq7yz2r48GaLPky_q_bvcEuJ'
LINKPDFTOTEXTMACOS = 'https://drive.google.com/uc?export=download&id=1ZkNeVEojpTKsL9EHwngbCfq4rdEtrx_u'

LINKPDFCONVERTER = 'https://drive.google.com/uc?export=download&id=1ns3jBwMxglkSOLzNU4TzoHD3eI3flLVg'
LINKDATACOLLECT = 'https://drive.google.com/uc?export=download&id=1uy_ZHjic5lbEK6bQNKTbiXYHXUfHPuWw'
LINKEXPORTDATA = 'https://drive.google.com/uc?export=download&id=1gh7XkRDZTMo6bwtvXUWUbMquwfgDulvf'

# Variabili globali 
USERNAME = getpass.getuser()
LIBRARIES = ['openpyxl', 'PySimpleGUI', 'wget', 'PyQt5', 'sip']

PATHDOCUMENTSWIN32 = 'C:\\Users\\' + USERNAME + '\\Documents'
PATHDOCUMENTSMAC = '/Users/' + USERNAME + '/Documents'

PATHWIN32 = PATHDOCUMENTSWIN32 + '\\PdfConverter-DataAnalyzer'
PATHMACOS = PATHDOCUMENTSMAC + '/PdfConverter-DataAnalyzerTEST'

PATHSWIN = ['\\lib', '\\pdf','\\txt', '\\output']
PATHSMACOS = ['/lib', '/pdf','/txt', '/output']

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
        
        self.checkPyLib()
        self.checkFirstInstallationMac()
        self.progressBar.setValue(100)
    
    def downloadUtilities(self):
        """
            Scarica tutte i file necessari per il corretto funzionamento del programma
        """
        
        if sys.platform.__contains__('win32'):
            wget.download(LINKPDFCONVERTER, PATHWIN32 + '\\pdfConverter.py')
            wget.download(LINKDATACOLLECT, PATHWIN32 + '\\dataCollect.py')
            wget.download(LINKEXPORTDATA, PATHWIN32 + '\\exportData.py')
        else:
            wget.download(LINKPDFTOTEXTMACOS, PATHMACOS + '/lib/pdftotxt')
            wget.download(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
            wget.download(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
            wget.download(LINKEXPORTDATA, PATHMACOS + '/exportData.py')

    def checkPyLib(self):
        """
            Controlla che tutte le librerie necessarie siano installate correttamente
        """

        com_d = os.popen('python3 -m pip list --disable-pip-version-check')
        listd = com_d.read()

        for i in range(len(LIBRARIES)):
            if LIBRARIES[i] in listd:
                pass
            else:
                os.system('python3 -m pip install ' + LIBRARIES[i] +
                    ' -q --disable-pip-version-check')

    def checkFirstInstallationMac(self):

        dirPCDA = False
        dirLib = False 
        dirOut = False
        dirPdf = False
        dirTxt = False
        checkDir = False
        checkExe = False
        checkpdfconverter = False
        checkdatacollect = False
        checkexportdata = False

        files = os.listdir(PATHDOCUMENTSMAC)

        for file in files:
            if file == 'PdfConverter-DataAnalyzerTEST':
                dirPCDA = True
                break

        if dirPCDA:
            files = os.listdir(PATHMACOS)
            
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
                    os.mkdir(PATHMACOS + '/lib')
                if not dirPdf:
                    os.mkdir(PATHMACOS + '/pdf')
                if not dirTxt:
                    os.mkdir(PATHMACOS + '/txt')
                if not dirOut:
                    os.mkdir(PATHMACOS + '/output')

            if checkDir:
                fileExe = os.listdir(PATHMACOS + '/lib')
                for file in fileExe:
                    if file == 'pdftotxt':
                        checkExe = True
                        break
            
            if not checkExe:
                wget.download(LINKPDFTOTEXTMACOS, PATHMACOS + '/lib/pdftotxt')
            
            for file in files:
                if file == 'pdfConverter.py':
                    checkpdfconverter = True
                if file == 'dataCollect.py':
                    checkdatacollect = True
                if file == 'exportData.py':
                    checkexportdata = True

            if checkpdfconverter is True and checkdatacollect is True and checkexportdata is True:
                pass
            else:
                if not checkpdfconverter:
                    wget.download(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
                if not checkdatacollect:
                    wget.download(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
                if not checkexportdata:
                    wget.download(LINKEXPORTDATA, PATHMACOS + '/exportData.py')

        else:
            os.mkdir(PATHMACOS)
            for p in PATHSMACOS:
                os.mkdir(PATHMACOS + p)
            self.downloadUtilities()
            os.popen('chmod +x ' + PATHMACOS + '/lib/pdftotxt')

def setData():
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    ui.main()