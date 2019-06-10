# -*- coding: utf-8 -*-

"""
    Scarica tutti i dati necessari per il corretto funzionamento del programma

    I dati scaricati verranno salvati nella directory 'Documenti'

    Lavoro svolto per l'azienda Fornace S.R.L
"""

__author__ = 'Vicentini Elia'
__version__ = '0.0.1'


import getpass
import sys
import os
import wget
import ssl
ssl._create_default_https_context = ssl._create_unverified_context


# -- Link per il download dei files utili --
LINKPDFTOTEXTWIN = 'https://drive.google.com/uc?export=download&id=19BTAN7mleq7yz2r48GaLPky_q_bvcEuJ'
LINKPDFTOTEXTMACOS = 'https://drive.google.com/uc?export=download&id=1ZkNeVEojpTKsL9EHwngbCfq4rdEtrx_u'

LINKPDFCONVERTER = 'https://drive.google.com/uc?export=download&id=1ns3jBwMxglkSOLzNU4TzoHD3eI3flLVg'
LINKDATACOLLECT = 'https://drive.google.com/uc?export=download&id=1uy_ZHjic5lbEK6bQNKTbiXYHXUfHPuWw'
LINKEXPORTDATA = 'https://drive.google.com/uc?export=download&id=1gh7XkRDZTMo6bwtvXUWUbMquwfgDulvf'

# Variabili globali 
USERNAME = getpass.getuser()
LIBRARIES = ['openpyxl', 'PySimpleGUI', 'wget']

PATHDOCUMENTSWIN32 = 'C:\\Users\\' + USERNAME + '\\Documents'
PATHDOCUMENTSMAC = '/Users/' + USERNAME + '/Documents'

PATHWIN32 = PATHDOCUMENTSWIN32 + '\\PdfConverter-DataAnalyzer'
PATHMACOS = PATHDOCUMENTSMAC + '/PdfConverter-DataAnalyzerTEST'

PATHSWIN = ['\\lib', '\\pdf','\\txt', '\\output']
PATHSMACOS = ['/lib', '/pdf','/txt', '/output']


