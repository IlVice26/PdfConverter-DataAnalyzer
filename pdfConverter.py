"""
    Convertitore in Python 3.7 di file PDF in file TXT
    Lavoro svolto da Vicentini Elia per l'azienda Fornace S.R.L
"""

__version__ = '0.0.1'
__author__ = 'Vicentini Elia'

import os
import subprocess
import time
import setupGui

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

pathPdf = setupGui.PATHMACOS
pathExe = 'lib/pdftotxt'
filesToConvert = []
isDirPdf = False
isDirLib = False
isDirTxt = False


def converttotxt():
    """
        Converte tutti file PDF presenti all'interno della cartella pdf
        in file TXT
    """
    # Lista contenenti tutti i nomi dei file
    files = list(os.listdir(pathPdf + '/pdf'))

    # Controllo numero file
    if len(files) is 0:
        print("[-] Nessun file trovato nella cartella pdf")
        exit(1)
    
    # Controllo estensioni
    for i in range(len(files)):
        temp = files[i].split('.')
        if temp[-1] == "pdf":
            filesToConvert.append(files[i])

    for i in range(len(filesToConvert)):
        try:
            temp = filesToConvert[i].split('.')
            name = temp[0] + ".txt"
            os.system(pathExe + " -table pdf/" + filesToConvert[i] + " txt/" + name)
            time.sleep(1)
        except PermissionError:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Errore")
            msg.setInformativeText("Il file " + filesToConvert[i] + ' non può essere convertito!')
            msg.setWindowTitle("Errore")
            test = msg.exec_()
            print(test)


def tostring(list):
    """
        Trasforma una lista in una stringa
    """
    string = ""
    for i in range(len(list)):
        string = string + list[i]
    return string


def delrowseni():
    """
        Sistema il file eni.txt con le righe in cui sono presenti i dati
        essenziali
    """
    
    canDelRows = False
    filesToTrasform = []

    files = os.listdir('txt')

    for file in files:
        if file.__contains__('eni'):
            filesToTrasform.append(file)
            canDelRows = True

    if canDelRows:
        for filet in filesToTrasform:
            temp6 = filet.split('.')
            nameTransformed = temp6[0]   
            file = open('txt/' + filet, 'r', errors = 'ignore')
            file_out = open('txt/' + nameTransformed + '_out.txt', 'w')

            lines = file.readlines()

            rows = []

            for line in lines:
                temp1 = line.split('    ')
                if temp1[0].__contains__('Nr carta') or temp1[0].__contains__('.'):
                    if temp1[0].__contains__('Nr carta'):
                        rows.append(tostring(temp1) + '\n')
                    if temp1[0].__contains__('.'):
                        temp2 = temp1[0].split('.')
                        try:
                            int(temp2[0])
                            rows.append(tostring(temp1) + '\n')
                        except ValueError:
                            pass
            
            file_out.writelines(rows)
            file_out.close()
            file.close()
            os.system('rm txt/' + nameTransformed + '.txt')
    else:
        pass


def delrowsunion():
    """
        Sistema il file union.txt con le righe in cui sono presenti i dati
        essenziali
    """
    canDelRows = False
    filesToTrasform = []

    files = os.listdir('txt')

    for file in files:
        if file.__contains__('union'):
            filesToTrasform.append(file)
            canDelRows = True

    if canDelRows:
        for filet in filesToTrasform:
            temp6 = filet.split('.')
            nameTransformed = temp6[0]   
            file = open('txt/' + filet, 'r', errors = 'ignore')
            file_out = open('txt/' + nameTransformed + '_out.txt', 'w')

            rows = []

            lines = file.readlines()
            
            for line in lines:
                temp1 = line.split('        ')
                if not temp1[0] == '\n':
                    if temp1[0].__contains__('Targa: '):
                        rows.append(tostring(temp1) + '\n')
                    if temp1[0].__contains__('.'):
                        try:
                            temp2 = temp1[0].split('.')
                            int(temp2[0])
                            rows.append(tostring(temp1) + '\n')
                        except Exception:
                            pass
            
            file_out.writelines(rows)
            file_out.close()
            file.close()
            os.system('rm txt/' + nameTransformed + '.txt')
    else:
        pass


def delrowsesso():
    """
        Sistema il file esso.txt con le righe in cui sono presenti i dati
        essenziali
    """
    canDelRows = False
    filesToTrasform = []

    files = os.listdir('txt')

    for file in files:
        if file.__contains__('esso'):
            filesToTrasform.append(file)
            canDelRows = True

    if canDelRows:
        for filet in filesToTrasform:
            temp6 = filet.split('.')
            nameTransformed = temp6[0]
            file = open('txt/' + filet, 'r', errors = 'ignore')
            file_out = open('txt/' + nameTransformed + '_out.txt', 'w')


            rows = []

            lines = file.readlines()

            for line in lines:
                if (line.__contains__('gasolio') or line.__contains__('E-DIESEL') or line.__contains__('scontrino')):
                    rows.append(line)

            file_out.writelines(rows)
            file_out.close()
            file.close()
            os.system('rm txt/' + nameTransformed + '.txt')
    else:
        pass

def checkfileclosed(file):
    """
        Controlla se il file è chiuso correttamente
        Ritorna lo stato del file
    """
    return file.closed


def start():
    """
        Avvio del servizio tramite exportData.py
    """
    converttotxt()

    delrowseni()
    delrowsunion()
    delrowsesso()


if __name__ == "__main__":    
    start()