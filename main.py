#        VAJA PARANDADA
###################################
# OSAD KURSUSED EI OLE KÕIGILE KLASSILE
# EELMINE AASTA ON VÕETUD EELDUSAINE
# VAJA LISADA PRAKTIKUMID/TUNNIVÄLISED
# VAJA LUUA ÕPILASTELE OUTPUT FILE  -  TEHTUD, KUID VIGANE (ÕPILASE JÄREL ON MINGI MUU ÕPILASE KURSUSED(ÕPILASED ON NUMBRI JÄRJEKORRAS, KUID KURSUSED ON SUVALISES JÄRJEKORRAS))
# VAJA LUUA ÕPETAJATELE OUTPUT FILE  -  TEHTUD
# LISADA KOMMENTAARE
# LUUA DOKUMENT
# LOGI FAILI LOOMINE - TEHTUD
###################################

import random
from csv import reader
from collections import OrderedDict
import copy
from openpyxl import Workbook

#{'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1', '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}}

def grupeerimine():
    klass10 = {}
    klass11 = {}
    klass12 = {}
    formating = []
    õpilaseNimed = []
    temp1 = {}
    korda = 0
    with open('testinput4.csv', 'r', encoding="utf-8") as input_file: ############### MUUDAB FAILI NIME
        csv_reader = reader(input_file)
        for row in csv_reader:
            #print(row)
            if korda == 0:
                formating = row
                for i in range(len(formating)):
                    formating[i] = formating[i].replace('"', "")
                korda += 1
            else:
                for i in range(len(row)):
                    row[i] = row[i].replace('"', "")
                    row[i] = row[i].replace('Ãµ', "õ")
                    row[i] = row[i].replace('Ã¤', "ä")
                    row[i] = row[i].replace('Ã¶', "ö")
                    row[i] = row[i].replace('Ã¼', "ü")
                
                #### Paneb õige klassi sõnastikku
                õpilaseNimed.append(row[2])
                if row[3] == '12':
                    for i in range(len(formating)):
                        temp1[formating[i]] = row[i]
                    klass12[row[2]] = temp1
                elif row[3] == '11':
                    for i in range(len(formating)):
                        temp1[formating[i]] = row[i]
                    klass11[row[2]] = temp1
                elif row[3] == '10':
                    for i in range(len(formating)):
                        temp1[formating[i]] = row[i]
                    klass10[row[2]] = temp1
                else:
                    print("TEKKIS VIGA ÕPILASE ÕIGESSE SÕNASTIKKU PANEMISEL")
                temp1 = {}
    return klass10, klass11, klass12, õpilaseNimed

klass10, klass11, klass12, õpilaseNimed = grupeerimine()
#print(klass11)
ained = {}
def ained_seadistamine():
    ainedList = []
    ained = {}
    with open('ained.txt', 'r', encoding="utf-8") as ainedfail:
        for i in ainedfail: #### {Python 2 : {"kohad" : 40, "eeldusaine" = "Python 1", "lisad" : ""}}
            temp1 = {}
            ainedList = i.replace("\n", "").split(";")
            #ained[ainedList[0]]["kohad"] = ainedList[1]
            #ained[ainedList[0]]["kohad"] = 40
            temp1["alternatiiv"] = ainedList[1]
            temp1["kohad"] = ainedList[2]
            temp1["periood"] = ainedList[3]
            temp1["kohtiVõetud"] = 0
            temp1["eeldusaine"] = ainedList[4]
            temp1["üksEeldusaine"] = ainedList[5]
            temp1["lisad"] = ainedList[6]
            temp1["vastuVõetud"] = []
            temp1["järjekord"] = []
            ained[ainedList[0]] = temp1
            #print(ained)
        #print(ained)
        return ained


klass10_seadistatud, klass11_seadistatud, klass12_seadistatud = {}, {}, {}


#### 12.klassi 1. valik kirja 

def seadistamine(õpilaseNimi, õpilaneDict):
    õpilaseKursused = [] #### [[P1H väga, P1H võtaks, P1H vähe], [P1Õ väga, P1õ võtaks, P1Õ vähe]]
    ajutine = []
    korda1 = 0
    #print(õpilaseNimi)
    for i in range(4, len(list(õpilaneDict))): ######################### KUI TULEB EMAIL KONTROLL VB PEAB LISAMA -1 len() LÕPPU
        if korda1 % 3 == 0 and korda1 != 0:
            õpilaseKursused.append(ajutine)
            ajutine = []
        korda1 += 1
        ajutine.append(list(õpilaneDict.values())[i])
    õpilaseKursused.append(ajutine)
    #print(õpilaseKursused)
    return õpilaseKursused


