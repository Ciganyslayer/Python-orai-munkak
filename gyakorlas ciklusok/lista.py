gyumolcsok = ["almalex", "szilvalex", "körtelex", "barackalex"]
print(gyumolcsok)

gyumolcsok.append("szőlőalex")
print(gyumolcsok)
print(gyumolcsok[0]) #lista 1. eleme
print(gyumolcsok[1]) #2. eleme
print(gyumolcsok[-1]) #lista utolsó eleme
print(gyumolcsok[1:4]) #lista 2-4 eleme

gyumolcsok.append(5) #bármi mehet bele
gyumolcsok.append(12) #bármi mehet bele
print(gyumolcsok)






import random
szamok = [] # üres lista
for i in range(50):
    szamok.append(random.randint(1,100))
print(szamok)
otoszto = 0
db = 0
for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        db += 1
    if szamok[i] % 5 == 0:
        otoszto += 1
print(f"({db}) db páros")
print(f"({otoszto}) 5-el osztható van")
i = 0
while i < len(szamok) and szamok[i] % 5 != 0:
    i += 1
if i < len(szamok):
    print("van benne 5-el osztható")
else:
    print("nincs benne 5-el osztható")

van = False
for i in range(len(szamok)):
    if szamok [i] % 5 == 0:
        van = True
        break
if van == True:
    print("Van benne 5-el osztható")
else:
    print("Nincs benne 5-el osztható")






max = 0
maxi = 0
for i in range(len(szamok)):
    if szamok[i] > max:
        max = szamok[i]
        maxi = i
print(f"legnagyobb szám: {max}")
print(f"a sorszáma: {maxi + 1}")








osszeg = 0
for i in range(len(szamok)):
    osszeg += szamok[i]
atlag = osszeg / len(szamok)
print(f"({atlag}) az atlag")