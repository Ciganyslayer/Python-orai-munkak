class ember:
    def __init__(self, name, birthdate, sex, height, favcolor, benchpress):
        self.name = name
        self.birthdate = int(birthdate)
        self.sex = sex
        self.height = int(height)
        self.favcolor = favcolor
        self.benchpress = benchpress


kecso = ember("Kecső Máté", 2009, "férfi", 187, "kék", 180)
arki = ember("Árki Davido", 2007,"férfi", 110, "barna", 20)
print(kecso.benchpress)
print(arki.benchpress)

adatok = input("Írd be a az ember adatait: ")
darabok = adatok.split(";")

e = ember(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])

if kecso.benchpress > e.benchpress:
    print("kecső többet benchel")
else:
    print(f"{e.name} többet benchel kecsőnél")