for i in range(0, len(klass12)):
    õpilaseNimi, õpilaseDict = random.choice(list(klass12.items()))
    del klass12[õpilaseNimi]
    klass12_seadistatud[õpilaseNimi] = seadistamine(õpilaseNimi, õpilaseDict)

#print(klass12_seadistatud)

for i in range(0, len(klass11)):
    õpilaseNimi, õpilaseDict = random.choice(list(klass11.items()))
    del klass11[õpilaseNimi]
    klass11_seadistatud[õpilaseNimi] = seadistamine(õpilaseNimi, õpilaseDict)

for i in range(0, len(klass10)):
    õpilaseNimi, õpilaseDict = random.choice(list(klass10.items()))
    del klass10[õpilaseNimi]
    klass10_seadistatud[õpilaseNimi] = seadistamine(õpilaseNimi, õpilaseDict)

klass10_PERM, klass11_PERM, klass12_PERM = copy.deepcopy(klass10_seadistatud), copy.deepcopy(klass11_seadistatud), copy.deepcopy(klass12_seadistatud)
ained = ained_seadistamine()
#print(ained)

resultList = {} ####{Marcus : ['Planimeetria alused', '3D-modelleerimine']}
result = {} ####{Marcus : {1 : 'Planimeetria alused', 2 : '', 3 : '3D-modelleerimine'}}
tempSõnastik = {}

def võrdlemine(a, b):
    for i in a:
        if i in b:
            return True
    return False

