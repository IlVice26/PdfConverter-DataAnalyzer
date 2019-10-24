# -*- coding: utf-8 -*-
"""
    Gui Setup.py
"""

import getpass
import sys
import os
from lib.Wget import wget


# Variabili globali 
USERNAME = getpass.getuser()

PATHDOCUMENTSWIN32 = 'C:\\Users\\' + USERNAME + '\\Documents'
PATHWIN32 = PATHDOCUMENTSWIN32 + '\\PdfConverter-DataAnalyzer'
PATHSWIN = ['\\pdf','\\txt', '\\output', '\\database']


def main():
    checkFirstInstallation()

def checkFirstInstallation():

    dirPCDA = False 
    dirOut = False
    dirPdf = False
    dirTxt = False
    dirDb = False

    files = os.listdir(PATHDOCUMENTSWIN32)

    for file in files:
        if file == 'PdfConverter-DataAnalyzer':
            dirPCDA = True
            break

    if dirPCDA:
        files = os.listdir(PATHWIN32)
        
        for file in files:
            if file == 'pdf':
                dirPdf = True
            if file == 'txt':
                dirTxt = True
            if file == 'output':
                dirOut = True
            if file == 'database':
                dirDb = True
        
        if dirPdf is True and dirTxt is True and dirOut is True and dirDb is True:
            checkDir = True
        else:
            if not dirPdf:
                os.mkdir(PATHWIN32 + '\\pdf')
            if not dirTxt:
                os.mkdir(PATHWIN32 + '\\txt')
            if not dirOut:
                os.mkdir(PATHWIN32 + '\\output')
            if not dirDb:
                os.mkdir(PATHWIN32 + '\\database')

    else:
        os.mkdir(PATHWIN32)
        for p in PATHSWIN:
            os.mkdir(PATHWIN32 + p)

main()
