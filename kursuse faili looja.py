import PySimpleGUI as sg
import time
import pandas as pd

saiÕigeFaili = True
ained = []

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
            loetavFail = open(failiNimi, 'r', encoding="utf-8")
            for i in loetavFail:
                print(i.replace("\n", ""))
                ained.append(i.replace("\n", ""))
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
    print("")
    #print(ained[])
    #ained = [['Programmeerimine keeles Python 1 hommikul','Programmeerimine keeles Python 1 õhtu','27','1','','',''], ['Programmeerimine keeles Python 1 hasdasdommikul','Programmeerimine keeles Pasdasdython 1 õhtu','27','1','','','']]
    while True:
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
                [sg.Button('Double'), sg.Button('Change Colors')],
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
                            print(ainedKorras[rida][j])
                            print(values[j+1])
                            print("")
                        window.close()
                        with open(failiNimi, 'r', encoding="utf-8") as file:
                            # read a list of lines into data
                            data = file.readlines()
                        
                        print(data[rida].split(";")[3]) 
                        
                        
                        # now change the 2nd line, note that you have to add a newline
                        seperator = ";"
                        data[rida] = seperator.join(ainedKorras[rida]) + "\n"

                        # and write everything back
                        with open(failiNimi, 'w', encoding="utf-8") as file:
                            file.writelines(data)

                    elif event == "Cancel":
                        print("Ei toimu muudatus")
                    else:
                        print("ERROR")
            except:
                sg.popup('Peate sisestama ainult numbri')
            print(rida)
        if event == 'Double':
            for i in range(len(data)):
                data.append(data[i])
            window['-TABLE-'].update(values=data)
        elif event == 'Change Colors':
            window['-TABLE-'].update(row_colors=((8, 'white', 'red'), (9, 'green')))

else:
    print("TÜHISTATI")
#sg.popup('You entered', text_input)
window.close()