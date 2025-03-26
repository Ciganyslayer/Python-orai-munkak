#Készíts programot, amely meghatározza a legszélesebb sziget bal-, illetve jobboldali partját!
#Készíts programot, amely meghatározza, hogy van-e két egyforma nagyságú sziget!
#Készíts programot, amely meghatározza azt a szigetet, amely a legközelebb van az óceán közepéhez!
#Készíts programot, amely meghatározza az egymáshoz legközelebb levő két szigetet!
#Készíts programot, amely meghatározza a legmeredekebb hegyet tartalmazó sziget két partját!
#Készíts programot, amely meghatározza a legmélyebb völgyet tartalmazó sziget két partját!
#Készíts programot, amely meghatározza az 200 méternél magasabb szigetek átlagos magasságát!
#Készíts programot, amely meghatározza, hogy a szigetek átlagmagassága növekszik-e!
#Készíts programot, amely meghatározza a tengerszakaszok átlagos hosszát!
#Készíts programot, amely meghatározza, hogy melyik sziget van legtávolabb a többi szigettől!
#Készíts programot, amely meghatározza a völgyet tartalmazó szigetek számát!
#Készíts programot, amely meghatározza a tengerszakaszok átlagos hosszát!
#Készíts programot, amely meghatározza a szárazföldön levő hegycsúcsok átlagos magasságát!
#Készíts programot, amely meghatározza a legmagasabb hegycsúcsot tartalmazó sziget bal-, illetve jobboldali partját!
#Készíts programot, amely meghatározza a 100 méternél alacsonyabb szigetek átlagos magasságát!
#Készíts programot, amely meghatározza, hogy az út során a szigetek egyre kisebbek lettek-e!

f = open("sziget.txt", "r", encoding="utf-8" )
sorok = f.readlines()
f.close()
print(sorok)

meresek = []
for i in range(len(sorok)):
    meresek.append(int(sorok[i].strip()))
print(meresek)