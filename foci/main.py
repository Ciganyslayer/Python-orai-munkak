f = open("meccs.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class merkozes:
    def __init__(self, ford, hg, vg, hfg, vfg, hazai, vendeg):
        self.ford = int(ford)
        self.hg = int(hg)
        self.vg = int(vg)
        self.hfg = int(hfg)
        self.vfg = int(vfg)
        self. hazai = hazai
        self.vendeg = vendeg

merkozesek = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split()
    m = merkozes(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6])
    merkozesek.append(m)

beford = int(input("Írja be a forduló számát: "))

for i in range(len(merkozesek)):
    if merkozesek[i].hazai == beford:
        print(f"{merkozesek[i].hazai}-{merkozesek[i].vendeg}: {merkozesek[i].hg}-{merkozesek[i].vg} ({merkozesek[i].hfg}-{merkozesek[i].vfg})")

for i in range(len(merkozesek)):
    if merkozesek[i].hg > merkozesek[i].vg and merkozesek[i].hfg < merkozesek[i].vfg:
        print(f"{merkozesek[i].hazai} {merkozesek[i].ford}")
    if merkozesek[i].hg < merkozesek[i].vg and merkozesek[i].hfg > merkozesek[i].vfg:
        print(f"{merkozesek[i].vendeg} {merkozesek[i].ford}")


csapat = ("írja be a csapat nevét: ")
lott = 0
kapott = 0
for i in range(len(merkozesek)):
    if merkozesek[i].hazai == csapat:
        lott += merkozesek[i].hg
        kapott += merkozesek[i].vg
    else:
        lott += merkozesek[i].vg
        kapott += merkozesek[i].hg
print(f"Lőtt: {lott}")
print(f"kapott: {kapott}")

volt = False
for i in range(len(merkozesek)):
    if merkozesek[i].hazai == csapat and merkozesek[i].hg < merkozesek[i].vg:
        print(f"A csapat először a {merkozesek[i].vendeg}-tól kapott ki.")
        volt = True
        break
if volt == False:
    print("A csapat otthon veretlen marad")

eredmenyek = set()
eredmenylist = []
for i in range(len(merkozesek)):
    if merkozesek[i].hg > merkozesek[i].vg:
        e = str(merkozesek[i].hg) + "-" + str(merkozesek[i].vg)
        eredmenyek.add(e)
    else:
        e = str(merkozesek[i].vg) + "-" + str(merkozesek[i].hg)
        eredmenyek.add(e)
        eredmenylist.append(e)
print(eredmenyek)
print(eredmenylist)

f = open("stat.txt", "w", encoding="utf-8")
for e in eredmenyek:
    db = 0
    for i in range(len(eredmenylist)):
        if eredmenylist[i] == e:
            db += 1
    print(f"{e}: {db} darab", file = f)
f.close()