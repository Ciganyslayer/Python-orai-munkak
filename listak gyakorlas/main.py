nums = []
import random
for i in range (50):
    nums.append(random.randint(-60, 100))
print(nums)

print("1. feladat")
szorzat = 1
for i in range(len(nums)):
    szorzat *= nums[i]
print(f"    a szamok szorata: {szorzat}")


print("2. feladat")
for i in reversed(range(len(nums))):
    if nums[i] % 5 == 0 or nums[i] % 7 == 0:
        print(f"    az utolsó 5-el vagy 7-el osztható szám indexe: {i}")
        break


print("3. feladat")
for i in reversed(range(len(nums))):
    if nums[i] % 3 == 0 or nums[i] % 7 == 0:
        print(f"    az utolsó 3-al vagy 7-el osztható szám indexe: {i}")
        break


print("4. feladat")
van = False
for i in range(len(nums)):
    if nums[i] >= 0:
        van = True
        break
if van == True:
    print("    van benne pozitív")
else:
    print("    minden szám negatív")


print("5. feladat")
vanet = False
for i in range(len(nums)):
    if nums[i] > 10 and nums[i] > 1:
        vanet = True
        break
if vanet == True:
    print("    van 1 és 10 közötti szám")
else:
    print("    nincs benne 1 és 10 közötti szám")


print("6. feladat")
tizennyolc = 0
for i in range(len(nums)):
    if nums[i] % 18 == 0:
        tizennyolc += 1
print(f"    ({tizennyolc}) 18-al osztható van benne")

print("7. feladat")
mini = 0
legkisebb = nums[i]
for i in range(len(nums)):
    if nums[i] < legkisebb:
        legkisebb = nums[i]
        mini = i
print(f"    a legkisebb szám indexe: {mini}")


print("8. feladat")
for i in range(len(nums)):
    if nums[i] % 17 == 0 or nums[i] % 18 == 0:
        print(nums[i] * nums[i])


print("9. feladat")
vanneg = False
for i in range(1, len(nums) - 1):
    if nums[i] < 0 and nums[i - 1] > 0 and nums[i + 1] > 0:
        vanneg = True
        break
if vanneg == True:
    print("van olyan negativ szam aminek a szomszédjai pozitivak")
else:
    print("nincs olyan negativ szam aminek a szomszédjai pozitivak")


print("10. feladat")
novekvo = True
for i in range(len(nums) - 1):
    if nums[i] > nums[i + 1]:
        novekvo = False
        break


