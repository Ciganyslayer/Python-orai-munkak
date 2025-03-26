#én lenni búrkoló

szelesseg = int(input("add meg a szélességet m-ben: "))
hosszusag = int(input("add meg a hosszúságot m-ben:"))
csempeszam = int(input("add meg a sempék számát"))

csempe = 0.2 * 2
fal = szelesseg * hosszusag / csempe
print(f"{fal} csempe kell")
if fal <= csempeszam:
    print("nem kell menni boltba")
else:
    print("mennyé bótba")
