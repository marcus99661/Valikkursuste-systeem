import random
from csv import reader
from collections import OrderedDict
#        VAJA PARANDADA
###################################
# PANEB ARVATAVASTI KOKKU KUI ON MITU EELDUSAINET
#
#
###################################

#### {Nimi,klass : [[P1Hväga, P1Hvõtaks, P1Hvähe], [P1Õväga, P1Õvõtaks, P1Õvähe]]}
klass10 = {}
klass11 = {}
klass12 = {}
####

#{'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1', '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}}

def grupeerimine():
    klass10 = {}
    klass11 = {}
    klass12 = {}
    formating = []
    temp1 = {}
    korda = 0
    with open('testinput2.csv', 'r', encoding="utf-8") as input_file:
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
                
                #### Paneb õige klassi sõnastikku
                if row[3] == '12':
                    for i in range(len(formating)):
                        temp1[formating[i]] = row[i]
                    klass12[row[2]] = temp1
                elif row[3] == '11':
                    for i in range(len(formating)):
                        temp1[formating[i]] = row[i]
                    klass12[row[2]] = temp1
                elif row[3] == '10':
                    for i in range(len(formating)):
                        temp1[formating[i]] = row[i]
                    klass12[row[2]] = temp1
                else:
                    print("TEKKIS VIGA ÕPILASE ÕIGESSE SÕNASTIKKU PANEMISEL")
                temp1 = {}
    return klass10, klass11, klass12

klass10, klass11, klass12 = grupeerimine()
#print(klass12)
ained = {}
def ained_seadistamine():
    ainedList = []
    ained = {}
    with open('ained.txt', 'r', encoding="utf-8") as ainedfail:
        for i in ainedfail: #### {Python 2 : {"kohad" : 40, "vajalikud" = "Python 1", "lisad" : ""}}
            temp1 = {}
            ainedList = i.replace("\n", "").split(";")
            #ained[ainedList[0]]["kohad"] = ainedList[1]
            #ained[ainedList[0]]["kohad"] = 40
            temp1["periood"] = ainedList[2]
            temp1["kohad"] = ainedList[1]
            temp1["kohtiVõetud"] = 0
            temp1["vajalikud"] = ainedList[3]
            temp1["lisad"] = ainedList[4]
            temp1["vastuVõetud"] = []
            ained[ainedList[0]] = temp1
            #print(ained)
        #print(ained)
        return ained


klass10_seadistatud, klass11_seadistatud, klass12_seadistatud = {}, {}, {}


#### 12.klassi 1. valik kirja 

def seadistamine(õpilaseNimi, õpilaneDict):
    õpilaseKursused = [] #### [[P1H väga, P1H võtaks, P1H vähe], [P1Õ väga, P1õ võtaks, P1Õ vähe]]
    #õpilaseNimi = list(õpilaneDict.keys())[0]
    ajutine = []
    korda1 = 0
    #print(õpilaseNimi)
    for i in range(4, len(list(õpilaneDict))):
        if korda1 % 3 == 0 and korda1 != 0:
            õpilaseKursused.append(ajutine)
            ajutine = []
        korda1 += 1
        ajutine.append(list(õpilaneDict.values())[i])
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


ained = ained_seadistamine()
#print(ained)

resultList = {} ####{Marcus : ['Planimeetria alused', '3D-modelleerimine']}
result = {} ####{Marcus : {1 : 'Planimeetria alused', 2 : '', 3 : '3D-modelleerimine'}}
tempSõnastik = {}