def downloadUtilities():
    """
        Scarica tutte i file necessari per il corretto funzionamento del programma
    """
    
    if sys.platform.__contains__('win32'):
        print('[>] Download pdfConverter.py')
        wget.download(LINKPDFCONVERTER, PATHWIN32 + '\\pdfConverter.py')
        print('[+] pdfConverter.py scaricato')
        print('[>] Download dataCollect.py')
        wget.download(LINKDATACOLLECT, PATHWIN32 + '\\dataCollect.py')
        print('[+] dataCollect.py scaricato')
        print('[>] Download exportData.py')
        wget.download(LINKEXPORTDATA, PATHWIN32 + '\\exportData.py')
        print('[+] exportData.py scaricato')
    else:
        print('[>] Download pdftotext')
        wget.download(LINKPDFTOTEXTMACOS, PATHMACOS + '/lib/pdftotxt')
        print('[+] pdftotxt.exe scaricato')
        print('[>] Download pdfConverter.py')
        wget.download(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
        print('[+] pdfConverter.py scaricato')
        print('[>] Download dataCollect.py')
        wget.download(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
        print('[+] dataCollect.py scaricato')
        print('[>] Download exportData.py')
        wget.download(LINKEXPORTDATA, PATHMACOS + '/exportData.py')
        print('[+] exportData.py scaricato')

    

def checkPyLib():
    """
        Controlla che tutte le librerie necessarie siano installate correttamente
    """

    print('\n--- Controllo librerie Python3 ---')

    com_d = os.popen('python3 -m pip list --disable-pip-version-check')
    listd = com_d.read()

    for i in range(len(LIBRARIES)):
        if LIBRARIES[i] in listd:
            print('[+] Libreria ' + LIBRARIES[i] + ' già presente')
        else:
            print('[>] Download libreria ' + LIBRARIES[i])
            os.system('python3 -m pip install ' + LIBRARIES[i] +
                  ' -q --disable-pip-version-check')
            print('[+] Libreria ' + LIBRARIES[i] + ' installata')

    print('--- Controllo librerie completato ---')


def checkFirstInstallationWin32():
    """
        Controlla che tutte le directory siano state create, in caso
        negativo crea o scarica le directory/files necessari
    """
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

    files = os.listdir(PATHDOCUMENTSWIN32)

    for file in files:
        if file == 'PdfConverter-DataAnalyzer':
            print('Cartella Esistente')
            dirPCDA = True

    if dirPCDA:
        print('Controllo files e directory esterne')
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
            print('Tutte le cartelle esistenti')
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
            print('pdftotxt.exe scaricato')
        
        checkPyLib()

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
                wget.download(LINKPDFCONVERTER, PATHWIN32 + '\\pdfConverter.py')
                print('pdfConverter.py scaricato')
            if not checkdatacollect:
                wget.download(LINKDATACOLLECT, PATHWIN32 + '\\dataCollect.py')
                print('dataCollect.py scaricato')
            if not checkexportdata:
                wget.download(LINKEXPORTDATA, PATHWIN32 + '\\exportData.py')
                print('exportData.py scaricato')

    else:
        os.mkdir(PATHWIN32)
        for p in PATHSWIN:
            os.mkdir(PATHWIN32 + p)
        
        print('Tutte le cartelle create')

        wget.download(LINKPDFTOTEXTWIN, PATHWIN32 + '\\lib\\pdftotxt.exe')
        print('pdftotxt.exe scaricato')

        checkPyLib()
        downloadUtilities()
    

def checkFirstInstallationMac():

    print('\n--- Controllo directory ---')

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
            print('[+] Cartella PdfConverter-DataAnalyzer TEST esistente')
            dirPCDA = True
            break

    if dirPCDA:
        print('\n[>] Controllo files e directory')
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
            print('[+] Tutte le directory esistenti')
        else:
            if not dirLib:
                os.mkdir(PATHMACOS + '/lib')
            if not dirPdf:
                os.mkdir(PATHMACOS + '/pdf')
            if not dirTxt:
                os.mkdir(PATHMACOS + '/txt')
            if not dirOut:
                os.mkdir(PATHMACOS + '/output')
            print('[+] Tutte le directory create')

        print('\n[>] Controllo utilities')
        if checkDir:
            fileExe = os.listdir(PATHMACOS + '/lib')
            for file in fileExe:
                if file == 'pdftotxt':
                    checkExe = True
                    break
        
        if not checkExe:
            print('[>] Download pdftotext')
            wget.download(LINKPDFTOTEXTMACOS, PATHMACOS + '/lib/pdftotxt')
            print('[+] Libreria pdftotxt scaricata')

        
        for file in files:
            if file == 'pdfConverter.py':
                checkpdfconverter = True
            if file == 'dataCollect.py':
                checkdatacollect = True
            if file == 'exportData.py':
                checkexportdata = True

        if checkpdfconverter is True and checkdatacollect is True and checkexportdata is True:
            pass
            print('[+] Controllo utilities completato')
        else:
            if not checkpdfconverter:
                wget.download(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
                print('[+] pdfConverter.py scaricato')
            if not checkdatacollect:
                wget.download(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
                print('[+] dataCollect.py scaricato')
            if not checkexportdata:
                wget.download(LINKEXPORTDATA, PATHMACOS + '/exportData.py')
                print('[+] exportData.py scaricato')

    else:

        print('[-] Cartella PdfConverter-DataAnalyzer TEST non esistente')
        
        print('\n[>] Creazione delle cartelle in corso')
        os.mkdir(PATHMACOS)
        for p in PATHSMACOS:
            os.mkdir(PATHMACOS + p)
        
        print('[+] Tutte le cartelle create\n\n[>] Download utilities in corso')
        downloadUtilities()
        print('[+] Download utilities completato')
        os.system('chmod +x ' + PATHMACOS + '/lib/pdftotext')

    print('--- Controllo directory completato ---\n\n--- Installazione completata ---')


def main():
    checkPyLib()    
    platform = sys.platform
    if platform.__contains__('win32'):
        checkFirstInstallationWin32()
    else:
        checkFirstInstallationMac()
        return True


if __name__ == "__main__":
    main()
