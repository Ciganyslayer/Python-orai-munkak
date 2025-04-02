#1.feladat
ar = int(input("Aggyad a cucc árát more!!!: "))
arf = float(input("Aggyad az euro arfolyamat: "))
euro = float(input("Mennyi eurod van cigger: "))

forint = euro * arf
if forint >= ar:
    print(f"{forint}- pézed van-e heee---Mehet a buy!!!")
else:
    print("{forint}Ft pézed van-e heee---Csóró magyar vagy te még ehhez!!!")


#2.feladat
def oszthato(szam):
    if szam % 7 == 0 and szam % 3 != 0:
        return True
    else:
        return False

osszeg = 0
db = 0
for i in range(100,1000):
    if oszthato(i) == True:
        db += 1
        osszeg += i
atlag = osszeg / db
print(f"A 7-el oszható és 3-al nem osztható számok átlaga: {atlag}")




#3.feladat
f = open("konyvek.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class konyv:
    def __init__(self, nev, szulEv, halEv, nemzetiseg, cim, helyezes):
        self.nev = nev
        self.szulEv = int(szulEv)
        self.halEv = int(halEv)
        self.nemzetiseg = nemzetiseg
        self.cim = cim
        self.helyes = int(helyezes)

konyvek = []
for i in range(1, len(lines)):
    darabok = lines[i].srtip.split(";")
    d = konyv(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    konyvek.append(d)

print(f"1.feladat: \t{len(konyvek)}-db könyv szerepel az állományban.")
