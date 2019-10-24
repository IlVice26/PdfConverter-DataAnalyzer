"""
    Raccoglie dati come targa, data, ora e costo della benzina dai file TXT
    Lavoro svolto per l'azienda Fornace S.R.L
"""

import os
import util.setupGui as setupGui
import xml.etree.ElementTree as ET


__version__ = '0.0.1'
__author__ = 'Vicentini Elia'

targheEni = {}
targheUnion = {}
targheEsso = {}
elemautostrade = {}
targheVWL = {}
targheARVAL = {}

targheDistributori = {}
targheLeasing = {}

boold = False


def datacollectunion():
    
    global targheUnion

    filesToCollect = []

    canCollect = False
    
    files = os.listdir(setupGui.PATHWIN32 + '\\txt\\')

    for file in files:
        if file.__contains__('union'):
            filesToCollect.append(file)
            canCollect = True


    if canCollect:
        for filet in filesToCollect:
            file = open(setupGui.PATHWIN32 + '\\txt\\' + filet, 'r', errors = 'ignore')

            lines = file.readlines()
            
            for line in lines:
                temp1 = line.split('    ')
                if not temp1[0] == '\n':
                    if temp1[0].__contains__('Targa: '):
                        temp2 = temp1[0].split(':')
                        temp3 = str(temp2[1].replace(' ', ''))[:7]

                        targa = str(temp3).replace(' ', '')
                        
                        infotarga = []
                        date = []
                        prezzi = 0

                        for i in range(1, len(lines)):
                            if (lines.index(line) + i) < len(lines):    
                                newrow = str(lines.__getitem__(lines.index(line) + i)).split(' ')
                                if not (newrow[0] == '' or newrow[0].__contains__('Targa:') or newrow[0] == '\n'):
                                    date.append(newrow[0][:6] + newrow[0][-2:])
                                    temp7 = newrow[-1].replace('\n', '')
                                    temp8 = temp7.replace(',', '.')
                                    prezzi += float(temp8)
                                else:
                                    if not (newrow[0] == '\n'):
                                        infotarga.append(date)
                                        infotarga.append(prezzi)
                                        infotarga.append('Union')
                                        targheUnion[targa] = infotarga
                                        
                                        keys = list(targheDistributori.keys())
                                        if targa in keys:
                                            targheDistributori[targa] += prezzi
                                        else:
                                            targheDistributori[targa] = prezzi

                                        break
                            else:
                                break
    else:
        pass


def datacollectesso():
    
    global targheEsso
    
    filesToCollect = []
    canCollect = False
    
    files = os.listdir(setupGui.PATHWIN32 + '\\txt\\')

    for file in files:
        if file.__contains__('esso'):
            filesToCollect.append(file)
            canCollect = True

    if canCollect:
        for filet in filesToCollect:
            file = open(setupGui.PATHWIN32 + '\\txt\\' + filet, 'r', errors = 'ignore')

            lines = file.readlines()
            targa = ""

            infotarga = []
            date = []
            prezzi = 0

            for line in lines:
                if (line.__contains__('gasolio') or line.__contains__('E-DIESEL')):
                    for i in range(1, len(lines)): 
                        if (lines.index(line) + i) < len(lines):    
                                newrow = str(lines.__getitem__(lines.index(line) + i)).split(' ')
                                if newrow[0] == '':
                                    dataLine = []
                                    for j in range(len(newrow)):
                                        if not newrow[j] == '':
                                            dataLine.append(newrow[j])
                                    temp1 = dataLine[1].split('-')
                                    if temp1[-1] != targa:
                                        
                                        if not (date == [] and prezzi == []):
                                            infotarga.append(date)
                                            infotarga.append(prezzi)
                                            infotarga.append('Esso')
                                            targheEsso[targa] = infotarga

                                            keys = list(targheDistributori.keys())
                                            if targa in keys:
                                                targheDistributori[targa] += prezzi
                                            else:
                                                targheDistributori[targa] = prezzi

                                        infotarga = []
                                        date = []
                                        prezzi = 0

                                        targa = temp1[-1]

                                        temp2 = line.split(' ')
                                        
                                        info = []
                                        for g in range(len(temp2)):
                                            if not temp2[g] == '':
                                                info.append(temp2[g])
                                        
                                        for g in range(len(info)):
                                            if info[g] == 'data':
                                                date.append(info[g + 1])

                                        temp3 = info[-1].replace(',', '.')
                                        prezzi += float(temp3.replace('\n', ''))

                                    else:
                                        
                                        temp2 = line.split(' ')
                                        
                                        info = []
                                        for g in range(len(temp2)):
                                            if not temp2[g] == '':
                                                info.append(temp2[g])

                                        for g in range(len(info)):
                                            if info[g] == 'data':
                                                date.append(info[g + 1])

                                        temp3 = info[-1].replace(',', '.')
                                        prezzi += float(temp3.replace('\n', ''))

                                else:
                                    break
    else:
        pass


