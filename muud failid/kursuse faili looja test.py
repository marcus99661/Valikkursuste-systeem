'''
import PySimpleGUI as sg
import random
import string

"""
    Basic use of the Table Element
"""

sg.theme('Dark Red')

# ------ Some functions to help generate data for the table ------
def word():
    return ''.join(random.choice(string.ascii_lowercase) for i in range(10))
def number(max_val=1000):
    return random.randint(0, max_val)

def make_table(num_rows, num_cols):
    data = [[j for j in range(num_cols)] for i in range(num_rows)]
    data[0] = [word() for __ in range(num_cols)]
    for i in range(1, num_rows):
        data[i] = [word(), *[number() for i in range(num_cols - 1)]]
    return data

# ------ Make the Table Data ------
data = make_table(num_rows=15, num_cols=6)
headings = [str(data[0][x])+'     ..' for x in range(len(data[0]))]


print(headings)
print(data[1:][:])
# ------ Window Layout ------
layout = [[sg.Table(values=data[1:][:], headings=headings, max_col_width=25,
                    # background_color='light blue',
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=20,
                    alternating_row_color='lightyellow',
                    key='-TABLE-',
                    row_height=35,
                    tooltip='This is a table')],
          [sg.Button('Read'), sg.Button('Double'), sg.Button('Change Colors')],
          [sg.Text('Read = read which rows are selected')],
          [sg.Text('Double = double the amount of data in the table')],
          [sg.Text('Change Colors = Changes the colors of rows 8 and 9')]]

# ------ Create Window ------
window = sg.Window('The Table Element', layout,
                   # font='Helvetica 25',
                   )

# ------ Event Loop ------
while True:
    event, values = window.read()
    print(event, values)
    if event == sg.WIN_CLOSED:
        break
    if event == 'Double':
        for i in range(len(data)):
            data.append(data[i])
        window['-TABLE-'].update(values=data)
    elif event == 'Change Colors':
        window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

window.close()
'''
'''
data = "Programmeerimine keeles Python 2;test 123 test;27;4. periood hommik;;Programmeerimine keeles Python 1 hommikul,Programmeerimine keeles Python 1 õhtul;"

data = data.split()
print(data)
data[3] = "test"
print(data)
seperator = ";"
data = seperator.join(data)
print(data)
'''

