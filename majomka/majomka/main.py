km = int(input("mennyit akarol menni?:"))
tank = int(input("mekkora a tank:"))
fogy = int(input("mennyit eszik:"))
maxkm = tank / fogy * 100
if maxkm > km:
    print("nem rohad le")
else:
    print("lerohad")


szelesseg = int(input("mekkora a szelesseg:"))
magassag = int(input("mekkora a magassag:"))
dobozszam = int(input("dobozunk van:"))
doboz = int(input("hany m2 re eleg 1szutyok:"))
szoba = szelesseg * magassag
if szoba <= doboz * dobozszam:
    print("gratula")
else:
    print("vegyel meg")

