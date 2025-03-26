#Kovács Dávid B csoport
f = open("snooker.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class vilagranglista:
    def __init__(self, helyezes, nev, orszag, eredmeny):
        self.helyezes = int(helyezes)
        self.nev = nev
        self.orszag = orszag
        self.eredmeny = int(eredmeny)

snooker = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    d = vilagranglista(darabok[0], darabok[1], darabok[2], darabok[3])
    snooker.append(d)

#1.feladat
print(f"1. FELADAT:\n\t({len(snooker)})-db játékos van a listán.")


#2. feladat
print("2. FELADAT")
lengyel = False
for i in range(len(snooker)):
    if snooker[i].orszag == "Lengyelország":
        lengyel = True
if lengyel == True:
    print("\tVan Lengyel játékos.")
else:
    print("\tNincs Lengyel játékos.")

#3.feladat
print("3. FELADAT")

#4. feladat
print("4. FELADAT")
masodik = []
for i in range(len(snooker)):
    if snooker[i].helyezes == 2:
        print(f"\t{snooker[i].nev}")

#5. feladat
print("5. FELADAT")
db = 0
orszag = set()
for i in range(len(snooker)):
    orszag.add(snooker[i].orszag)
for i in orszag:
    for k in range(len(snooker)):
        if i == snooker[k].orszag:
            db += snooker[k].eredmeny
    print(f"\t{i}: {db * 480}Ft")