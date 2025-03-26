f = open("berek2020.txt", "r", encoding="utf-8")
lines = f.readlines()

class dolgozo:
    def __init__(self, nev, nem, reszleg, belepes, ber):
        self.nev = nev
        self.nem = nem
        self.reszleg = reszleg
        self.belepes = int(belepes)
        self.ber = int(ber)

dolgozok = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    d = dolgozo(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4])
    dolgozok.append(d)

print(f"3. feladat: Dolgozók száma: ({len(dolgozok)})")

osszeg = 0
for i in range(len(dolgozok)):
    osszeg += dolgozok[i].ber
atlag = round(osszeg / len(dolgozok) / 1000, 1)
print(f"Az átlagfizu ({atlag})-E Ft")

beszerleg = input("4. feladat: Adja meg egy részleg nevét: ")

max = 0
maxi = 0
for i in range(len(dolgozok)):
    if dolgozok[i].ber > max:
        max = dolgozok[i].ber
        maxi = i

if max == 0:
    print("Nincs ilyen nevű részleg")
else:
    print("A legtöbbet kereső dolgozó a részlegen: ")
    print(f"\tNév: {dolgozok[maxi].nev}")
    print(f"\tNeme: {dolgozok[maxi].nem}")
    print(f"\tBelépés: {dolgozok[maxi].belepes}")
    print(f"\tBér: {dolgozok[maxi].ber}")

reszlegek = set()
for i in range(len(dolgozok)):
    reszlegek.add(dolgozok[i].reszleg)

for r in reszlegek:
    db = 0
    for i in range(len(dolgozok)):
        if dolgozok[i].reszleg == r:
            db += 1
    print(f"\t{r}: {db} fő")

f = open("asztalos.txt", "w", encoding="utf-8")