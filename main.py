import random
from csv import reader
from collections import OrderedDict

#### {Nimi,klass : [[P1Hväga, P1Hvõtaks, P1Hvähe], [P1Õväga, P1Õvõtaks, P1Õvähe]]}
klass10 = {}
klass11 = {}
klass12 = {}
korda = 0
formating = []
temp1 = {}
####

#{'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1', '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}}

with open('testinput2.csv', 'r') as input_file:
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


#print(klass12)
#print(klass10)


#### 12.klassi 1. valik kirja 

def registreerimine(õpilaseNimi, õpilaneDict, tegevus):
#{'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1',
# '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}}
    õpilaseKursused = [] #### [[P1H väga, P1H võtaks, P1H vähe], [P1Õ väga, P1õ võtaks, P1Õ vähe]]
    #õpilaseNimi = list(õpilaneDict.keys())[0]
    ajutine = []
    korda1 = 0
    print(õpilaseNimi)
    for i in range(4, len(list(õpilaneDict))):
        if korda1 % 3 == 0 and korda1 != 0:
            õpilaseKursused.append(ajutine)
            ajutine = []
        korda1 += 1
        ajutine.append(list(õpilaneDict.values())[i])
    print(õpilaseKursused)


'''
country, capital = random.choice(list(klass12.items()))
'''
for i in range(0, len(klass12)):
    õpilaseNimi, õpilaseDict = random.choice(list(klass12.items()))
    del klass12[õpilaseNimi]
    registreerimine(õpilaseNimi, õpilaseDict, "väga")


#registreerimine({'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1', '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}})
