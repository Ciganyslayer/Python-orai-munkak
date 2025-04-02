f = open("konyvek.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class konyv:
    def __init__(self, nev, szulEv, halEv, nemzetiseg, cim, helyezes):
        self.nev = nev
        self.szulEv = int(szulEv)
        self.halEv = halEv
        self.nemzetiseg = nemzetiseg
        self.cim = cim
        self.helyezes = int(helyezes)

konyvek = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    if darabok[2] == "":
        darabok[2] = 2005
    d = konyv(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    konyvek.append(d)
#1
print(f"1.feladat:\t{len(konyvek)}-db könyv szerepel az állományban.")

#2
helyezesek = []
for i in range(len(konyvek)):
    helyezesek.append(konyvek[i].helyezes)
minhely = min(helyezesek)
for i in range(len(konyvek)):
    if konyvek[i].helyezes == minhely:
        print(f"2.feladat:\ta legjobb elert helyezes adatai: {konyvek[i].nev}: {konyvek[i].cim}")

#3
nemetcigany = False
for i in range(len(konyvek)):
    if konyvek[i].nemzetiseg == "német":
        nemetcigany = True
if nemetcigany == True:
    print("3.feladat:\tszerepel német író a listában")
else:
    print("3.feladat:\tnem szerepel német író a listában")

#4
kilencvenidos = []
for i in range(len(konyvek)):
    eletkor = darabok[2] - darabok[1]
    if eletkor >= 90:
        kilencvenidos.append(konyvek[i].nev)
print(kilencvenidos)
