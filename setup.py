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
try:
    import urllib.request
except:
    pass

# -- Link per il download dei files utili --
LINKPDFTOTEXT = 'https://drive.google.com/uc?export=download&id=19BTAN7mleq7yz2r48GaLPky_q_bvcEuJ'
LINKPDFCONVERTER = 'https://drive.google.com/uc?export=download&id=1ns3jBwMxglkSOLzNU4TzoHD3eI3flLVg'
LINKDATACOLLECT = 'https://drive.google.com/uc?export=download&id=1uy_ZHjic5lbEK6bQNKTbiXYHXUfHPuWw'
LINKEXPORTDATA = 'https://drive.google.com/uc?export=download&id=1gh7XkRDZTMo6bwtvXUWUbMquwfgDulvf'

# Variabili globali 
USERNAME = getpass.getuser()
LIBRARIES = ['openpyxl', 'PySimpleGUI']

PATHDOCUMENTSWIN32 = 'C:\\Users\\' + USERNAME + '\\Documents'
PATHDOCUMENTSUNIX = '/home/' + USERNAME
PATHDOCUMENTSMAC = '/Users/' + USERNAME

PATHWIN32 = PATHDOCUMENTSWIN32 + '\\PdfConverter-DataAnalyzer'
PATHUNIX = PATHDOCUMENTSUNIX + '/PdfConverter-DataAnalyzer'
PATHMACOS = PATHDOCUMENTSMAC + '/Documents/PdfConverter-DataAnalyzer TEST'

PATHSWIN = ['\\lib', '\\pdf','\\txt', '\\output']
PATHSUNIX = ['/lib', '/pdf','/txt', '/output']
PATHSMACOS = ['/lib', '/pdf','/txt', '/output']


def downloadLibrariesUnix():
    """
        Scarica tutte i file necessari per il corretto funzionamento del programma
    """
    print('Download file necessari')
    urllib.request.urlretrieve(LINKPDFCONVERTER, PATHUNIX + '/pdfConverter.py')
    print('pdfConverter.py scaricato')
    urllib.request.urlretrieve(LINKDATACOLLECT, PATHUNIX + '/dataCollect.py')
    print('dataCollect.py scaricato')
    urllib.request.urlretrieve(LINKEXPORTDATA, PATHUNIX + '/exportData.py')
    print('exportData.py scaricato')


def downloadLibrariesWin32():
    """
        Scarica tutte i file necessari per il corretto funzionamento del programma
    """
    print('Download file necessari')
    urllib.request.urlretrieve(LINKPDFCONVERTER, PATHWIN32 + '\\pdfConverter.py')
    print('pdfConverter.py scaricato')
    urllib.request.urlretrieve(LINKDATACOLLECT, PATHWIN32 + '\\dataCollect.py')
    print('dataCollect.py scaricato')
    urllib.request.urlretrieve(LINKEXPORTDATA, PATHWIN32 + '\\exportData.py')
    print('exportData.py scaricato')
    


def checkPyLib():
    """
        Controlla che tutte le librerie necessarie siano installate correttamente
    """
    com_d = os.popen('python -m pip list --disable-pip-version-check')
    listd = com_d.read()

    for i in range(len(LIBRARIES)):
        if LIBRARIES[i] in listd:
            print('Libreria ' + LIBRARIES[i] + ' già presente')
        else:
            print('Download libreria ' + LIBRARIES[i])
            os.system('python -m pip install ' + LIBRARIES[i] +
                  ' -q --disable-pip-version-check')
            print('Libreria ' + LIBRARIES[i] + ' installata')


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
    checkLib = False
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
            urllib.request.urlretrieve(LINKPDFTOTEXT, PATHWIN32 + '\\lib\\pdftotxt.exe')
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
            checkLib = True
        else:
            if not checkpdfconverter:
                urllib.request.urlretrieve(LINKPDFCONVERTER, PATHWIN32 + '\\pdfConverter.py')
                print('pdfConverter.py scaricato')
            if not checkdatacollect:
                urllib.request.urlretrieve(LINKDATACOLLECT, PATHWIN32 + '\\dataCollect.py')
                print('dataCollect.py scaricato')
            if not checkexportdata:
                urllib.request.urlretrieve(LINKEXPORTDATA, PATHWIN32 + '\\exportData.py')
                print('exportData.py scaricato')

    else:
        os.mkdir(PATHWIN32)
        for p in PATHSWIN:
            os.mkdir(PATHWIN32 + p)
        
        print('Tutte le cartelle create')

        urllib.request.urlretrieve(LINKPDFTOTEXT, PATHWIN32 + '\\lib\\pdftotxt.exe')
        print('pdftotxt.exe scaricato')

        checkPyLib()
        downloadLibrariesWin32()
        