import copy
#ainedKorras = ['Programmeerimine keeles Python 1 hommikul;Programmeerimine keeles Python 1 õhtu;27;1;;;\n', 'Programmeerimine keeles Python 1 õhtul;Programmeerimine keeles Python 1 hommikul;27;2;;;\n', 'Programmeerimine keeles Python 2;123789645312;27;test;;Programmeerimine keeles Python 1 hommikul,Programmeerimine keeles Python 1 õhtul;\n', 'Hispaania keel 1;;30;2;;;Hispaania keel 2,Hispaania keel 3\n', 'Hispaania keel 2;;30;4;;;\n', 'Hispaania keel 3;;30;6;;;\n', 'Planimeetria alused;;30;1;;;\n', '3D-modelleerimine 3. periood;;35;3;;Joonestamine 2. periood,Joonestamine 4. periood;\n', '3D-modelleerimine 5. periood;;35;7;;Joonestamine 2. periood,Joonestamine 4. periood;\n', 'Statistiline maailmapilt;;24;4;;;\n', 'Loomade käitumine 4. periood;Loomade käitumine 3. periood;24;5;;;\n', 'Loomade käitumine 3. periood;Loomade käitumine 4. periood;24;3;;;\n', 'CAD joonestamine;;14;8;;;\n', 'Veebidisain;;2;4;;;\n', 'Arvutivõrkude alused;;16;6;;;\n', 'Küberkaitse 1;;36;3;;;\n', 'Keskkonnakeemia 2. periood;Keskkonnakeemia 3. periood;20;1;;;\n', 'Keskkonnakeemia 3. periood;Keskkonnakeemia 2. periood;20;4;;;\n', 'Labortöid füüsikas 10. ja 11. klassile;;12;2;;;\n', 'Joonestamine 2. periood;;45;1;;;\n', 'Joonestamine 4. periood;;45;5;;;\n', 'Ettevõtlusõpe 3. periood;Ettevõtlusõpe 5. periood;24;4;;;\n', 'Ettevõtlusõpe 5. periood;Ettevõtlusõpe 3. periood;24;7;;;\n', 'Millest ELU koosneb?;;25;6;;;\n', 'Sissejuhatus ehitusinseneeriasse;;50;4;;;\n', 'Matemaatika ajaloo elemente ja rakendusi;;29;5;;;\n', 'Liiklusfüüsika;;50;7;;;\n', 'Geoinformaatika;;25;1;;;\n', 'Globaliseeruv maailm;;28;1;;;\n', 'Globaalne keskkond;;50;7;;;\n', 'Astronoomia;;30;2;;;\n', 'Astrofüüsika 2. periood;Astrofüüsika 3. periood;35;1;;;\n', 'Astrofüüsika 3. periood;Astrofüüsika 2. periood;35;3;;;\n', 'Keemilised elemendid;;20;3;;;\n', 'Loogika 2. periood;Loogika 4. periood;31;1;;;\n', 'Loogika 4. periood;Loogika 2. periood;31;5;;;\n', 'Programmeerimine keeles Java 1;;26;3;;Programmeerimine keeles Python 1 hommikul,Programmeerimine keeles Python 1 õhtul;\n', 'Programmeerimine keeles Java 2;;26;7;;Programmeerimine keeles Java 1;\n', 'Köögifüüsika;;30;5;;;\n', 'Majandusmatemaatika elemendid;;50;7;;;\n', 'Laboratoorsed tööd bioloogias;;50;7;;;\n', 'Arvutite riistvara ja lisaseadmed;;16;4;;;\n', 'Loodusteadused, tehnoloogia ja ühiskond;;25;5;;;\n', 'Kasutame füüsikat!;;27;5;;;\n', 'Hiina keel 1;;18;2;;;Hiina keel 2,Hiina keel 3\n', 'Hiina keel 2;;18;4;;;\n', 'Hiina keel 3;;18;6;;;\n', 'Kirjandus ja film;;34;1;;;\n', 'Loominguline joonestamine 1;;23;1;;;\n', 'Orgaaniline arhitektuur;;20;1;;;\n', 'Värvus ja kompositsioon;;20;1;;;\n', 'Inimene ja õigus;;16;2;;;\n', 'Kristliku kultuuriruumi alustekstid;;36;2;;;\n', 'Linux Raspberry Pi näitel;;16;2;;;\n', 'Loodusvaatlused ja harrastusteadus;;24;2;;;\n', 'Lähis-Ida 20. sajandi teisest poolest tänapäevani;;36;2;;;\n', 'Meediakursus;;32;2;;;\n', 'Prantsuse keel 1;;20;2;;;Prantsuse keel 2,Prantsuse keel 3\n', 'Prantsuse keel 2;;20;4;;;\n', 'Prantsuse keel 3;;20;6;;;\n', 'Soome keel 1;;25;2;;;Soome keel 2,Soome keel 3\n', 'Soome keel 2;;25;4;;;\n', 'Soome keel 3;;25;6;;;\n', 'Õpioskused;;18;2;;;\n', 'Ajakirjanduse alused;;31;3;;;\n', 'Filosoofia 1;;30;3;;;\n', 'Filosoofia 2;;30;7;Filosoofia 1;;\n', 'Ladina keel 1;;18;3;;;Ladina keel 2\n', 'Ladina keel 2;;18;5;;;\n', 'Loovkirjutamine;;26;3;;;\n', 'Muusikaline kirjaoskus;;18;3;;;\n', 'Natuurist joonistamine;;16;3;;;\n', 'Fotograafia 1;;24;4;;;\n', 'Inimene ja ühiskond 3. periood;Inimene ja ühiskond 4. periood;36;4;;;\n', 'Inimene ja ühiskond 4. periood;Inimene ja ühiskond 3. periood;36;4;;;\n', 'Sissejuhatus ehitusinseneeriasse;;22;4;;;\n', 'Teadusajalugu 3. periood;Teadusajalugu 5. periood;30;4;;;\n', 'Teadusajalugu 5. periood;Teadusajalugu 3. periood;30;8;;;\n', 'Turundus;;26;4;;;\n', 'Vaimne tervis ja selle hoidmine;;24;4;;;\n', 'Klassikaline skulptuur;;20;5;;;\n', 'Kujutav geomeetria;;22;5;;;\n', 'Loominguline joonistamine 2;;22;5;;Loominguline joonestamine 1;\n', 'Praktiline kommunikatsioon;;35;5;;;\n', 'Majandusõpe;;36;6;;;\n', 'Meditsiinikursus;;15;6;;;\n', 'Psühholoogia alused;;24;6;;;\n', 'Riigikaitse 1;;80;6;;;\n', 'Riigikaitse 2;;80;8;;Riigikaitse 1;\n', 'Teater Vanemuise kultuuritänavas;;25;6;;;\n', 'Ajakirjanduse praktika;;30;8;;Meediakursus,Praktiline kommunikatsioon,Ajakirjanduse alused;\n', 'Karjääriõpetus;;30;8;;;\n', 'Mobiilirakenduste loomine (APP Inventor);;18;8;;;\n', 'Projektikirjutamisõpe;;16;8;;;\n', 'Raamatukunst;;20;7;;;\n', 'Finantsmõtlemine;;16;1;;;\n', 'Tänavakunst;;20;7;;;']['Programmeerimine keeles Python 1 hommikul;Programmeerimine keeles Python 1 õhtu;27;1;;;\n', 'Programmeerimine keeles Python 1 õhtul;Programmeerimine keeles Python 1 hommikul;27;2;;;\n', 'Programmeerimine keeles Python 2;123789645312;27;test;;Programmeerimine keeles Python 1 hommikul,Programmeerimine keeles Python 1 õhtul;\n', 'Hispaania keel 1;;30;2;;;Hispaania keel 2,Hispaania keel 3\n', 'Hispaania keel 2;;30;4;;;\n', 'Hispaania keel 3;;30;6;;;\n', 'Planimeetria alused;;30;1;;;\n', '3D-modelleerimine 3. periood;;35;3;;Joonestamine 2. periood,Joonestamine 4. periood;\n', '3D-modelleerimine 5. periood;;35;7;;Joonestamine 2. periood,Joonestamine 4. periood;\n', 'Statistiline maailmapilt;;24;4;;;\n', 'Loomade käitumine 4. periood;Loomade käitumine 3. periood;24;5;;;\n', 'Loomade käitumine 3. periood;Loomade käitumine 4. periood;24;3;;;\n', 'CAD joonestamine;;14;8;;;\n', 'Veebidisain;;2;4;;;\n', 'Arvutivõrkude alused;;16;6;;;\n', 'Küberkaitse 1;;36;3;;;\n', 'Keskkonnakeemia 2. periood;Keskkonnakeemia 3. periood;20;1;;;\n', 'Keskkonnakeemia 3. periood;Keskkonnakeemia 2. periood;20;4;;;\n', 'Labortöid füüsikas 10. ja 11. klassile;;12;2;;;\n', 'Joonestamine 2. periood;;45;1;;;\n', 'Joonestamine 4. periood;;45;5;;;\n', 'Ettevõtlusõpe 3. periood;Ettevõtlusõpe 5. periood;24;4;;;\n', 'Ettevõtlusõpe 5. periood;Ettevõtlusõpe 3. periood;24;7;;;\n', 'Millest ELU koosneb?;;25;6;;;\n', 'Sissejuhatus ehitusinseneeriasse;;50;4;;;\n', 'Matemaatika ajaloo elemente ja rakendusi;;29;5;;;\n', 'Liiklusfüüsika;;50;7;;;\n', 'Geoinformaatika;;25;1;;;\n', 'Globaliseeruv maailm;;28;1;;;\n', 'Globaalne keskkond;;50;7;;;\n', 'Astronoomia;;30;2;;;\n', 'Astrofüüsika 2. periood;Astrofüüsika 3. periood;35;1;;;\n', 'Astrofüüsika 3. periood;Astrofüüsika 2. periood;35;3;;;\n', 'Keemilised elemendid;;20;3;;;\n', 'Loogika 2. periood;Loogika 4. periood;31;1;;;\n', 'Loogika 4. periood;Loogika 2. periood;31;5;;;\n', 'Programmeerimine keeles Java 1;;26;3;;Programmeerimine keeles Python 1 hommikul,Programmeerimine keeles Python 1 õhtul;\n', 'Programmeerimine keeles Java 2;;26;7;;Programmeerimine keeles Java 1;\n', 'Köögifüüsika;;30;5;;;\n', 'Majandusmatemaatika elemendid;;50;7;;;\n', 'Laboratoorsed tööd bioloogias;;50;7;;;\n', 'Arvutite riistvara ja lisaseadmed;;16;4;;;\n', 'Loodusteadused, tehnoloogia ja ühiskond;;25;5;;;\n', 'Kasutame füüsikat!;;27;5;;;\n', 'Hiina keel 1;;18;2;;;Hiina keel 2,Hiina keel 3\n', 'Hiina keel 2;;18;4;;;\n', 'Hiina keel 3;;18;6;;;\n', 'Kirjandus ja film;;34;1;;;\n', 'Loominguline joonestamine 1;;23;1;;;\n', 'Orgaaniline arhitektuur;;20;1;;;\n', 'Värvus ja kompositsioon;;20;1;;;\n', 'Inimene ja õigus;;16;2;;;\n', 'Kristliku kultuuriruumi alustekstid;;36;2;;;\n', 'Linux Raspberry Pi näitel;;16;2;;;\n', 'Loodusvaatlused ja harrastusteadus;;24;2;;;\n', 'Lähis-Ida 20. sajandi teisest poolest tänapäevani;;36;2;;;\n', 'Meediakursus;;32;2;;;\n', 'Prantsuse keel 1;;20;2;;;Prantsuse keel 2,Prantsuse keel 3\n', 'Prantsuse keel 2;;20;4;;;\n', 'Prantsuse keel 3;;20;6;;;\n', 'Soome keel 1;;25;2;;;Soome keel 2,Soome keel 3\n', 'Soome keel 2;;25;4;;;\n', 'Soome keel 3;;25;6;;;\n', 'Õpioskused;;18;2;;;\n', 'Ajakirjanduse alused;;31;3;;;\n', 'Filosoofia 1;;30;3;;;\n', 'Filosoofia 2;;30;7;Filosoofia 1;;\n', 'Ladina keel 1;;18;3;;;Ladina keel 2\n', 'Ladina keel 2;;18;5;;;\n', 'Loovkirjutamine;;26;3;;;\n', 'Muusikaline kirjaoskus;;18;3;;;\n', 'Natuurist joonistamine;;16;3;;;\n', 'Fotograafia 1;;24;4;;;\n', 'Inimene ja ühiskond 3. periood;Inimene ja ühiskond 4. periood;36;4;;;\n', 'Inimene ja ühiskond 4. periood;Inimene ja ühiskond 3. periood;36;4;;;\n', 'Sissejuhatus ehitusinseneeriasse;;22;4;;;\n', 'Teadusajalugu 3. periood;Teadusajalugu 5. periood;30;4;;;\n', 'Teadusajalugu 5. periood;Teadusajalugu 3. periood;30;8;;;\n', 'Turundus;;26;4;;;\n', 'Vaimne tervis ja selle hoidmine;;24;4;;;\n', 'Klassikaline skulptuur;;20;5;;;\n', 'Kujutav geomeetria;;22;5;;;\n', 'Loominguline joonistamine 2;;22;5;;Loominguline joonestamine 1;\n', 'Praktiline kommunikatsioon;;35;5;;;\n', 'Majandusõpe;;36;6;;;\n', 'Meditsiinikursus;;15;6;;;\n', 'Psühholoogia alused;;24;6;;;\n', 'Riigikaitse 1;;80;6;;;\n', 'Riigikaitse 2;;80;8;;Riigikaitse 1;\n', 'Teater Vanemuise kultuuritänavas;;25;6;;;\n', 'Ajakirjanduse praktika;;30;8;;Meediakursus,Praktiline kommunikatsioon,Ajakirjanduse alused;\n', 'Karjääriõpetus;;30;8;;;\n', 'Mobiilirakenduste loomine (APP Inventor);;18;8;;;\n', 'Projektikirjutamisõpe;;16;8;;;\n', 'Raamatukunst;;20;7;;;\n', 'Finantsmõtlemine;;16;1;;;\n', 'Tänavakunst;;20;7;;;']
#ained_temp = copy.deepcopy(ainedKorras)


