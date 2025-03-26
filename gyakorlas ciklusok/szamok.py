import random
paros = 0
paratlan = 0
otoszthato = 0
legkisebb = 0
for i in range(500):
    szamok = random.randint(1,10000)
    if szamok % 2 == 0:
        paros += 1
        print(f"{szamok}: paros")

    else:
        paratlan += 1
        print(f"{szamok}: paratlan")

    if szamok % 5 == 0:
        otoszthato += 1
        print(f"{szamok}: oszthato 5-el")

    if szamok % 5 == 0 and szamok % 2 == 0:
        otoszthato += 1
        paros += 1
        print(f"{szamok}: 5-el és 2-vel is osztható")

    if szamok < legkisebb:
        szamok = legkisebb
        print(f"{legkisebb} a legkisebb")