#### [['Planimeetria alused', 'Globaliseeruv maailm', 'Ei taha'], ['Programmeerimine keeles Python 1', 'Programmeerimine keeles Python 1', 'Programmeerimine keeles Python 1'], ['3D-modelleerimine', 'Küberkaitse 1', '3D-modelleerimine'], ['Statistiline maailmapilt', 'Ei taha', 'Ei taha'], ['Loomade käitumine', 'Ei taha', 'Ei taha'], ['Majandusõpe', 'Millest ELU koosneb?', 'Majandusõpe'], ['Ettevõtlusõpe', 'Liiklusfüüsika', 'Liiklusfüüsika'], ['CAD joonestamine', 'Ei taha', 'Ei taha']]
with open("log.txt", "w") as file:
    file.write("")
    def registreerimine(klass_seadistatud, valik, result):
        for i in range(0, len(klass_seadistatud)):
            temp2 = []
            tempSõnastik = {}
            klass_seadistatud_temp = klass_seadistatud
            õpilaseNimi, õpilaseKursused = random.choice(list(klass_seadistatud_temp.items()))
            del klass_seadistatud_temp[õpilaseNimi]
            if õpilaseNimi not in result:
                tempSõnastik = {k: '' for k in range(1, len(õpilaseKursused)+2)}
                result[õpilaseNimi] = tempSõnastik
            for i in range(0, len(õpilaseKursused)):
                #print(õpilaseKursused)
                hetkeneKursus = õpilaseKursused[i][valik]
                temp2 = resultList.get(õpilaseNimi, [])
                resultList[õpilaseNimi] = temp2
                if hetkeneKursus == "Ei taha": ### EI TEA KAS TÖÖTAB
                    print(õpilaseNimi + " ei tahtnud see periood midagi")
                elif ained[hetkeneKursus]['kohtiVõetud'] <  int(ained[hetkeneKursus]['kohad']):  # 1. kui mahub 2. ei ole juba sellel kursusel 3. ei ole see periood veel midagi võetud 4. eeldusained on võetud (eelmine periood või eelmine aasta) 5. üks sama eeldusaine on võetud
                    if hetkeneKursus not in resultList[õpilaseNimi]: #### õpilasel on see kursus juba võetud
                        if ained[hetkeneKursus]['alternatiiv'] not in resultList[õpilaseNimi]: #### õpilasel on selle kursuse alternatiiv võetud
                            if result[õpilaseNimi][int(ained[hetkeneKursus]['periood'])] == '': #### õpilasel on sellel perioodil midagi juba võetud
                                #### TULEB LISADA EELMISE AASTA EELDUSAINED JUURDE
                                if ained[hetkeneKursus]['eeldusaine'] == '' or all(elem in resultList[õpilaseNimi] for elem in ained[hetkeneKursus]['eeldusaine'].split(",")): ##### kontrollib kas õpilane on see aasta võtnud eeldusained
                                    if ained[hetkeneKursus]['üksEeldusaine'] == '' or võrdlemine(ained[hetkeneKursus]['üksEeldusaine'].split(","), resultList[õpilaseNimi]):
                                        print(õpilaseNimi + " vastu võetud " + hetkeneKursus)
                                        file.write(õpilaseNimi + " vastu võetud " + hetkeneKursus + "\n")
                                        ained[hetkeneKursus]['kohtiVõetud'] += 1
                                        ained[hetkeneKursus]['vastuVõetud'].append(õpilaseNimi)
                                        ########
                                        temp2 = resultList.get(õpilaseNimi, [])
                                        temp2.append(hetkeneKursus)
                                        resultList[õpilaseNimi] = temp2
                                        #print(resultList)
                                        ########
                                        tempSõnastik = result[õpilaseNimi]
                                        tempSõnastik[i+1] = hetkeneKursus
                                        result[õpilaseNimi] = tempSõnastik
                                        #print(result)
                                        ########
                                        if ained[hetkeneKursus]['lisad'] != '':
                                            for j in range(0, len(ained[hetkeneKursus]['lisad'].split(","))):
                                                print(õpilaseNimi + " vastu võetud " + ained[hetkeneKursus]['lisad'].split(",")[j])
                                                file.write(õpilaseNimi + " vastu võetud " + ained[hetkeneKursus]['lisad'].split(",")[j] + "\n")
                                                ained[ained[hetkeneKursus]['lisad'].split(",")[j]]['vastuVõetud'].append(õpilaseNimi) ## Kui õigesti mäletan siis see rida lisab kursuse "vastuVõetud" listi õpilase nime juurde
                                                #####
                                                temp2 = resultList.get(õpilaseNimi, [])
                                                temp2.append(ained[hetkeneKursus]['lisad'].split(",")[j])
                                                resultList[õpilaseNimi] = temp2
                                                #print(resultList)
                                                #####
                                                tempSõnastik[int(ained[ained[hetkeneKursus]['lisad'].split(",")[j]]['periood'])] = ained[hetkeneKursus]['lisad'].split(",")[j]
                                                result[õpilaseNimi] = tempSõnastik
                                                #print(result)
                                                #####
                                else:
                                    print(õpilaseNimi + " ei saanud " + hetkeneKursus + ", sest ei ole võtnud eeldusainet " + ained[hetkeneKursus]['eeldusaine'])
                                    file.write(õpilaseNimi + " ei saanud " + hetkeneKursus + ", sest ei ole võtnud eeldusainet " + ained[hetkeneKursus]['eeldusaine'] + "\n")
                            else:
                                print(õpilaseNimi + " ei saanud kursusele " + hetkeneKursus + ", sest on juba sellel perioodil muule kursusele sisse saanud")
                                file.write(õpilaseNimi + " ei saanud kursusele " + hetkeneKursus + ", sest on juba sellel perioodil muule kursusele sisse saanud" + "\n")
                        else:
                            print(õpilaseNimi + " on juba " + hetkeneKursus + " kursuse alternatiivile sisse eelneval hetkel")
                            file.write(õpilaseNimi + " on juba " + hetkeneKursus + " kursuse alternatiivile sisse eelneval hetkel" + "\n")
                    else:
                        print(õpilaseNimi + " on juba " + hetkeneKursus + " kursusele sisse saanud eelneval hetkel")
                        file.write(õpilaseNimi + " on juba " + hetkeneKursus + " kursusele sisse saanud eelneval hetkel" + "\n")
                else:
                    print(õpilaseNimi + " ei saanud kursusele " + hetkeneKursus + ", sest see oli juba täis")
                    file.write(õpilaseNimi + " ei saanud kursusele " + hetkeneKursus + ", sest see oli juba täis" + "\n")
                    if len(ained[hetkeneKursus]["järjekord"]) < 10:
                        ained[hetkeneKursus]["järjekord"].append(õpilaseNimi)
                        print(õpilaseNimi + " lisati " + hetkeneKursus + " järjekorda") ################ LISADA KÕIK hetkeneKursus "" VAHELE ET OLEKS ILUSAM
                        file.write(õpilaseNimi + " lisati " + hetkeneKursus + " järjekorda" + "\n")

        #print(result)
        return result
    #### 12. klassi 1. valik valimine
    klass12_segamini = {}
    for i in range(0, len(klass12_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass12_seadistatud))
        kursused = klass12_seadistatud[õpilaseNimi]
        del klass12_seadistatud[õpilaseNimi]
        klass12_segamini[õpilaseNimi] = kursused
    result = registreerimine(klass12_segamini, 0,result)
    print("LÕPPETATUD 12. KLASSI 1. VALIK")
    #### 11. ja 10. klassi 1. valik
    klass12_seadistatud = copy.deepcopy(klass12_PERM)
    kokku11ja10 = {} #### PANEB KÕIK 11 JA 10 KLASSI ÕPILASED SÕNASTIKKU SISSE JA HAKKAB REGISTREERIMA SUVALISES JÄRJEKORRAS
    kokku11ja10_segamini = {}

    for i in range(0, len(klass11_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass11_seadistatud))
        kursused = klass11_seadistatud[õpilaseNimi]
        del klass11_seadistatud[õpilaseNimi]
        kokku11ja10[õpilaseNimi] = kursused
    for i in range(0, len(klass10_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass10_seadistatud))
        kursused = klass10_seadistatud[õpilaseNimi]
        del klass10_seadistatud[õpilaseNimi]
        kokku11ja10[õpilaseNimi] = kursused

    for i in range(0, len(kokku11ja10.keys())):
        õpilaseNimi = random.choice(list(kokku11ja10))
        kursused = kokku11ja10[õpilaseNimi]
        del kokku11ja10[õpilaseNimi]
        kokku11ja10_segamini[õpilaseNimi] = kursused
    result = registreerimine(kokku11ja10_segamini, 0,result)
    print("LÕPPETATUD 11. JA 10. KLASSI 1. VALIK")
    #### 12., 11. ja 10. klassi 2. valik
    klass12_seadistatud = copy.deepcopy(klass12_PERM)
    klass11_seadistatud = copy.deepcopy(klass11_PERM)
    klass10_seadistatud = copy.deepcopy(klass10_PERM)
    kokku12ja11ja10 = {}
    kokku12ja11ja10_segamini = {}

    for i in range(0, len(klass12_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass12_seadistatud))
        kursused = klass12_seadistatud[õpilaseNimi]
        del klass12_seadistatud[õpilaseNimi]
        kokku12ja11ja10[õpilaseNimi] = kursused
    for i in range(0, len(klass11_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass11_seadistatud))
        kursused = klass11_seadistatud[õpilaseNimi]
        del klass11_seadistatud[õpilaseNimi]
        kokku12ja11ja10[õpilaseNimi] = kursused
    for i in range(0, len(klass10_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass10_seadistatud))
        kursused = klass10_seadistatud[õpilaseNimi]
        del klass10_seadistatud[õpilaseNimi]
        kokku12ja11ja10[õpilaseNimi] = kursused
        
    for i in range(0, len(kokku12ja11ja10.keys())):
        õpilaseNimi = random.choice(list(kokku12ja11ja10))
        kursused = kokku12ja11ja10[õpilaseNimi]
        del kokku12ja11ja10[õpilaseNimi]
        kokku12ja11ja10_segamini[õpilaseNimi] = kursused

    result = registreerimine(kokku12ja11ja10_segamini, 1,result)
    #print(kokku12ja11ja10_segamini)
    print("LÕPPETATUD 12., 11. ja 10. KLASSI 2. VALIK")
    #### 12., 11. ja 10. klassi 3. valik
    klass12_seadistatud = copy.deepcopy(klass12_PERM)
    klass11_seadistatud = copy.deepcopy(klass11_PERM)
    klass10_seadistatud = copy.deepcopy(klass10_PERM)

    kokku12ja11ja10 = {}
    kokku12ja11ja10_segamini = {}
    for i in range(0, len(klass12_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass12_seadistatud))
        kursused = klass12_seadistatud[õpilaseNimi]
        del klass12_seadistatud[õpilaseNimi]
        kokku12ja11ja10[õpilaseNimi] = kursused
    for i in range(0, len(klass11_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass11_seadistatud))
        kursused = klass11_seadistatud[õpilaseNimi]
        del klass11_seadistatud[õpilaseNimi]
        kokku12ja11ja10[õpilaseNimi] = kursused
    for i in range(0, len(klass10_seadistatud.keys())):
        õpilaseNimi = random.choice(list(klass10_seadistatud))
        kursused = klass10_seadistatud[õpilaseNimi]
        del klass10_seadistatud[õpilaseNimi]
        kokku12ja11ja10[õpilaseNimi] = kursused
        
    for i in range(0, len(kokku12ja11ja10.keys())):
        õpilaseNimi = random.choice(list(kokku12ja11ja10))
        kursused = kokku12ja11ja10[õpilaseNimi]
        del kokku12ja11ja10[õpilaseNimi]
        kokku12ja11ja10_segamini[õpilaseNimi] = kursused
        
    result = registreerimine(kokku12ja11ja10_segamini, 2,result)
    #print(kokku12ja11ja10_segamini)
    print("LÕPPETATUD 12., 11. ja 10. KLASSI 3. VALIK")

    print(result)
    print("-------------------------")
    #################################### ÕPETAJA FAILI KIRJUTAMINE
    kursusedFailiJaoks = []
    õpilasteNimedFailiJaoks = []
    järjekordFailiJaoks = []
    aed = ained.keys()
    for i in range(0, len(aed)):
        kursusedFailiJaoks.append(list(aed)[i])
        õpilasteNimedFailiJaoks.append(ained[list(aed)[i]]["vastuVõetud"])
        järjekordFailiJaoks.append(ained[list(aed)[i]]["järjekord"])

    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Kursus"
    sheet["E1"] = "Õpilased"
    sheet["O1"] = "Järjekord"
    seperator = ", "
    for i in range(0, len(kursusedFailiJaoks)):
        sheet.cell(row=i+2, column=1).value = kursusedFailiJaoks[i]
        sheet.cell(row=i+2, column=5).value = seperator.join(õpilasteNimedFailiJaoks[i])
        sheet.cell(row=i+2, column=15).value = seperator.join(järjekordFailiJaoks[i]) ########## LISADA ÕPILASTE JÄRJEKORD
    workbook.save(filename="õpetajateFail.xlsx")
    print("-------------------------")
    #################################### ÕPILASTE FAILI KIRJUTAMINE

    igaÕpilaseKursused = []
    #õpilaseNimed = []
    aed = result.keys() 
    for i in range(0, len(aed)):
        #igaÕpilaseKursused.append(result[list(aed)[i]])
        hetkesedKursused = []
        for j in range(1, int(list(result[list(aed)[0]].keys())[-1])):
            if result[list(aed)[i]].get(int(j)) == "":
                hetkesedKursused.append(" --- ")
            else:
                hetkesedKursused.append(result[list(aed)[i]].get(int(j)))
        igaÕpilaseKursused.append(hetkesedKursused)


    workbook = Workbook()
    sheet = workbook.active
    sheet["A1"] = "Õpilane"
    sheet["B1"] = "2. periood hommik"
    sheet["C1"] = "2. periood õhtu"
    sheet["D1"] = "3. periood hommik"
    sheet["E1"] = "3. periood õhtu"
    sheet["F1"] = "4. periood hommik"
    sheet["G1"] = "4. periood õhtu"
    sheet["H1"] = "5. periood hommik"
    sheet["I1"] = "5. periood õhtu"

    seperator = ", "
    for i in range(0, len(igaÕpilaseKursused)):
        '''
        print(i)
        print(õpilaseNimed[i])
        print(igaÕpilaseKursused[i])
        sheet.cell(row=i+2, column=1).value = õpilaseNimed[i]
        sheet.cell(row=i+2, column=4).value = seperator.join(igaÕpilaseKursused[i])
        '''
        sheet["A" + str(i+2)] = õpilaseNimed[i]
        sheet["B" + str(i+2)] = igaÕpilaseKursused[i][0]
        sheet["C" + str(i+2)] = igaÕpilaseKursused[i][1]
        sheet["D" + str(i+2)] = igaÕpilaseKursused[i][2]
        sheet["E" + str(i+2)] = igaÕpilaseKursused[i][3]
        sheet["F" + str(i+2)] = igaÕpilaseKursused[i][4]
        sheet["G" + str(i+2)] = igaÕpilaseKursused[i][5]
        sheet["H" + str(i+2)] = igaÕpilaseKursused[i][6]
        sheet["I" + str(i+2)] = igaÕpilaseKursused[i][7]
    workbook.save(filename="õpilasteFail.xlsx")

    print("LÕPETATUD EDUKALT")