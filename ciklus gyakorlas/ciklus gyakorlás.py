szam1 = int(input("aggya szamot"))
osszeg = 1
for i in range(10):
    osszeg *= szam1
print(osszeg)
fakt = 1
for i in range(1, szam1 + 1):
    fakt *= i
print(f"{szam1}! = {fakt}")


n = int(input("aggya szamot"))
for i in range(1,n + 1):
    print(i * i)