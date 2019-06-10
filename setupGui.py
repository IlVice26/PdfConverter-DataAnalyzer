# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setup.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 197)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 151, 31))
        self.label.setObjectName("label")
        self.execution = QtWidgets.QLabel(self.centralwidget)
        self.execution.setGeometry(QtCore.QRect(20, 50, 341, 51))
        self.execution.setText("")
        self.execution.setObjectName("execution")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(20, 110, 591, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.startSetup = QtWidgets.QPushButton(self.centralwidget)
        self.startSetup.setGeometry(QtCore.QRect(510, 10, 113, 32))
        self.startSetup.setObjectName("startSetup")
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
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:18pt;\">Setup Program</span></p></body></html>"))
        self.startSetup.setText(_translate("MainWindow", "Start Setup"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionEsci.setText(_translate("MainWindow", "Esci"))

    def downloadUtilities(self):
        """
            Scarica tutte i file necessari per il corretto funzionamento del programma
        """
        
        if sys.platform.__contains__('win32'):
            self.execution.setText('[>] Download pdfConverter.py')
            wget.download(LINKPDFCONVERTER, PATHWIN32 + '\\pdfConverter.py')
            self.execution.setText('[+] pdfConverter.py scaricato')
            self.execution.setText('[>] Download dataCollect.py')
            wget.download(LINKDATACOLLECT, PATHWIN32 + '\\dataCollect.py')
            self.execution.setText('[+] dataCollect.py scaricato')
            self.execution.setText('[>] Download exportData.py')
            wget.download(LINKEXPORTDATA, PATHWIN32 + '\\exportData.py')
            self.execution.setText('[+] exportData.py scaricato')
        else:
            self.execution.setText('[>] Download pdftotext')
            wget.download(LINKPDFTOTEXTMACOS, PATHMACOS + '/lib/pdftotxt')
            self.execution.setText('[+] pdftotxt.exe scaricato')
            self.execution.setText('[>] Download pdfConverter.py')
            wget.download(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
            self.execution.setText('[+] pdfConverter.py scaricato')
            self.execution.setText('[>] Download dataCollect.py')
            wget.download(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
            self.execution.setText('[+] dataCollect.py scaricato')
            self.execution.setText('[>] Download exportData.py')
            wget.download(LINKEXPORTDATA, PATHMACOS + '/exportData.py')
            self.execution.setText('[+] exportData.py scaricato')


    def checkPyLib(self):
        """
            Controlla che tutte le librerie necessarie siano installate correttamente
        """

        self.execution.setText('--- Controllo librerie Python3 ---')

        com_d = os.popen('python3 -m pip list --disable-pip-version-check')
        listd = com_d.read()

        for i in range(len(LIBRARIES)):
            if LIBRARIES[i] in listd:
                self.execution.setText('[+] Libreria ' + LIBRARIES[i] + ' già presente')
            else:
                self.execution.setText('[>] Download libreria ' + LIBRARIES[i])
                os.system('python3 -m pip install ' + LIBRARIES[i] +
                    ' -q --disable-pip-version-check')
                self.execution.setText('[+] Libreria ' + LIBRARIES[i] + ' installata')

        self.execution.setText('--- Controllo librerie completato ---')

    def checkFirstInstallationMac(self):

        self.execution.setText('--- Controllo directory ---')

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
                self.execution.setText('[+] Cartella PdfConverter-DataAnalyzer TEST esistente')
                dirPCDA = True
                break

        if dirPCDA:
            self.execution.setText('\n[>] Controllo files e directory')
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
                self.execution.setText('[+] Tutte le directory esistenti')
            else:
                if not dirLib:
                    os.mkdir(PATHMACOS + '/lib')
                if not dirPdf:
                    os.mkdir(PATHMACOS + '/pdf')
                if not dirTxt:
                    os.mkdir(PATHMACOS + '/txt')
                if not dirOut:
                    os.mkdir(PATHMACOS + '/output')
                self.execution.setText('[+] Tutte le directory create')

            self.execution.setText('\n[>] Controllo utilities')
            if checkDir:
                fileExe = os.listdir(PATHMACOS + '/lib')
                for file in fileExe:
                    if file == 'pdftotxt':
                        checkExe = True
                        break
            
            if not checkExe:
                self.execution.setText('[>] Download pdftotext')
                wget.download(LINKPDFTOTEXTMACOS, PATHMACOS + '/lib/pdftotxt')
                self.execution.setText('[+] Libreria pdftotxt scaricata')

            
            for file in files:
                if file == 'pdfConverter.py':
                    checkpdfconverter = True
                if file == 'dataCollect.py':
                    checkdatacollect = True
                if file == 'exportData.py':
                    checkexportdata = True

            if checkpdfconverter is True and checkdatacollect is True and checkexportdata is True:
                pass
                self.execution.setText('[+] Controllo utilities completato')
            else:
                if not checkpdfconverter:
                    wget.download(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
                    self.execution.setText('[+] pdfConverter.py scaricato')
                if not checkdatacollect:
                    wget.download(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
                    self.execution.setText('[+] dataCollect.py scaricato')
                if not checkexportdata:
                    wget.download(LINKEXPORTDATA, PATHMACOS + '/exportData.py')
                    self.execution.setText('[+] exportData.py scaricato')

        else:

            self.execution.setText('[-] Cartella PdfConverter-DataAnalyzer TEST non esistente')
            
            self.execution.setText('\n[>] Creazione delle cartelle in corso')
            os.mkdir(PATHMACOS)
            for p in PATHSMACOS:
                os.mkdir(PATHMACOS + p)
            
            self.execution.setText('[+] Tutte le cartelle create\n\n[>] Download utilities in corso')
            downloadUtilities()
            self.execution.setText('[+] Download utilities completato')
            os.system('chmod +x ' + PATHMACOS + '/lib/pdftotext')

        self.execution.setText('--- Controllo directory completato ---\n\n--- Installazione completata ---')


    def main(self):
        self.checkPyLib()    
        platform = sys.platform
        if platform.__contains__('win32'):
            checkFirstInstallationWin32()
        else:
            time.sleep(5)
            self.checkFirstInstallationMac()
            return True



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
