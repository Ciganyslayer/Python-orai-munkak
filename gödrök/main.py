f = open("melyseg.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

godor = []
for i in range(len(lines)):
    godor.append(int(lines[i]))

print(f"A fájl adatainak száma: {len(godor)}")

tav = int(input("Adjon meg egy távolságértéket!"))
