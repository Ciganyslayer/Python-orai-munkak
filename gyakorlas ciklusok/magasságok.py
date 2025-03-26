max = 0
maxnev = ""
for i in range(100):
    nev = (input("Nev(nem cigány): "))
    magassag = int(input("Magassaga(cm): "))
    if magassag == 0:
        break
    else:
        if magassag > max:
            max = magassag
            maxnev = nev
print(f"a legnagyobb magasság {max} cm")
print(f"a legmagasabb {maxnev}")