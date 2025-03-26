print("gondokszójjá egy szamra 1 es 1000 kodzött: ")
e = 1
u = 1000
k = (e + u) // 2
for i in range(1000):
    valasz = input(f"a cám a {k}? (i/n)")
    if valasz == "i":
        print("megvan")
        break
    else:
        valasz = input(f"a szam nagyobb mint {k}? (i/n)")
        if valasz == "i":
            e = k + 1
        else:
            u = k - 1
        k = (e + u) // 2