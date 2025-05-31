f = open("filmek (1).txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()


class diafilm:
    def __init__(self, cim, ev, kockas, szin):
        self.cim = cim
        self.ev = int(ev)
        self.kockas = int(kockas)
        self.szin = int(szin)

diafilmek = []
for i in range(len(lines)):
    darabok = lines[i].strip().split(";")
    d = diafilm(darabok[0], darabok[1], darabok[2], darabok[3])
    diafilmek.append(d)



#1
print(f"1: {len(diafilmek)}-db adat van")

#2
evek = []
for i in range(len(diafilmek)):
    evek.append(diafilmek[i].ev)
legregebbi = min(evek)
for i in range(len(diafilmek)):
    if diafilmek[i].ev == legregebbi:
        print(f"2: a legrebbi diafilm adatai: {diafilmek[i].cim}, {diafilmek[i].ev}, {diafilmek[i].kockas}, {diafilmek[i].szin}")

#3
filmek = []
szam = int(input("aggyá egy szamot:"))
for i in range(len(diafilmek)):
    if szam == diafilmek[i].ev:
        filmek.append(diafilmek[i].cim)
        print(f"3: a megegyezo evu filmek {filmek}")
if szam not in evek:
    print("3: „Nem található az évszám!”")

#4
szinesgecik = []
for i in range(len(diafilmek)):
    if diafilmek[i].szin == -1:
        szinesgecik.append(diafilmek[i].kockas)
osszeg = sum(szinesgecik)
oszto = len(szinesgecik)
print(f"4: az atlag {round(osszeg / oszto, 2)}")