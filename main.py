import random
from csv import reader
from collections import OrderedDict

#### {Nimi,klass : [[P1Hväga, P1Hvõtaks, P1Hvähe], [P1Õväga, P1Õvõtaks, P1Õvähe]]}
klass10 = {}
klass11 = {}
klass12 = {}
korda = 0
formating = []
temp = []
temp1 = {}
####

#{'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1', '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}}

with open('testinput1.csv', 'r') as input_file:
    csv_reader = reader(input_file)
    for row in csv_reader:
        #print(row)
        if korda == 0:
            formating = ''.join(row).split(",")
            for i in range(len(formating)):
                formating[i] = formating[i].replace('"', "")
            korda += 1
        else:
            temp = ''.join(row).split(",")
            for i in range(len(temp)):
                temp[i] = temp[i].replace('"', "")
            
            #### Paneb õige klassi sõnastikku
            if temp[3] == '12':
                for i in range(len(formating)):
                    temp1[formating[i]] = temp[i]
                klass12[temp[2]] = temp1
            elif temp[3] == '11':
                for i in range(len(formating)):
                    temp1[formating[i]] = temp[i]
                klass11[temp[2]] = temp1
            elif temp[3] == '10':
                for i in range(len(formating)):
                    temp1[formating[i]] = temp[i]
                klass10[temp[2]] = temp1
            else:
                print("TEKKIS VIGA ÕPILASE ÕIGESSE SÕNASTIKKU PANEMISEL")


print(klass12)
print(klass10)


#### 12.klassi 1. valik kirja 

def registreerimine(õpilaneDict):
#{'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1',
# '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}}

    õpilaseKursused = [] #### [[P1H väga, P1H võtaks, P1H vähe], [P1Õ väga, P1õ võtaks, P1Õ vähe]]
    õpilaseNimi = list(õpilaneDict.keys())[0]
    ajutine = []
    print(õpilaseNimi)
    '''
    for i in range(4, len(õpilaneDict)):
        if i % 3 == 0:
            õpilaseKursused.append(ajutine)
            ajutine = []
        ajutine.append(õpilaneDict[i])
    print(õpilaseKursused)
    '''

registreerimine({'Marcus': {'Ajatempel': '2020/07/04 10:41:27 PM GMT +3', 'Kasutajanimi': 'marcus99661@gmail.com', 'Nimi': 'Marcus', 'Klass': '10', '2. periood hommik 1. valik': 'Aine 1', '2. periood hommik 2. valik': 'Aine 2', '2. periood hommik 3. valik': 'Ei taha', '2. periood Ãµhtu 1. valik': 'Ei taha', 'EI VASTA': ''}})
