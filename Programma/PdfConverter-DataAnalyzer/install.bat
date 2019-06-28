@echo off
REM Questo è un installer delle librerie necessarie per il corretto funzionamento del programma pdfConverterGui.pyw

ECHO Installazione delle librerie Python
pip install --upgrade pip
pip install PyQt5
pip install openpyxl

ECHO Installazione completata!
PAUSE