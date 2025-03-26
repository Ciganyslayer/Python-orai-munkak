f = open("vb2018.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()


class stadion:
    def __init__(self, varos, nev1, nev2, ferohely):
        self.varos = varos
        self.nev1 = nev1
        self.nev2 = nev2
        self.ferohely = int(ferohely)

stadionok = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    d = stadion(darabok[0], darabok[1], darabok[2], darabok[3])
    stadionok.append(d)


#1.feladat: Jelenítse meg a képernyôn, hogy hány stadionban játszották a VB mérkőzéseit!
print(f"1. feladat: A stadionok száma: {len(stadionok)}")

#2.feladat: Határozza meg, és írja a képernyőre a legkevesebb férőhellyel rendelkező stadion adatait!
ferohelyek = []
minhely = 0
for i in range(len(stadionok)):
    ferohelyek.append(stadionok[i].ferohely)
minhely = min(ferohelyek)
for i in range(len(stadionok)):
    if stadionok[i].ferohely == minhely:
        print(f"A legkisebb ferohelyu stadion: {stadionok[i].nev1}; {stadionok[i].nev2} --- ferohelye: {minhely}")

#3.Határozza meg és irja ki a képernyôre a stadionok férőhelyszámának átlagát, az eredményt egy tizedesjegyre kerekítve jelenitse meg!
osszeg = sum(ferohelyek)
atlag = osszeg / len(ferohelyek)
print(f"A ferohelyek atlaga: {round(atlag, 1)}")


#4.Számolja meg, hogy hány stadion rendelkezik alternativ névvel! Az eredményt írja a képernyőre!
alternat = 0
for i in range(len(stadionok)):
    if stadionok[i].nev2 != "n.a.":
        alternat += 1
print(f"Az alternativ nevvel rendelkezo stadionok szama: {alternat}")


#5.Kérje be a felhasználótól egy város nevét! Az adatbevitelt mindaddig ismételje, amíg a bevitt név (szöveg) hossza nem éri el a három karaktert!
varos = "aa"
while len(varos) < 3:
    varos = input("Adja meg az egyok varos nevet: ")

#6.Döntse el, hogy az előző feladatban megadott városban zajlottak-e VB mérkőzések! Ha a választ meg tudja adni, akkor ne folytassa a keresést! Az eredményt a képernyőn jelenítse meg! Oldja meg, hogy az összehasonlításnál ne számítsanak a kis- és nagybetük! Ha az előző feladatot nem tudta megoldani, akkor dolgozzon a Szocsi" névvel!
for i in range(len(stadionok)):
    if str(stadionok[i].varos).lower() == varos.lower():
        print(f"Volt vb {stadionok[i].varos}-ban")


#7.Határozza meg és írja a képernyőre, hogy hány különböző városban zajlottak a VB mérkőzései!
kulonbozo = set()
for i in range(len(stadionok)):
    kulonbozo.add(stadionok[i].varos)
print(f"A VB merkozesei ({len(kulonbozo)}) kulonbozo varosban zajlottak")