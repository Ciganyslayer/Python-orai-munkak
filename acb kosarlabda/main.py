f = open("eredmenyek.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()


class eredmeny:
    def __init__(self, hazai, idegen, hazai_pont, idegen_pont, helyszin, idopont):
        self.hazai = hazai
        self.idegen = idegen
        self.hazai_pont = int(hazai_pont)
        self.idegen_pont = int(idegen_pont)
        self.helyszin = helyszin
        self.idopont = idopont


eredmenyek = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    d = eredmeny(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5])
    eredmenyek.append(d)


#1
print("1.")
putamadrid = 0
for i in range(len(eredmenyek)):
    if eredmenyek[i].hazai == "Real Madrid" or eredmenyek[i].idegen == "Real Madrid":
        putamadrid += 1
print(f"\t{putamadrid}-szer jatszott a Real Madrid.")


#2
print("2.")
dontetlen = False
for i in range(len(eredmenyek)):
    if eredmenyek[i].hazai_pont == eredmenyek[i].idegen_pont:
        dontetlen = True
if dontetlen == True:
    print(f"\tVolt dontetlen merkozes.")
else:
    print(f"\tnem volt dontetlen merkozes.")

#3
print("3.")
for i in range(len(eredmenyek)):
    if "Barcelona" in eredmenyek[i].hazai:
        print(f"\tA Barcelona teljes neve: {eredmenyek[i].hazai}")
        break

#4
print("4.")
jasztottak = set()
for i in range(len(eredmenyek)):
    if eredmenyek[i].idopont == "2004-11-21":
        jasztottak.add(eredmenyek[i].hazai and eredmenyek[i].idegen)
print(f"\t{jasztottak}-csapatok jatszottak azon a napon")

#5
print("5.")
stadionok = set()
db = 0
for i in range(len(eredmenyek)):
    stadionok.add(eredmenyek[i].helyszin)
for i in stadionok:
    for k in range(len(eredmenyek)):
        