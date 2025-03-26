#sziper szuper file kiolvasás dogalex b csoportalexe
f = open("be.txt", "r", encoding="utf-8")
sorok = f.readlines()
f.close()

szamok = []
for i in range(len(sorok)):
    szamok.append(int(sorok[i]))
print(szamok)

print("1. feladat")
harmincnagy = 0
for i in range(len(sorok)):
    if szamok[i] > 30:
        harmincnagy += 1
print(f"({harmincnagy}) 30-nál nagyobb szám van")

print("2. feladat")
pozi = 0
kiltiotoszt = ()
for i in range(len(sorok)):
    if szamok[i] % 9 == 0 or szamok[i] % 15 == 0:
        kiltiotoszt = szamok[i]
        pozi = i + 1
print(f"Az utolsó 9-cel vagy 15-tel osztható szám: ({kiltiotoszt}) indexe: ({pozi}) ")

print("3. feladat")
szorzat = 1
for i in range(len(sorok)):
    szorzat *= szamok[i]
fele = szorzat / 2
print(f"A sorozatban található számok szorzatának a fele: ({fele})")

print("4. feladat")
kismitiz = []
for i in range(len(sorok)):
    if szamok[i] < -10:
        kismitiz.append(szamok[i])
print(f"({max(kismitiz)}) legnagyobb szám a -10-nél kisebbek közül")

print("5. feladat")
paros = []
for i in range(len(sorok)):
    if szamok[i] % 2 == 0:
        paros.append(szamok[i] * 2)
f = open("alex listaja.txt", "w", encoding="utf-8")
for i in range(len(paros)):
    print(paros[i], file=f)
print(f"A sorozat páros tagjainak a kétszerese: {paros}")

