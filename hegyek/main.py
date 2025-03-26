f = open("hegyekMo.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

print(lines)

class hegy:
    def __init__(self, hegycs, hegyseg, magassag):
        self.hegycs = hegycs
        self.hegyseg = hegyseg
        self.magassag = magassag

hegyek = []
for i in range(len(lines)):
    darabok = lines[i].strip().split(";")
    h = hegy(darabok[0], darabok[1], darabok[2])
    hegyek.append(h)

print(hegyek)
print(f"3. feladat: hegycsúcsok száma: ({len(hegyek)}) db")

osszeg = 0
for i in range(len(hegyek)):
    osszeg += hegyek[i].magassag

atlag = osszeg / len(hegyek)
print(f"4. feladat: Hegycsúcsok átlagos magassága: ({atlag}) m")

max = 0
maxi = 0
for i in range(len(hegyek)):
    if hegyek[i].magassag > max:
        maxi = i

print("5. feladat: Legmagasabb hegycsúcs adatai: ")
print(f"\tNév: {hegyek[maxi].hegycs}")
print(f"\tHegység: {hegyek[maxi].hegyseg}")
print(f"\tMagasság: {hegyek[maxi].magassag}")

bemagas = int(input("Kűrek egy magasságot: "))
van = False
for i in range(len(hegyek)):
    if hegyek[i].hegyseg == "Börzsöny" and hegyek[i].magassag > bemagas:
        van = True

if van == True:
    print(f"Van {bemagas} méternél magasabb hegy a Börzsönyben.")
else:
    print(f"Nincs {bemagas} méternél magasabb hegy a Börzsönyben.")
