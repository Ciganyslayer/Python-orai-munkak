f = open("filmek.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class diafilm:
    def __init__(self, cim, ev, kockak, szines,):
        self.cim = cim
        self.ev = int(ev)
        self.kockak = int(kockak)
        self.szines = int(szines)

diafilmek = []
for i in range(len(lines)):
    darabok = lines[i].strip().split(";")
    d = diafilm(darabok[0], darabok[1], darabok[2], darabok[3])
    diafilmek.append(d)

print(f"1.feladat: {len(diafilmek)}-db diafilm van a listában.")



evszamok = []
for i in range(len(diafilmek)):
    evszamok.append(diafilmek[i].ev)
legoreg = min(evszamok)
for i in range(len(diafilmek)):
    if diafilmek[i].ev == legoreg:
        print(f"2.feladat: A legrégebbi diafilm adatai: {diafilmek[i].cim, diafilmek[i].ev, diafilmek[i].kockak}")



evszam = int(input("Irjon be egy évszámot: "))
for i in range(len(diafilmek)):
    if diafilmek[i].ev == evszam:
        print(f"3.feladat: A {evszam} évben készült diafilmek: ({diafilmek[i].cim})")
if evszam not in evszamok:
    print("3.feladat: Nem található az évszám!")






