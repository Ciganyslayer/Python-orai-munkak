f = open("schumacher.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()


class futam:
    def __init__(self, date, grandprix, position, laps, points, team, status):
        self.date = date
        self.grandprix = grandprix
        self.position = int(position)
        self.laps = int(laps)
        self.points = int(points)
        self.team = team
        self.status = status


futamok = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    d = futam(darabok[0], darabok[1], darabok[2], darabok[3], darabok[4], darabok[5], darabok[6])
    futamok.append(d)


#1.feladat:
print(f"1.feladat: {len(futamok)} információ található a nagydíjról.")


#2.feladat:
motorhiba = 0
for i in range(len(futamok)):
    if futamok[i].status == "Engine":
        motorhiba += 1
print(f"2.feladat: {motorhiba}-szor kellett motorhiba miatt feladni a versenyt")


#3.feladat:
benettonok = []
for i in range(len(futamok)):
    if futamok[i].team == "Benetton":
        benettonok.append(futamok[i].points)
print(f"3.feladat: Benetton színeiben a legtobbet szerzett pont: {max(benettonok)}")


#4.feladat:
csapatok = set()
eredmeny = 0
for i in range(len(futamok)):
    csapatok.add(futamok[i].team)
for i in csapatok:
    for d in range(len(futamok)):
        if i == futamok[d].team and futamok[d].position == 1:
            eredmeny += 1
    print(f"{i}: {eredmeny}")