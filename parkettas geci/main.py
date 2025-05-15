szeles = float(input("Szoba szélessége(m): "))
hosszu = float(input("Szoba hosszúsága(m): "))
doboz = int(input("Hány doboz van: "))

#1.feladat
terulet = szeles * hosszu
print(f"A szoba területe {terulet} négyzetméter.")

van = doboz * 2
if van >= terulet:
    print("Van elég parkettácska.")
else:
    print("Nincs elég parkettácska. Mennyé bótba paraszt.")


#2.feladat
def negativ(szam):
    if szam < 0:
        return True
    else:
        return False

import random
db = 0
for i in range(100):
    d = random.randint(-50, 50)
    if negativ(d) == True:
        db += 1
print(f"A számok között {db} negatív van.")

#3.feladat
