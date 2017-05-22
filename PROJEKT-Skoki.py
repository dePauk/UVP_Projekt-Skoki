class Skakalec:
    def __init__(self, ime = "Unnamed"):
        dolzina_skoka = 0
        self.ime = ime
    def __repr__(self):
        return "Objekt"       
    def dolzina_skoka(self):
        self.dolzina_skoka = dolzina_skoka
        
      
class Veter:
    '''Nastavi veter ba poljubno vrednost med -3 in 3 m/s'''
    def moc(self):
        moc = 0

        
import random




print ("Ime skakalca?")
ime = input()
print ("Kaj želiš sedaj, " + ime + "? (skok()/...)")


SKAKALEC = Skakalec(ime)
       
nakljucni_veter = random.uniform(-3,3)
Veter.moc = nakljucni_veter


SKAKALEC.dolzina_skoka = 30 + Veter.moc * 10

def skok(x = ime):
    return SKAKALEC.dolzina_skoka
