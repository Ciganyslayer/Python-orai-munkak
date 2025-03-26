import random
csapadekmentes = 0
gyengeso = 0
eso = 0
vihar = 0
for i in range(1, 30 + 1):
    egynap = random.randint(0,20)
    if egynap == 0:
        csapadekmentes += 1
        print(f"{i}: ({egynap} mm); csapadékmentes")
    elif egynap < 6 and egynap > 0:
        gyengeso += 1
        print(f"{i}: ({egynap} mm); gyenge eső")
    elif egynap < 7 and egynap < 11:
        eso += 1
        print(f"{i}: ({egynap} mm); eső")
    elif egynap < 11 and egynap <= 20:
        vihar += 1
        print(f"{i}: ({egynap} mm); vihar")