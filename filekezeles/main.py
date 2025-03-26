f = open("be.txt", "r", encoding= "utf-8")
a = int(f.readline())
b = int(f.readline())

f.close()

osszeg = a + b
f = open("ki.txt", "w", encoding= "utf-8")
print(osszeg, file=f)
f.close()







#paros paratlan szamok
f = open("szamok.txt", "r", encoding= "utf-8")
sor = f.readline()
f.close()
print(sor)

darabok = sor.split()
print(darabok)

szamok = []
for i in range(len(darabok)):
    szamok.append(int(darabok[i]))

paros = open("paros.txt", "w", encoding= "utf-8")
paratlan = open("paratlan.txt", "w", encoding= "utf-8")
for i in range(len(szamok)):
    if szamok[i] % 2 == 0:
        print(szamok[i], file=paros)
    else:
        print(szamok[i], file=paratlan)
paros.close()
paratlan.close()