def datacollecteni():
    
    global targheEni
    
    filesToCollect = []

    canCollect = False
    
    files = os.listdir(setupGui.PATHWIN32 + '\\txt\\')

    for file in files:
        if file.__contains__('eni'):
            filesToCollect.append(file)
            canCollect = True


    if canCollect:
        for filet in filesToCollect:
            file = open(setupGui.PATHWIN32 + '\\txt\\' + filet, 'r', errors = 'ignore')

            lines = file.readlines()

            try:
                for line in lines:
                    if not line == '\n':
                        if line.__contains__('Nr carta'):
                            targa = line[-8:].replace('\n', '')
                            infotarga = []
                            date = []
                            ore = []
                            prezzi = 0

                            for i in range(1, len(lines)):
                                newrow = str(lines.__getitem__(lines.index(line) + i)).split(' ')
                                if not (newrow[0] == 'Nr' or newrow[0] == 'Totale'):    
                                    if not (newrow[0] == '\n'):    
                                        
                                        # Tolgo tutti gli spazi e aggiungo i dati ad una lista
                                        dataLine = []
                                        for j in range(len(newrow)):
                                            if not (newrow[j] == ''):
                                                dataLine.append(newrow[j])
                                        
                                        # Aggiunta alla lista della date la data
                                        date.append(dataLine[0])
                                        
                                        # Controllo e aggiunta alla lista delle ore, l'ora
                                        if dataLine[1] == 'F':
                                            ore.append(dataLine[2].replace('F', ''))
                                        else:
                                            ore.append(dataLine[1].replace('F', ''))

                                        
                                        # Controllo e aggiunta alla lista dei prezzi il costo della benzina
                                        tempPrezzo = dataLine[10].split(',')
                                        if (len(tempPrezzo) == 2):    
                                            if (len(tempPrezzo[0]) >= 2):
                                                temp8 = dataLine[10].replace(',', '.')
                                                if len(temp8) > 6:
                                                    prezzi += float(temp8[-5:])
                                                else:
                                                    prezzi += float(temp8)
                                            else:
                                                temp8 = str(dataLine[11])[-6:]
                                                temp9 = temp8.replace(',', '.')
                                                if len(temp9) > 6:
                                                    prezzi += float(temp9[-5:])
                                                else:
                                                    prezzi += float(temp9)
                                        elif (len(tempPrezzo) == 3):
                                            temp8 = str(dataLine[10])[-6:]
                                            temp9 = temp8.replace(',', '.')
                                            prezzi += float(temp9)
                                        else:
                                            for j in range(len(dataLine)):
                                                if (dataLine[j] == 'SELF'):
                                                    prezzi += float(dataLine[j - 1].replace(',', '.'))
                                                    break

                                else:
                                    # Se la riga successiva si riferisce ad una targa nuova salvo i dati
                                    infotarga.append(date)
                                    infotarga.append(ore)
                                    infotarga.append(prezzi)
                                    infotarga.append('Eni')

                                    # Assegno i dati salvati alla targa
                                    targheEni[targa] = infotarga

                                    keys = list(targheDistributori.keys())
                                    if targa in keys:
                                        targheDistributori[targa] += prezzi
                                    else:
                                        targheDistributori[targa] = prezzi
                                    break
            except IndexError:
                pass                
    else:
        pass
       

def datacollectautostrade():
    
    global elemautostrade

    filesToCollect = []

    canCollect = False
    
    files = os.listdir(setupGui.PATHWIN32 + '\\txt\\')

    for file in files:
        if file.__contains__('autostrade'):
            filesToCollect.append(file)
            canCollect = True

    if canCollect:
        for filet in filesToCollect:
            file = open(setupGui.PATHWIN32 + '\\txt\\' + filet, 'r', errors = 'ignore')

            lines = file.readlines()

            for line in lines:
                if line.__contains__('TESSERA VIACARD') or line.__contains__('APPARATO TELEPASS'):
                    temp2 = line.split('    ')
                    tessera = temp2[-1].replace('\n', '')
                    if tessera.__contains__('.'):
                        tessera2 = tessera.replace('.', '')
                    else:
                        tessera2 = tessera

                    temp3 = lines[lines.index(line) + 1].split('    ')
                    totaleCosto = temp3[-1].replace('\n', '')
                    totaleCosto2 = totaleCosto.replace(',', '.')

                    elemautostrade[tessera2] = float(totaleCosto2.replace(' ', ''))
            file.close()
    else:
        pass

