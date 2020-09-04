import random
from csv import reader
from collections import OrderedDict
import copy
from openpyxl import Workbook

class kõikÕpilased:
    klass10 = []
    klass11 = []
    klass12 = []
    
    def __init__(self, nimi, klass):
        self.nimi = nimi
        self.klass = klass
        if self.klass == 10:
            kõikÕpilased.klass10.append(self.nimi)
        if self.klass == 11:
            kõikÕpilased.klass11.append(self.nimi)
        if self.klass == 12:
            kõikÕpilased.klass12.append(self.nimi)

    def printklass10():
        print(kõikÕpilased.klass10)
    def printklass11():
        print(kõikÕpilased.klass11)
    def printklass12():
        print(kõikÕpilased.klass12)


class Õpilane:
    def __init__(self, nimi, klass, ained):
        self.nimi = nimi
        self.klass = klass
        self.ained = ained

        #print(ained)
        

class Kursus:
    kursused = []

    def __init__(self, nimi, periood, kohad, vabadKohad, alternatiivid, eeldusaine, üksEeldusaine, lisad, vastuVõetud, järjekord):
        self.nimi = nimi
        self.periood = periood
        self.kohad = kohad
        self.vabadKohad = vabadKohad 
        self.alternatiivid = alternatiivid
        self.eeldusaine = eeldusaine
        self.üksEeldusaine = üksEeldusaine
        self.lisad = lisad
        self.vastuVõetud = vastuVõetud
        self.järjekord = järjekord
        Kursus.kursused.append(self.nimi)
    def printKursused():
        print(Kursus.kursused)

'''
õpilased = {"Sten" : 10, "Marcus" : 11, "Kristo" : 10, "Oja" : 12, "Mair" : 10}

for i in õpilased.keys():
    i = kõikÕpilased(i, õpilased[i])

kõikÕpilased.printklass10()
'''
korda = 0
formating = []
with open('testinput1.csv', 'r', encoding="utf-8") as input_file: # Õpilaste kursuste faili avamine
        csv_reader = reader(input_file)
        for row in csv_reader:
            if korda == 0:
                formating = row
                for i in range(len(formating)):
                    formating[i] = formating[i].replace('"', "")
                korda += 1
            else:
                for i in range(len(row)):
                    row[i] = row[i].replace('"', "") # Encodingu parandus
                    row[i] = row[i].replace('Ãµ', "õ")
                    row[i] = row[i].replace('Ã¤', "ä")
                    row[i] = row[i].replace('Ã¶', "ö")
                    row[i] = row[i].replace('Ã¼', "ü")
                
                #### Paneb õige klassi sõnastikku
                nimi = row[2]
                nimi = Õpilane(row[2], int(row[3]), row[4:])
                nimi = kõikÕpilased(row[2], int(row[3]))

kõikÕpilased.printklass11()

with open('ained.txt', 'r', encoding="utf-8") as ainedfail:
    for i in ainedfail: #### {Python 2 : {"kohad" : 40, "eeldusaine" = "Python 1", "lisad" : ""}}
        ainedList = i.replace("\n", "").split(";")
        nimi = ainedList[0]
        nimi = Kursus(ainedList[0], ainedList[3], ainedList[2], 0, ainedList[1], ainedList[4], ainedList[5], ainedList[6], [], [])


Kursus.printKursused()
#print(Kursus.kursused[3].periood)
'''
#õpilased = ["Sten", "Marcus", "Kristo Oja"]
                    #       (Sten) 1H         1Õ jne                                            (Marcus) 1H               1Õ
õpilase_kursused = [[["Inka", "Vene", "Test"],["Hommik", "Küberkaitse", "Loom"]], [["asdasdasd", "Vene", "Test"],["123123123k", "Küberkaitse", "Loom"]], [["ginvi", "Vene", "Test"],["H123123ik", "Küberkaitse", "Loom"]]]
for i in range(0, len(õpilased)): 
    õpilased[i] = Õpilane(õpilased[i], 11, õpilase_kursused[i][0], õpilase_kursused[i][1])
    print(õpilased[i].periood1õhtu)
    print(õpilased[i].kool)
'''