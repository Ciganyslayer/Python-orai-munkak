f = open("kolcsonzesek.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()
class kolcsonzes:
    def __init__(self, nev, jazon, eora, eperc, vora, vperc):
        self.nev = nev
        self.jazon = jazon
        self.eora = int(eora)
        self.eperc = int(eperc)
        self.vora = int(vora)
        self.vperc = int(vperc)

kolcsonzesek = []
for i in range(len(lines)):
    darabok = lines[i].strip().split(";")
    nigger = kolcsonzes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    kolcsonzesek.append(nigger)
