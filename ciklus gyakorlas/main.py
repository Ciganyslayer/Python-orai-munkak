szam1 = int(input("aggya egy szamot"))

db = 0

for i in range(1, szam1 + 1):
    if szam1 % i == 0:
        db = db + 1
print(db)
if db == 2:
    print("primecske")
else:
    print("nem primszam")
