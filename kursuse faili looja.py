#        VAJA PARANDADA/LISADA
###################################
# LISADA VÕIMALUS UUSI KURSUSI LISADA - PEAKS OLEMA KORRAS
###################################

import PySimpleGUI as sg
import time
import pandas as pd
import copy

saiÕigeFaili = True

layout = [[sg.Text('Sisestage kursuste faili nimi (ilma .txt lõputa)')],      
                 [sg.InputText()],      
                 [sg.Submit(), sg.Cancel()]]      

window = sg.Window('Kursused', layout)    

event, values = window.read()
window.close()
if event == "Submit":
    while saiÕigeFaili:
        failiNimi = values[0] + ".txt"
        try:
            with open(failiNimi, "r", encoding="utf-8") as loetavFail: ### test kas fail on olemas
                pass
            saiÕigeFaili = False
        except:
            layout = [[sg.Text('Sisestatud kursuse nimi oli vale\nSisestage kursuste faili nimi (ilma .txt lõputa)')],      
                         [sg.InputText()],      
                         [sg.Submit(), sg.Cancel()]]
            window = sg.Window('Kursused', layout)
            event, values = window.read()
            if event != "Submit":
                print("TÜHISTATI1")
                window.close()
                break
            else:
                window.close()
    ###jätk
    #print(ainedKorras)
    #print("")
    #print(ained[])
    #ained = [['Programmeerimine keeles Python 1 hommikul','Programmeerimine keeles Python 1 õhtu','27','1','','',''], ['Programmeerimine keeles Python 1 hasdasdommikul','Programmeerimine keeles Pasdasdython 1 õhtu','27','1','','','']]
    while True:
        ained = []
        with open(failiNimi, "r", encoding="utf-8") as loetavFail:
            for i in loetavFail:
                #print(i.replace("\n", ""))
                ained.append(i.replace("\n", ""))
        ainedKorras = []
        for i in range(0, len(ained)):
            temp = []
            temp = ained[i].split(";")
            #print(temp[3])
            perioodil = temp[3]
            if perioodil == '1':
                temp[3] = "2. periood hommik"
            elif perioodil == '2':
                temp[3] = "2. periood õhtu     "
            elif perioodil == '3':
                temp[3] = "3. periood hommik"
            elif perioodil == '4':
                temp[3] = "3. periood õhtu     "
            elif perioodil == '5':
                temp[3] = "4. periood hommik"
            elif perioodil == '6':
                temp[3] = "4. periood õhtu     "
            elif perioodil == '7':
                temp[3] = "5. periood hommik"
            elif perioodil == '8':
                temp[3] = "5. periood õhtu     "
            else:
                temp[3] == "MÄRGITUD VALE PERIOOD"
            ainedKorras.append(temp)
        #print(ainedKorras)
        layout = [[sg.Table(values=ainedKorras, headings=["Nimi", "Alternatiivid", "Kohad", "Periood", "Eeldusained", "Üks eeldusainetest vajalik", "Lisaks peab võtma"], max_col_width=25,
                        #background_color='light blue',
                        auto_size_columns=True,
                        display_row_numbers=True,
                        justification='right',
                        num_rows=10,
                        alternating_row_color='lightblue',
                        #key='-TABLE-',
                        row_height=35,
                        text_color="black")],
                [sg.Button('Muuda rida'),sg.Text('Saab muuta kursust realt: '), sg.InputText()],
                [sg.Button('Lisa uus kursus')],
        ]
        window = sg.Window('Table', layout)
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        if event == "Muuda rida":
            try:
                rida = int(values[1])
                if rida < 0 or rida > len(ainedKorras)-1:
                    sg.popup('Sellist rida ei ole')
                else:
                    layout = [[sg.InputText(rida), sg.Text('Kursuse rida')],
                                [sg.InputText(ainedKorras[rida][0]), sg.Text('Nimi')], 
                                [sg.InputText(ainedKorras[rida][1]), sg.Text('Alternatiivid')],
                                [sg.InputText(ainedKorras[rida][2]), sg.Text('Kohad')],
                                [sg.InputText(ainedKorras[rida][3]), sg.Text('Periood')],
                                [sg.InputText(ainedKorras[rida][4]), sg.Text('Eeldusained')],
                                [sg.InputText(ainedKorras[rida][5]), sg.Text('Üks eeldusainetest vajalik')],
                                [sg.InputText(ainedKorras[rida][6]), sg.Text('Lisaks peab võtma')],
                                [sg.Submit(), sg.Cancel()]]    
                    window1 = sg.Window("Kursuse muutmine", layout)
                    event, values = window1.read()
                    window1.close()
                    print(event)
                    print(values)
                    if event == "Submit":
                        print("Toimub muudatus")
                        for j in range(0, len(ainedKorras[rida])):
                            ainedKorras[rida][j] = values[j+1]
                        window.close()
                        ained_temp = copy.deepcopy(ainedKorras)
                        with open(failiNimi, 'r', encoding="utf-8") as file:
                            # read a list of lines into data
                            data = file.readlines()
                        seperator = ";"
                        print(ained_temp)
                        #ainedKorras[rida] = seperator.join(ainedKorras[rida])
                        print(ained_temp[rida])
                        print("ASDEEDEDEDEDEDE")
                        print(ained_temp)
                        if ained_temp[rida][3] == "2. periood hommik":
                            ained_temp[rida][3] = "1"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3].replace(" ", "") == "2.perioodõhtu":
                            ained_temp[rida][3] = "2"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3] == "3. periood hommik":
                            ained_temp[rida][3] = "3"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3].replace(" ", "") == "2.perioodõhtu":
                            ained_temp[rida][3] = "4"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3] == "4. periood hommik":
                            ained_temp[rida][3] = "5"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3].replace(" ", "") == "2.perioodõhtu":
                            ained_temp[rida][3] = "6"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3] == "5. periood hommik":
                            ained_temp[rida][3] = "7"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        elif ained_temp[rida][3].replace(" ", "") == "2.perioodõhtu":
                            ained_temp[rida][3] = "8"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"
                        else:
                            ained_temp[rida][3] = "PERIOOD VALESTI KIRJUTATUD FAILI"
                            ained_temp[rida] = seperator.join(ained_temp[rida]) + "\n"

                        # now change the 2nd line, note that you have to add a newline
                        data[rida] = ained_temp[rida]
                        print(data)

                        # and write everything back
                        with open(failiNimi, 'w', encoding="utf-8") as file:
                            file.writelines(data)
                        print(ainedKorras)
                        print("ASD123")

                    elif event == "Cancel":
                        print("Ei toimu muudatus")
                    else:
                        print("ERROR")
            except:
                sg.popup('Peate sisestama ainult numbri') ############ VISKAB MILLEGI PÄRAT SELLE ERRORI
            print(rida)

        ########
        elif event == 'Lisa uus kursus':
            layout = [[sg.InputText(), sg.Text('Nimi')], 
                        [sg.InputText(), sg.Text('Alternatiivid')],
                        [sg.InputText(), sg.Text('Kohad')],
                        [sg.Text('Periood')],
                        [sg.Radio('2. periood hommik',group_id=1), sg.Radio('3. periood hommik',group_id=1), sg.Radio('4. periood hommik',group_id=1), sg.Radio('5. periood hommik',group_id=1)],
                        [sg.Radio('2. periood õhtu     ',group_id=1), sg.Radio('3. periood õhtu      ',group_id=1), sg.Radio('4. periood õhtu     ',group_id=1), sg.Radio('5. periood õhtu     ',group_id=1)],
                        [sg.InputText(), sg.Text('Eeldusained')],
                        [sg.InputText(), sg.Text('Üks eeldusainetest vajalik ()')],
                        [sg.InputText(), sg.Text('Lisaks peab võtma')],
                         [sg.Submit(), sg.Cancel()]]    
            window1 = sg.Window("Kursuse lisamine", layout)
            event, values = window1.read()
            window1.close()
            print(values)
            if event == "Submit":
                väike_temp = []
                väike_temp.append(values[0])
                väike_temp.append(values[1])
                väike_temp.append(values[2])
                if values[3] == True:
                    väike_temp.append('1')
                elif values[7] == True:
                    väike_temp.append('2')
                elif values[4] == True:
                    väike_temp.append('3')
                elif values[8] == True:
                    väike_temp.append('4')
                elif values[5] == True:
                    väike_temp.append('5')
                elif values[9] == True:
                    väike_temp.append('6')
                elif values[6] == True:
                    väike_temp.append('7')
                elif values[10] == True:
                    väike_temp.append('8')
                else:
                    väike_temp.append('PERIOOD EI OLE MÄRGITUD')
                väike_temp.append(values[11])
                väike_temp.append(values[12])
                väike_temp.append(values[13])

                with open(failiNimi, 'r', encoding="utf-8") as file:
                    # read a list of lines into data
                    data = file.readlines()
                seperator = ";"
                
                # now change the 2nd line, note that you have to add a newline
                if data[-1][-1] == "n" and data[-1][-2] == '\\':
                    pass
                else:
                    data[-1] += "\n"
                seperator = ";"
                data.append(seperator.join(väike_temp)+ "\n")
                print(data)

                # and write everything back
                with open(failiNimi, 'w', encoding="utf-8") as file:
                    file.writelines(data)
                #print(ainedKorras)
                #print("ASD123")
            elif event == "Cancel":
                print("Ei toimu muudatus")
            else:
                print("ERROR")

        window.close()
else:
    print("TÜHISTATI")
#sg.popup('You entered', text_input)
window.close()
