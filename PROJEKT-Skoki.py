import random

class Skakalec:

    def __init__(self, ime = "Unnamed"):
        self.dolzina_skoka = 0
        self.ime = ime

    def __repr__(self):
        return "Skakalec({})".format(self.ime)       

    def nastavi_dolzino_skoka(self, x):
        self.dolzina_skoka = x
        
      
class Veter:

    def __init__(self, moc = 0):
        self.moc = moc
    
    '''Nastavi veter ba poljubno vrednost med -3 in 3 m/s'''
    def nakljucno_nastavi_moc(self):
        self.moc = random.uniform(-3,3)

class Igra:
    
    def __init__(self):
        self.igralec = None

    def zacni(self):
        ime = self.pridobi_ime()
        self.igralec = Skakalec(ime)

        
        zelja = self.pridobi_zeljo()
        if zelja == "skok":
            self.igralec.nastavi_dolzino_skoka(30 + Veter.moc * 10)
            print("Skočila si " + str(self.igralec.dolzina_skoka))
        else:
            print("Tega ukaza ne poznam...")
            
            

    def pridobi_ime(self):
        ime = input("Ime skakalca? ")
        return ime

    def pridobi_zeljo(self):
        zelja = input("Kaj želiš sedaj, " + self.igralec.ime + "? (skok/...) ")
        return zelja
    

i = Igra()
i.zacni()

