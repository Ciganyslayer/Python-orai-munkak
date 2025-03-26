maxpont = int(input("mennyi a max pontocska?:  "))
osszeg = 0
db = 0
for i in range(100):
    pont = int(input("kövi pontsztám: "))
    if pont == -1:
        break
    else:
        db += 1
        szazalek = pont / maxpont * 100
        if szazalek < 40:
            print("1es lett máma kint alszol")
            osszeg += 1
        elif szazalek < 50:
            print("2es lett kutyam")
            osszeg += 2
        elif szazalek < 60:
            print("3as lett")
            osszeg += 3
        elif szazalek < 80:
            print("4es lett")
            osszeg += 4
        else:
            print("5os lett")
            osszeg += 5
