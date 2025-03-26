f = open("szavazatok.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class szavazas:
    def __init__(self, korzetszam, szavazat, vezeteknev, utonev, part):
        self.korzetszam = int(korzetszam)
        self.szavazat = int(szavazat)
        self.vezeteknev = vezeteknev
        self.utonev = utonev
        self.part = part

jeloltek = []
for i in range(len(lines)):
    darabok = lines[i].strip().split(" ")
    d = szavazas(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4])
    jeloltek.append(d)
print(f"1. FELADAT: A szavazáson indulók száma: ({len(jeloltek)})")

hepjeloltek = 0
for i in range(len(jeloltek)):
    if jeloltek[i].part == "HEP":
        hepjeloltek += 1
print(f"2. FELADAT: A HEP pártban indulók száma: ({hepjeloltek})")

hetkor = []
for i in range(len(jeloltek)):
    if jeloltek[i].korzetszam == 7:
        hetkor.append(jeloltek[i].szavazat)
print(f"3. FELADAT: A 7. körzetben indulók száma közül a legkevesebbet szerző: ({min(hetkor)})")
