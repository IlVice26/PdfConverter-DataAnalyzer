"""
    Convertitore in Python 3.7 di file PDF in file TXT
    Lavoro svolto da Vicentini Elia per l'azienda Fornace S.R.L
"""

__version__ = '0.0.1'
__author__ = 'Vicentini Elia'

import os
import subprocess
import time


pathExe = 'lib\\pdftotext.exe'
filesToConvert = []
isDirPdf = False
isDirLib = False
isDirTxt = False


def ctrlfiles():
    """
        Controlla se sono presenti tutti file e le cartelle necessarie per il
        corretto funzionamento
    """
    global isDirPdf, isDirLib, isDirTxt

    canExport = True
    files = os.listdir('.')

    for i in range(len(files)):
        if (files[i] == 'pdf'):
            isDirPdf = True
        if (files[i] == 'lib'):
            isDirLib = True
        if (files[i] == 'txt'):
            isDirTxt = True

    if not (isDirPdf):
        print('Cartella pdf\\ creata')
        os.mkdir('pdf')

    if not (isDirTxt):
        print('Cartella txt\\ creata')
        os.mkdir('txt')

    if (isDirLib):
        files = os.listdir('lib')
        for i in range(len(files)):
            if not (files[i] == 'pdftotext.exe'):
                canExport = False
            else:
                canExport = True
    else:
        canExport = False

    files = os.listdir('txt\\')
    for i in range(len(files)):
        os.system('del txt\\' + files[i])

    return canExport


def converttotxt():
    """
        Converte tutti file PDF presenti all'interno della cartella pdf
        in file TXT
    """
    # Lista contenenti tutti i nomi dei file
    files = os.listdir('pdf')
    
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
            subprocess.Popen(pathExe + " -table pdf\\" + filesToConvert[i] + " txt\\" + name)
            time.sleep(1)
        except PermissionError:
            print("[-] Errore, un file non può essere convertito!")


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
    file = open('txt\\eni.txt', 'r')
    file_out = open('txt\\eni_out.txt', 'w')

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
    os.system('del txt\\eni.txt')


def delrowsunion():
    """
        Sistema il file union.txt con le righe in cui sono presenti i dati
        essenziali
    """
    file = open('txt\\union.txt', 'r')
    file_out = open('txt\\union_out.txt', 'w')

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
    os.system('del txt\\union.txt')


def delrowsesso():
    """
        Sistema il file esso.txt con le righe in cui sono presenti i dati
        essenziali
    """
    file = open('txt\\esso.txt', 'r')
    file_out = open('txt\\esso_out.txt', 'w')

    rows = []

    lines = file.readlines()

    for line in lines:
        if (line.__contains__('gasolio') or line.__contains__('E-DIESEL') or line.__contains__('scontrino')):
            rows.append(line)

    file_out.writelines(rows)
    file_out.close()
    file.close()
    os.system('del txt\\esso.txt')


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
    print('[>] Controllo file e directory in esecuzione')
    if (ctrlfiles()):
        print('[+] Controllo file e directory eseguito\n\n[>] Conversione pdf to txt in esecuzione')
        converttotxt()
        print('[+] Conversione pdf to txt eseguito')

        print("\n[>] Formattazione dei file in esecuzione")
        delrowseni()
        delrowsunion()
        delrowsesso()
        print("[+] Formattazione dei file completata")
    else:
        print("\n[-] Errore: Cartella lib non trovata!")
        exit(1)


if __name__ == "__main__":    
    start()