#"Napkeleti bölcsek munkája": Árki Dávid--Tren twin; Kovács kapitány; Kis Marcipán--Alex csicskája

import random
nyeroszamok = []
while len(nyeroszamok) < 5:
    szam = random.randint(1, 90)
    if szam not in nyeroszamok:
        nyeroszamok.append(szam)



tipszmix = []
print("X-eljél be 5 számot a szelvényen! Nyilván 1- és 90 közzött legyenek!")
while len(tipszmix) < 5:
    tippek = input(f"Tippeld meg az {len(tipszmix) + 1}. számot (Úgyse fogsz nyerni!!!): ")
    if not tippek.isdigit():
        print("Elkúrtuk!! A lottón csak számok vannak!")
        continue
    szam = int(tippek)
    if szam < 1 or szam > 90:
        print("Elkúrtuk!! Csak 1- és 90 között vannak számok a szelvényen!")
    elif szam in tipszmix:
        print("Elkúrtuk!! Nem tudod 2-ször ugyan azt x-elni!")
    else:
        tipszmix.append(szam)


print(f"A tippelt számaid:{tipszmix}")
print(f"A nyerő számok:{nyeroszamok}")


talalatok = 0
for szam in tipszmix:
    if szam in nyeroszamok:
        talalatok += 1
print(f"Találatok száma:{talalatok}")


if talalatok == 5:
    print("Beszarás!!! Költözünk az országból!")
elif talalatok == 4:
    print("Mámma eszünk!")
elif talalatok == 3:
    print("Egyszer van karácsony!")
elif talalatok == 2:
    print("Legalább nem döglök éhen!")
elif talalatok == 1:
    print("Jackpot!!!")
else:
    print("Tipikus magyar szerencsejáték!")