def checkFirstInstallationUnix():
    
    dirPCDA = False
    dirLib = False 
    dirOut = False
    dirPdf = False
    dirTxt = False
    checkDir = False
    checkExe = False
    checkLib = False
    checkpdfconverter = False
    checkdatacollect = False
    checkexportdata = False

    files = os.listdir(PATHDOCUMENTSUNIX)

    for file in files:
        if file == 'PdfConverter-DataAnalyzer':
            print('Cartella Esistente')
            dirPCDA = True

    if dirPCDA:
        print('Controllo files e directory esterne')
        files = os.listdir(PATHUNIX)
        
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
                os.mkdir(PATHUNIX + '/lib')
            if not dirPdf:
                os.mkdir(PATHUNIX + '/pdf')
            if not dirTxt:
                os.mkdir(PATHUNIX + '/txt')
            if not dirOut:
                os.mkdir(PATHUNIX + '/output')

        if checkDir:
            fileExe = os.listdir(PATHUNIX + '/lib')
            for file in fileExe:
                if file == 'pdftotxt.exe':
                    checkExe = True
                    break
        
        if not checkExe:
            urllib.request.urlretrieve(LINKPDFTOTEXT, PATHUNIX + '/lib/pdftotxt.exe')
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
            checkLib = True
        else:
            if not checkpdfconverter:
                urllib.request.urlretrieve(LINKPDFCONVERTER, PATHUNIX + '//pdfConverter.py')
                print('pdfConverter.py scaricato')
            if not checkdatacollect:
                urllib.request.urlretrieve(LINKDATACOLLECT, PATHUNIX + '//dataCollect.py')
                print('dataCollect.py scaricato')
            if not checkexportdata:
                urllib.request.urlretrieve(LINKEXPORTDATA, PATHUNIX + '//exportData.py')
                print('exportData.py scaricato')

    else:
        os.mkdir(PATHUNIX)
        # for p in PATHSWIN:
        os.system('cd PdfConverter-DataAnalyzer && mkdir test')
        
        print('Tutte le cartelle create')

        urllib.request.urlretrieve(LINKPDFTOTEXT, PATHUNIX + '/lib/pdftotxt.exe')
        print('pdftotxt.exe scaricato')

        checkPyLib()
        downloadLibrariesUnix()


def checkFirstInstallationMac():

    dirPCDA = False
    dirLib = False 
    dirOut = False
    dirPdf = False
    dirTxt = False
    checkDir = False
    checkExe = False
    checkLib = False
    checkpdfconverter = False
    checkdatacollect = False
    checkexportdata = False

    files = os.listdir(PATHDOCUMENTSMAC)

    for file in files:
        if file == 'PdfConverter-DataAnalyzer TEST':
            print('Cartella Esistente')
            dirPCDA = True

    if dirPCDA:
        print('Controllo files e directory esterne')
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
            print('Tutte le cartelle esistenti')
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
                if file == 'pdftotxt.exe':
                    checkExe = True
                    break
        
        if not checkExe:
            urllib.request.urlretrieve(LINKPDFTOTEXT, PATHMACOS + '/lib/pdftotxt.exe')
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
            checkLib = True
        else:
            if not checkpdfconverter:
                urllib.request.urlretrieve(LINKPDFCONVERTER, PATHMACOS + '/pdfConverter.py')
                print('pdfConverter.py scaricato')
            if not checkdatacollect:
                urllib.request.urlretrieve(LINKDATACOLLECT, PATHMACOS + '/dataCollect.py')
                print('dataCollect.py scaricato')
            if not checkexportdata:
                urllib.request.urlretrieve(LINKEXPORTDATA, PATHMACOS + '/exportData.py')
                print('exportData.py scaricato')

    else:
        os.mkdir(PATHMACOS)
        for p in PATHMACOS:
            os.mkdir(PATHSMACOS + p)
        
        print('Tutte le cartelle create')

        urllib.request.urlretrieve(LINKPDFTOTEXT, PATHUNIX + '/lib/pdftotxt.exe')
        print('pdftotxt.exe scaricato')

        """
        checkPyLib()
        downloadLibrariesUnix()
        """


if __name__ == "__main__":    
    platform = sys.platform
    if platform.__contains__('win32'):
        checkFirstInstallationWin32()
    elif platform.__contains__('linux'):
        checkFirstInstallationUnix()
    else:
        checkFirstInstallationMac()