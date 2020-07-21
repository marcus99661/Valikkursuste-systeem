class Õpilane:
    kool = "Poska"
    def __init__(self, nimi, klass, periood1hommik, periood1õhtu):
        self.nimi = nimi
        self.klass = klass
        self.periood1hommik = periood1hommik
        self.periood1õhtu = periood1õhtu

class Kursus:
    def __init__(self, nimi, periood, kohad, vabadKohad, vajalikud, alternatiivid):
        pass

õpilased = ["Sten", "Marcus", "Kristo Oja"]
                    #       (Sten) 1H         1Õ jne                                            (Marcus) 1H               1Õ
õpilase_kursused = [[["Inka", "Vene", "Test"],["Hommik", "Küberkaitse", "Loom"]], [["asdasdasd", "Vene", "Test"],["123123123k", "Küberkaitse", "Loom"]], [["ginvi", "Vene", "Test"],["H123123ik", "Küberkaitse", "Loom"]]]
for i in range(0, len(õpilased)): 
    õpilased[i] = Õpilane(õpilased[i], 11, õpilase_kursused[i][0], õpilase_kursused[i][1])
    print(õpilased[i].periood1õhtu)
    print(õpilased[i].kool)