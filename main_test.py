import random
from csv import reader
from collections import OrderedDict

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
print(klass12)
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
            temp1["kohad"] = ainedList[1]
            temp1["kohtiVõetud"] = 0
            temp1["vajalikud"] = ainedList[2]
            temp1["lisad"] = ainedList[3]
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

result = {}


#### {Marcus : ['Planimeetria alused', '', '3D-modelleerimine']}
#### [['Planimeetria alused', 'Globaliseeruv maailm', 'Ei taha'], ['Programmeerimine keeles Python 1', 'Programmeerimine keeles Python 1', 'Programmeerimine keeles Python 1'], ['3D-modelleerimine', 'Küberkaitse 1', '3D-modelleerimine'], ['Statistiline maailmapilt', 'Ei taha', 'Ei taha'], ['Loomade käitumine', 'Ei taha', 'Ei taha'], ['Majandusõpe', 'Millest ELU koosneb?', 'Majandusõpe'], ['Ettevõtlusõpe', 'Liiklusfüüsika', 'Liiklusfüüsika'], ['CAD joonestamine', 'Ei taha', 'Ei taha']]
for i in range(0, len(klass12_seadistatud)):
    temp2 = []
    klass12_seadistatud_temp = klass12_seadistatud
    õpilaseNimi, õpilaseKursused = random.choice(list(klass12_seadistatud_temp.items()))
    del klass12_seadistatud_temp[õpilaseNimi]
    for i in range(0, len(õpilaseKursused)):
        temp2 = result.get(õpilaseNimi, [])
        result[õpilaseNimi] = temp2
        if õpilaseKursused[i][0] == "Ei taha": ### EI TEA KAS TÖÖTAB
            temp2 = result.get(õpilaseNimi, [])
            temp2.append("")
            result[õpilaseNimi] = temp2
        elif ained[õpilaseKursused[i][0]]['kohtiVõetud'] <  int(ained[õpilaseKursused[i][0]]['kohad']) and õpilaseKursused[i][0] not in result[õpilaseNimi] and len(result[õpilaseNimi]) < i+1:  # 1. kui mahub 2. ei ole juba sellel kursusel 3. vajalikud on võetud (eelmine periood või eelmine aasta) 4. ei ole see periood veel midagi võetud
            print(õpilaseNimi + " vastu võetud " + õpilaseKursused[i][0])
            ained[õpilaseKursused[i][0]]['kohtiVõetud'] += 1
            #print(ained[õpilaseKursused[i][0]])
            ained[õpilaseKursused[i][0]]['vastuVõetud'].append(õpilaseNimi)
            #print(ained[õpilaseKursused[i][0]])
            #print(ained)
            ########
            temp2 = result.get(õpilaseNimi, [])
            temp2.append(õpilaseKursused[i][0])
            result[õpilaseNimi] = temp2
            #print(result)
            ########
            if ained[õpilaseKursused[i][0]]['lisad'] != '': #### TÖÖTAB ÕIGESTI AINULT KUI KURSUSE LISAD ON JÄRJESTIKKU. TULEKS ÄRA MUUTA
                for j in range(0, len(ained[õpilaseKursused[i][0]]['lisad'].split(","))):
                    print(õpilaseNimi + " vastu võetud " + ained[õpilaseKursused[i][0]]['lisad'].split(",")[j])
                    ained[ained[õpilaseKursused[i][0]]['lisad'].split(",")[j]]['vastuVõetud'].append(õpilaseNimi)
                    temp2 = result.get(õpilaseNimi, [])
                    temp2.append(ained[õpilaseKursused[i][0]]['lisad'].split(",")[j]) #### LISAD KURSUSED TULEB PANNA ÕIGESSE KOHTA
                    result[õpilaseNimi] = temp2
                    #print(result)
        else:
            temp2 = result.get(õpilaseNimi, [])
            temp2.append("")
            result[õpilaseNimi] = temp2

