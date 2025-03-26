f = open("utca.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

elsosor = lines.pop(0)
darabok = elsosor.strip().split()
adoA = int(darabok[0])
adoB = int(darabok[1])
adoC = int(darabok[2])

class haz:
    def __init__(self, adosz, utca, hsz, sav, terulet):
        self.adosz = adosz
        self.utca = utca
        self.hsz = hsz
        self.sav = sav
        self.terulet = int(terulet)

hazak = []
for i in range(len(lines)):
    darabok = lines[i].strip().split()
    h = haz(lines[0], darabok[1], darabok[2], darabok[3], darabok[4])
    hazak.append(h)
print(f"2. feladat: A mintában ({len(hazak)}) telek szerepel.")
