szam = int(input(f"aggyá szamot:"))
if szam > 0:
    print("a szam pozitiv")
elif szam < 0:
    print("a szam negativ")
else:
    print("a szam nulla")
szam1 = input(f"aggya szemot te:")
szam2 = input(f"aggya meg egyet:")
if szam2 < szam1:
    print("szam1 nagyobb")
elif szam1 < szam2:
    print("szam2 nagyobb")
else:
    print(" egyenlo")
aoldal = input(f"egy oldal")
print("aggyal egy oldalt")
boldal = input(f"masodik oldal")
print("adjal masodik oldalt")
coldal = input(f"harmadik oldal")
print("adjL harmadiko oldalt")
if aoldal + boldal > coldal and aoldal + coldal > boldal and boldal + coldal > aoldal:
    print("mukodik")
else:
    print("meghalt")
evszam = int(input("aggya egy evszamot"))
if evszam % 4 == 0 and evszam % 100 != 0:
    print(f"{evszam}:szokoevecske")
elif evszam % 400 == 0:
    print("szokoev")
else:
    print("ez nm szokoev")
time = int(input("mennyi az ido"))
print("mennyi az ido")
if time >= 6 and time <= 10:
    print("gyó reggölt")
if time >= 11 and time <= 17:
    print("gyó napokat")
if time >= 18 and time <= 22:
    print("gyó esitket")
if time >= 23 and time <= 24 and time >= 0 and time <= 5:
    print("gyó ejcakatt")
doga = int(input("mennyi az elert pontszam:"))
szazalek = doga / 50 * 100
if szazalek >= 40  and szazalek <= 49:
    print("2")
if szazalek >= 50  and szazalek <= 59:
    print("3")
if szazalek >= 60  and szazalek <= 69:
    print("4")
if szazalek >= 80:
    print("5")


