a = float(input("Írja be az (A) egyűtthatót:"))
b = float(input("Írja be az (B) egyűtthatót:"))
c = float(input("Írja be az (C) egyűtthatót:"))

import math

disz = b * b - 4 * a * c
if disz < 0:
    print("Az egyenletnek nincs valós gyöke.")
elif disz == 0:
    print("Az egyenletnek egy valós gyöke van.")
    x = -b / (2 * a)
    print(f"x = {x}")
else:
    print("Az egyenletnek két valós gyöke van.")
    x1 = (-b + math.sqrt(disz)) / (2 * a)
    x2 = (-b - math.sqrt(disz)) / (2 * a)
print(f"x1 = {x1}")
print(f"x2 = {x2}")