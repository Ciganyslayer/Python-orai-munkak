import random
sebhatar = int(input("mennyi a sebességhatár (km/h): "))
gyorshajto = 0
leggyorsabb = 0
for i in range(200):
    sebesseg = int(input("mennyi az auto sebessége"))
    if sebesseg == 0:
        break
    else:
        if sebesseg > sebhatar:
            gyorshajto += 1
        if sebesseg > leggyorsabb:
            leggyorsabb = sebesseg
print(f"a gyorhajtok szama {gyorshajto}")
print(f"a leggyorsabb {leggyorsabb} km/h, {leggyorsabb - sebhatar}- al lepte at")