#### [['Planimeetria alused', 'Globaliseeruv maailm', 'Ei taha'], ['Programmeerimine keeles Python 1', 'Programmeerimine keeles Python 1', 'Programmeerimine keeles Python 1'], ['3D-modelleerimine', 'Küberkaitse 1', '3D-modelleerimine'], ['Statistiline maailmapilt', 'Ei taha', 'Ei taha'], ['Loomade käitumine', 'Ei taha', 'Ei taha'], ['Majandusõpe', 'Millest ELU koosneb?', 'Majandusõpe'], ['Ettevõtlusõpe', 'Liiklusfüüsika', 'Liiklusfüüsika'], ['CAD joonestamine', 'Ei taha', 'Ei taha']]
for i in range(0, len(klass12_seadistatud)):
    temp2 = []
    klass12_seadistatud_temp = klass12_seadistatud
    õpilaseNimi, õpilaseKursused = random.choice(list(klass12_seadistatud_temp.items()))
    del klass12_seadistatud_temp[õpilaseNimi]
    tempSõnastik = {k: '' for k in range(1, len(õpilaseKursused)+1)}
    result[õpilaseNimi] = tempSõnastik
    print(result)
    for i in range(0, len(õpilaseKursused)):
        temp2 = resultList.get(õpilaseNimi, [])
        resultList[õpilaseNimi] = temp2
        if õpilaseKursused[i][0] == "Ei taha": ### EI TEA KAS TÖÖTAB
            temp2 = resultList.get(õpilaseNimi, [])
            temp2.append("")
            resultList[õpilaseNimi] = temp2
        elif ained[õpilaseKursused[i][0]]['kohtiVõetud'] <  int(ained[õpilaseKursused[i][0]]['kohad']):  # 1. kui mahub 2. ei ole juba sellel kursusel 3. ei ole see periood veel midagi võetud 4. vajalikud on võetud (eelmine periood või eelmine aasta)
            if õpilaseKursused[i][0] not in resultList[õpilaseNimi]: #### õpilasel on see kursus juba võetud
                if ained[õpilaseKursused[i][0]]['periood'] != '': #### õpilasel on sellel perioodil midagi juba võetud
                    if ained[õpilaseKursused[i][0]]['vajalikud'] == '' or ained[õpilaseKursused[i][0]]['vajalikud'] in resultList[õpilaseNimi]: ##### kontrollib kas õpilane on see aasta võtnud eeldusained
                        print(õpilaseNimi + " vastu võetud " + õpilaseKursused[i][0])
                        ained[õpilaseKursused[i][0]]['kohtiVõetud'] += 1
                        ained[õpilaseKursused[i][0]]['vastuVõetud'].append(õpilaseNimi)
                        ########
                        temp2 = resultList.get(õpilaseNimi, [])
                        temp2.append(õpilaseKursused[i][0])
                        resultList[õpilaseNimi] = temp2
                        #print(resultList)
                        ########
                        tempSõnastik[i+1] = õpilaseKursused[i][0]
                        result[õpilaseNimi] = tempSõnastik
                        print(result)
                        ########
                        if ained[õpilaseKursused[i][0]]['lisad'] != '':
                            for j in range(0, len(ained[õpilaseKursused[i][0]]['lisad'].split(","))):
                                print(õpilaseNimi + " vastu võetud " + ained[õpilaseKursused[i][0]]['lisad'].split(",")[j])
                                ained[ained[õpilaseKursused[i][0]]['lisad'].split(",")[j]]['vastuVõetud'].append(õpilaseNimi)
                                #####
                                temp2 = resultList.get(õpilaseNimi, [])
                                temp2.append(ained[õpilaseKursused[i][0]]['lisad'].split(",")[j])
                                resultList[õpilaseNimi] = temp2
                                #print(resultList)
                                #####
                                tempSõnastik[int(ained[ained[õpilaseKursused[i][0]]['lisad'].split(",")[j]]['periood'])] = ained[õpilaseKursused[i][0]]['lisad'].split(",")[j]
                                result[õpilaseNimi] = tempSõnastik
                                print(result)
                                #####
                    else:
                        print(õpilaseNimi + " ei saanud " + õpilaseKursused[i][0] + ",sest ei ole võetnud eeldusainet " + ained[õpilaseKursused[i][0]]['vajalikud'])
                else:
                    print(õpilaseNimi + " on juba sellel perioodil muule kursusele sisse saanud")
            else:
                print(õpilaseNimi + " on juba " + õpilaseKursused[i][0] + " kursusele sisse saanud eelneval hetkel")
        else:
            pass
            '''
            temp2 = resultList.get(õpilaseNimi, [])
            temp2.append("")
            resultList[õpilaseNimi] = temp2
            '''