def parseVWL():
    """
    Esegue il parse su tutti i file xml che sono inseriti all'interno
    della directory
    """
    global targheVWL

    filesToCollect = []

    canCollect = False
    
    files = os.listdir(setupGui.PATHWIN32 + '\\txt\\')

    for file in files:
        if file.__contains__('vwl') and file.__contains__('.xml'):
            filesToCollect.append(file)
            canCollect = True

    if canCollect:
        for filet in filesToCollect:    
            tree = ET.parse(setupGui.PATHWIN32 + '\\txt\\' + filet)
            root = tree.getroot()

            for i in range(0, len(root[1][1]) - 1, 2):   
                targa = root[1][1][i][8][1].text
                tot1 = float(root[1][1][i][6].text)
                tot2 = float(root[1][1][i+1][6].text)
                targheVWL[targa] = tot1 + tot2

                keys = list(targheLeasing.keys())
                if targa in keys:
                    targheLeasing[targa] += tot1 + tot2
                else:
                    targheLeasing[targa] = tot1 + tot2
    else:
        pass



def parseARVAL():
    """
    Esegue il parse su tutti i file xml che sono inseriti all'interno
    della directory
    """
    global targheARVAL

    filesToCollect = []

    canCollect = False
    
    files = os.listdir(setupGui.PATHWIN32 + '\\txt\\')

    for file in files:
        if file.__contains__('arval') and file.__contains__('.xml'):
            filesToCollect.append(file)
            canCollect = True

    if canCollect:
        for filet in filesToCollect:    
            tree = ET.parse(setupGui.PATHWIN32 + '\\txt\\' + filet)
            root = tree.getroot()

            for i in range(0, len(root[1][1]) - 1, 2):   
                targa = root[1][1][i][8][1].text
                print(targa)
                tot1 = float(root[1][1][i][5].text)
                tot2 = float(root[1][1][i+1][5].text)
                targheARVAL[targa] = tot1 + tot2

                keys = list(targheLeasing.keys())
                if targa in keys:
                    targheLeasing[targa] += tot1 + tot2
                else:
                    targheLeasing[targa] = tot1 + tot2
    else:
        pass     


def viewDict(targhe):
    """
        Visualizza tutto il dizionario contenente le targhe
    """
    # Lista contenente tutte le targhe
    keys = list(targhe.keys())
    
    # Stampa tutte le informazioni delle targhe
    for i in range(len(targhe)):
        print(keys[i])
        print(targhe[keys[i]])


def exportRows():
    file = open('rawFile.txt', 'w')
    file.write('-- Targhe Eni --\n')
    keys = list(targheEni.keys())
    for i in range(len(targheEni)):
        file.write(keys[i])
        file.write(str(targheEni[keys[i]]))
    file.write('-- Targhe Esso --\n')
    keys = list(targheEsso.keys())
    for i in range(len(targheEsso)):
        file.write(keys[i])
        file.write(str(targheEsso[keys[i]]))
    file.write('-- Targhe Union --\n')
    keys = list(targheUnion.keys())
    for i in range(len(targheUnion)):
        file.write(keys[i])
        file.write(str(targheUnion[keys[i]]))
    file.write('-- Tessere Autostrade --\n')
    keys = list(elemautostrade.keys())
    for i in range(len(elemautostrade)):
        file.write(keys[i])
        file.write(str(elemautostrade[keys[i]]))
    file.write('-- Targhe VWL --\n')
    keys = list(targheVWL.keys())
    for i in range(len(targheVWL)):
        file.write(keys[i])
        file.write(str(targheVWL[keys[i]]))
    file.write('-- Targhe Arval --\n')
    keys = list(targheARVAL.keys())
    for i in range(len(targheARVAL)):
        file.write(keys[i])
        file.write(str(targheARVAL[keys[i]]))
    file.close()

def start():
    datacollecteni()
    datacollectunion()
    datacollectesso()
    datacollectautostrade()
    parseVWL()
    parseARVAL()


if __name__ == "__main__":
    start()