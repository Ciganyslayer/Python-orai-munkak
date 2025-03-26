tabla = []
for i in range(10):
    sor = []
    for j in range(10):
        sor.append(" ")
    tabla.append(sor)
print(tabla)

jatekos = "X"

while True:
    print("  0  1  2  3  4  5  6  7  8  9")
    for i in range(10):
        print(i, end="")
        for j in range(10):
            print(f"[{tabla[i][j]}]", end="")
        print()

    print(f"{jatekos}- következik!")
    print("Hová szeretnél billegni?")

    sor = int(input("Sor: "))
    oszlop = int(input("Oszlop: "))

    if tabla[sor][oszlop] == " ":
        tabla[sor][oszlop] = jatekos
        db =0
        max = 0
        for j in range(10):
            if tabla[sor][j] == jatekos:
                db += 1
            else:
                if db > max:
                    max = db
                    db = 0

        for i in range(10):
            if tabla[sor][i] == jatekos:
                db += 1
            else:
                if db > max:
                    max = db
                    db = 0

        if max == 5:
            print(f"{jatekos} gyűzütt!!!")
            break


        if jatekos == "X":
            jatekos = "O"
        else:
            jatekos = "X"
    else:
        print("Oda nem léphetsz fasz!")
