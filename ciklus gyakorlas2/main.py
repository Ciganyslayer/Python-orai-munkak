osszeg = 0
for i in range(7):
    szam1 = int(input("hany fok van: "))
    osszeg += szam1
    if szam1 < 0:
        print("fagyott")
    else:
        print("nem fagyott")
atlag = osszeg / 7
print(atlag)