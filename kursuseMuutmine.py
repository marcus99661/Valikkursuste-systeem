#### Tegeleb Discordist tulnud käskudega

# 1. Kursusest ära ütlemine, kui mingi muu kursus vajab eemaldatud kursust, siis see tuleb ka ära eemaltada
# 2. Kursuse lisamine (kontroll kas on kohti vaba, õpilasel ei ole juba midagi võetud, eeldusained on jne)
# 3. Saadud kursuste kinnitamine
# 4. ???Doomino effektiga täita tühjad kohad???
# 5. Logi faili loomine muudatustest
'''
class Õpilane:
    def __init__(self, nimi, kursus)
'''
tähed = ["A", "B", "C", "D", "E", "F", "G", "H", "I"]
#from openpyxl import Workbook
from openpyxl import load_workbook
import openpyxl

def kursuseEemaldamine(nimi, kursus): ### Peab muutma õpetajateFailis ka, kui võrdleb nimesid ja kursuseid siis võtab ära suure tähe ja tühikud
    õpilaste = load_workbook("õpilasteFail.xlsx")
    leht = õpilaste['Sheet']
    for rida in range(1, leht.max_row):
        #print(leht['A' + str(i)].value)
        if leht['A' + str(rida)].value == nimi:
            #print("Õpilane nimega: " + nimi + " leitud")
            for j in tähed:
                #print(leht[j + str(rida)].value)
                if leht[j + str(rida)].value == kursus:
                    print("Leitud kursus nimega: " + kursus)
                    sheet = õpilaste.get_sheet_by_name("Sheet")
                    sheet[j + str(rida)] = "---"
                    õpilaste.save('õpilasteFail.xlsx')
                    break
                elif j == tähed[-1]:
                    return "Ei leitud kursust nimega: " + kursus + ", lõpetan tegevuse"
                    #print("Ei leitud kursust nimega: " + kursus + ", lõpetan tegevuse")
            õpilaste.close()
            break
    ###############
    õpetajate = load_workbook("õpetajateFail.xlsx")
    leht = õpetajate['Sheet']
    for rida in range(1, leht.max_row):
        if leht['A' + str(rida)].value == kursus:
            #print(leht['A' + str(rida)].value)
            print(leht['E' + str(rida)].value)
            õpilased = leht['E' + str(rida)].value.split(", ")
            try:
                õpilased.remove(nimi)
            except:
                return "ERROR, õpilast ei leitud õpetajate failis kursuse all kirjas"
                #print("ERROR, õpilast ei leitud õpetajate failis kursuse all kirjas")
            seperator = ", "
            sheet = õpilaste.get_sheet_by_name("Sheet")
            sheet['E' + str(rida)] = seperator.join(õpilased)
            print(seperator.join(õpilased))
            õpetajate.save('õpetajateFail.xlsx')

    return 'Edukalt eemaldatud ' + nimi + 'kursuselt "' + kursus + '"'
    #print("Lõpetatud õpilaselt kursuse eemaldamine")

def kursuseLisamine(nimi, kursus): ## võtab ained.txt kursuse kohad, võtab õpetaja failist õpilaste arvu ja lisab õpilase juurde kui on ruumi, kontrollib eeldusaineid (ja klassi)
    õpilaste = load_workbook("õpilasteFail.xlsx")
    leht = õpilaste['Sheet']
    for i in range(1, 100):
        #print(leht['A' + str(i)].value)
        if leht['A' + str(i)].value == nimi:
            #print("Õpilane nimega: " + nimi + " leitud")
            rida = i

if __name__ == "__main__":
    #kursuseEemaldamine("Emily 445", "Fotograafia 1")
    #kursuseEemaldamine("Emily 445", "Fot")
    pass