######### ainedKorras = [['Programmeerimine keeles Python 1 hommikul','Programmeerimine keeles Python 1 õhtu','27','1','','']]
ained_temp = [['Programmeerimine keeles Python 1 hommikul', 'Programmeerimine keeles Python 1 õhtu', '27', '2. periood hommik', '', '', ''], ['Programmeerimine keeles Python 1 õhtul', 'Programmeerimine keeles Python 1 hommikul', '27', '2. periood õhtu     ', '', '', '']]
'''
if ainedKorras[i][3] == 1:
    ainedKorras[i][3] = "2. periood hommik"
elif True:
    pass
'''
seperator = ";"
ained_temp_temp = []
for i in range(0, len(ained_temp)):
    if ained_temp[i][3] == "2. periood hommik":
        ained_temp[i][3] = "1"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "2. periood õhtu     ":
        ained_temp[i][3] = "2"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "3. periood hommik":
        ained_temp[i][3] = "3"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "3. periood õhtu     ":
        ained_temp[i][3] = "4"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "4. periood hommik":
        ained_temp[i][3] = "5"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "4. periood õhtu     ":
        ained_temp[i][3] = "6"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "5. periood hommik":
        ained_temp[i][3] = "7"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"
    elif ained_temp[i][3] == "5. periood õhtu     ":
        ained_temp[i][3] = "8"
        ained_temp[i] = seperator.join(ained_temp[i]) + "\n"


print(ained_temp)