f = open("musor.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class zene:
    def __init__(self, ado, p, mp, eloado, cim):
        self.ado = int(ado)
        self.p = int(p)
        self.mp = int(mp)
        self.eloado = eloado
        self.cim = cim

zenek = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split()
    cimeloado = ""
    for j in range(3, len(darabok)):
        cimeloado += (darabok[j] + " ")
    szeletek = cimeloado.strip().split(":")

    z = zene(darabok[0], darabok[1], darabok[2], szeletek[0], szeletek[1])
    zenek.append(z)


cs1 = 0
cs2 = 0
cs3 = 0

for i in range(len(zenek)):
    if zenek[i].ado == 1:
        cs1 += 1
    if zenek[i].ado == 2:
        cs2 += 1
    if zenek[i].ado == 3:
        cs3 += 1
print(f"1-es csatorna: {cs1}")
print(f"2-es csatorna: {cs2}")
print(f"3-es csatorna: {cs3}")

for i in range(len(zenek)):
    if zenek[i].ado == 1 and zenek[i].eloado == "Eric Clapton":
        elso = i
        break
for i in reversed(range(len(zenek))):
    if zenek[i].ado == 1 and zenek[i].eloado == "Eric Clapton":
        utolso = i
        break

eltelt = 0
for i in range(elso, utolso + 1):
    if zenek[i].ado == 1:
        eltelt += zenek[i].p * 60 + zenek[i].mp

ora = eltelt // 3600
eltelt = eltelt % 3600
perc = eltelt // 60
mp = eltelt % 60

print(f"A két szám között ({ora}:{perc}:{mp}) telt el")

for i in range(hanyadik, -1, -1):
    if zenek[i].eloado == "Omega" and zenek[i].cim == "Legenda":
        melyik = zenek[i].ado
        hanyadik = i
        break
for i in range(hanyadik, -1, -1):
    if zenek[i].ado != melyik:
        print(f"{zenek[i].eloado} {zenek[i].cim}")
        break
