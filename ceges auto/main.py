f = open("autok.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class mozgas:
    def __init__(self, nap, ido, rendszam, azonosito, kmszamlalo, beki):
        self.nap = int(nap)
        self.ido = ido
        self.rendszam = rendszam
        self.azonosito = int(azonosito)
        self.kmszamlalo = int(kmszamlalo)
        self.beki = int(beki)

mozgasok = []
for i in range(len(lines)):
    darabok = lines[i].strip().split()
    m = mozgas(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    mozgasok.append(m)

for i in reversed(range(len(mozgasok))):
    if mozgasok[i].beki == 0:
        print(f"{mozgasok[i].nap}. nap rendszám {mozgasok[i].rendszam}")
        break

benap = int(input("Írja be egy nap számát: "))
print(f"Forgalom a {benap}. napon: ")
for i in range(len(mozgasok)):
    if mozgasok[i].nap == benap:
        print(f"{mozgasok[i].ido} {mozgasok[i].rendszam} {mozgasok[i].azonosito} {mozgasok[i].beki}")