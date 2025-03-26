import random
xhideg = 0
elviselheto = 0
xmeleg = 0
legmagasabb = 0
szamok = 0

for i in range(1,150 + 1):
    meres = random.randint(-200, 3000)
    szamok += meres
    if meres >= -200 and meres < -51:
        xhideg += 1
        print(f"{i}: ({meres} fok)- extrém hideg")
    elif meres > -50 and meres < 81:
        elviselheto += 1
        print(f"{i}: ({meres} fok)- elviselhető")
    elif meres > 80:
        xmeleg += 1
        print(f"{i}: ({meres} fok)- extrém meleg")
    if meres > legmagasabb:
        legmagasabb = meres

atlag = szamok // 150
print(f"      {legmagasabb}-fok a legmagasabb mért fok")
print(f"      {atlag}- az átlaguk")
