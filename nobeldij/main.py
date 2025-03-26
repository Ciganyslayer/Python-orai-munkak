f = open("nobel.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

class dij:
    def __init__(self, ev, tipus, keresztnev, vezeteknev):
        self.ev = int(ev)
        self.tipus = tipus
        self.keresztnev = keresztnev
        self.vezeteknev = vezeteknev

dijak = []
for i in range(1, len(lines)):
    darabok = lines[i].strip().split(";")
    d = dij(darabok[0], darabok[1], darabok[2], darabok[3])
    dijak.append(d)

for i in range(len(dijak)):
    if dijak[i].keresztnev == "Arthur B." and dijak[i].vezeteknev == "McDonald":
        print(f"3. feladat: {dijak[i].tipus}")
        break

for i in range(len(dijak)):
    if dijak[i].ev == 2017 and dijak[i].tipus == "irodalmi":
        print(f"4. feladat: {dijak[i].keresztnev} {dijak[i].vezeteknev}")
        break

print("5. feladat:")
for i in range(len(dijak)):
    if dijak[i].vezeteknev == "" and dijak[i].ev >= 1990:
        print(f"\t{dijak[i].ev}: {dijak[i].keresztnev}")

print("6. feladat:")
for i in range(len(dijak)):
    if dijak[i].vezeteknev.count("Curie") > 0:
        print(f"\t{dijak[i].ev}: {dijak[i].keresztnev} {dijak[i].vezeteknev} ({dijak[i].tipus})")

kategoriak = set()
for i in range(len(dijak)):
    kategoriak.add(dijak[i].tipus)
print(kategoriak)

for k in kategoriak:
    db = 0
    for i in range(len(dijak)):
        if dijak[i].tipus == k:
            db += 1
    print(f"{k} {db} db")