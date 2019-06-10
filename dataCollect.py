"""
    Raccoglie dati come targa, data, ora e costo della benzina dai file TXT
    Lavoro svolto per l'azienda Fornace S.R.L
"""

__version__ = '0.0.1'
__author__ = 'Vicentini Elia'

targheEni = {}
targheUnion = {}
targheEsso = {}

boold = False


def datacollectunion():
    
    global targheUnion
    
    file = open('txt\\union_out.txt', 'r')

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
                prezzi = []

                for i in range(1, len(lines)):
                    if (lines.index(line) + i) < len(lines):    
                        newrow = str(lines.__getitem__(lines.index(line) + i)).split(' ')
                        if not (newrow[0] == '' or newrow[0].__contains__('Targa:') or newrow[0] == '\n'):
                            date.append(newrow[0][:6] + newrow[0][-2:])
                            prezzi.append(newrow[-1].replace('\n', ''))
                        else:
                            if not (newrow[0] == '\n'):
                                infotarga.append(date)
                                infotarga.append(prezzi)
                                infotarga.append('Union')
                                targheUnion[targa] = infotarga
                                break
                    else:
                        break


def datacollectesso():
    
    global targheEsso

    file = open('txt\\esso_out.txt')

    lines = file.readlines()
    targa = ""

    infotarga = []
    date = []
    prezzi = []

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

                                infotarga = []
                                date = []
                                prezzi = []

                                targa = temp1[-1]

                                temp2 = line.split(' ')
                                
                                info = []
                                for g in range(len(temp2)):
                                    if not temp2[g] == '':
                                        info.append(temp2[g])
                                
                                for g in range(len(info)):
                                    if info[g] == 'data':
                                        date.append(info[g + 1])

                                temp3 = info[-1].replace('.', ',')
                                prezzi.append(temp3.replace('\n', ''))

                            else:
                                
                                temp2 = line.split(' ')
                                
                                info = []
                                for g in range(len(temp2)):
                                    if not temp2[g] == '':
                                        info.append(temp2[g])

                                for g in range(len(info)):
                                    if info[g] == 'data':
                                        date.append(info[g + 1])

                                temp3 = info[-1].replace('.', ',')
                                prezzi.append(temp3.replace('\n', ''))

                        else:
                            break


def datacollecteni():
    
    global targheEni
    
    file = open('txt\\eni_out.txt', 'r')

    lines = file.readlines()

    try:
        for line in lines:
            if not line == '\n':
                if line.__contains__('Nr carta'):
                    targa = line[-8:].replace('\n', '')
                    
                    infotarga = []
                    date = []
                    ore = []
                    prezzi = []

                    for i in range(1, len(lines)):
                        newrow = str(lines.__getitem__(lines.index(line) + i)).split(' ')
                        if not (newrow[0] == 'Nr' or newrow[0] == 'Totale'):    
                            if not (newrow[0] == '\n'): 
                                dataLine = []
                                for j in range(len(newrow)):
                                    if not (newrow[j] == ''):
                                        dataLine.append(newrow[j])
                                date.append(dataLine[0])
                                if dataLine[1] == 'F':
                                    ore.append(dataLine[2].replace('F', ''))
                                else:
                                    ore.append(dataLine[1].replace('F', ''))
                                tempPrezzo = dataLine[10].split(',')
                                if (len(tempPrezzo) == 2):    
                                    if (len(tempPrezzo[0]) >= 2):
                                        prezzi.append(dataLine[10])
                                    else:
                                        prezzi.append(str(dataLine[11])[-6:])
                                elif (len(tempPrezzo) == 3):
                                    prezzi.append(str(dataLine[10])[-6:])
                                else:
                                    for j in range(len(dataLine)):
                                        if (dataLine[j] == 'SELF'):
                                            prezzi.append(dataLine[j - 1])
                                            break
                        else:
                            infotarga.append(date)
                            infotarga.append(ore)
                            infotarga.append(prezzi)
                            infotarga.append('Eni')
                            targheEni[targa] = infotarga
                            break
    except IndexError:
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


def start():
    print("[>] Elaborazione dati in esecuzione")
    datacollecteni()
    print('-> Data Eni completato')
    datacollectunion()
    print('-> Data Union completato')
    datacollectesso()
    print('-> Data Esso completato')
    print("[+] Elaborazione dati compleatata")
    
    if boold:    
        print('\n -- Targhe ENI --  \n')
        viewDict(targheEni)
        print('\n -- Targhe UNION --  \n')
        viewDict(targheUnion)
        print('\n -- Targhe ESSO --  \n')
        viewDict(targheEsso)

if __name__ == "__main__":
    start()