import random
fej = 0
iras = 0
streak = 0
max = 0
for i in range(200):
    dobas = random.randint(1,2)
    if dobas == 1:
        fej += 1
    if dobas == 2:
        iras += 1
    if dobas == 1:
        fej += 1
        streak += 1
    else:
        iras += 1
        if streak > max:
            max = streak
print(f"max fej streak = {max}")
print(f"Fejet dobtál {fej}")
print(f"Írást dobtál {iras}")