import random
nums = []

for i in range(60):
    nums.append(random.randint(-90, 70))
print(nums)



for i in range(len(nums)):
    if nums[i] % 6 == 0 or nums[i] % 7 == 0:
        break
print(f"1. feladat: az 1. 6-al vagy 7-el osztható szám ({nums[i]})")



nultizkoz = False
for i in range(len(nums)):
    if nums[i] < 0 and nums[i] > -10:
        nultizkoz = True
        break
if nultizkoz == True:
    print(f"2. feladat: van 0 és -10 közötti szám: ({nums[i]})")
else:
    print("2. feladat: nincs 0 és -10 közötti szám")



mihetvenkisebb = 0
for i in range(len(nums)):
    if nums[i] < -70:
        mihetvenkisebb += 1
print(f"3. feladat: ({mihetvenkisebb}) -70-nél kisebb szám van")



idx = 0
legkisebb = nums[i]
for i in range(len(nums)):
    if nums[i] < legkisebb and nums[i] % 2 == 1:
        legkisebb = nums[i]
        idx = nums[i]
print(f"4. feladat: legkisebb paratlan szam: ({legkisebb}) -indexe: ({i})")



elutkisebb = 0
for i in range(1, len(nums) -1):
    if nums[i] < nums[i - 1] and nums[i] < nums[i + 1]:
        elutkisebb += 1
print(f"5. feladat: ({elutkisebb}) szám van ami kisebb mind a 2 szomszédjánál")
