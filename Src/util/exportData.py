"""
    Attraverso le librerie:
    - pdfConverter.py
    - dataCollect.py
    Salva tutti i dati raccolti all'interno di un file Excel (.xlsx)
    Lavoro svolto per l'azienda Fornace S.R.L
"""

__version__ = '0.0.1'
__author__ = 'Vicentini Elia'

import util.pdfConverter as pdfConverter
import util.dataCollect as dataCollect
import openpyxl
import time, datetime
import util.setupGui as setupGui


targhe1 = dataCollect.targheEni
targhe2 = dataCollect.targheUnion
targhe3 = dataCollect.targheEsso
targhe4 = dataCollect.targheVWL
targhe5 = dataCollect.targheARVAL
tessere = dataCollect.elemautostrade


def exporttofile():
    
    pass
    

def main():
    pdfConverter.start()
    dataCollect.start()
    exporttofile()


if __name__ == "__main__":
    main()