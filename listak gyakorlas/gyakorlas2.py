nums = []
import random
for i in range (40):
    nums.append(random.randint(-50, 80))
print(nums)



osszeg = 0
for i in range(len(nums)):
    osszeg += nums[i]
atlag = osszeg / len(nums)
print(f"1.feladat--a számok átlaga: ({atlag})")



for i in reversed(range(len(nums))):
    if nums[i] % 5 == 0 and nums[i] % 9 == 0:
        print(f"2. feladat--utolsó 5-el és 9-el osztható számok indxe: ({i})")
        break



for i in range(len(nums)):
    if nums[i] % 2 == 0 or nums[i] % 7 == 0:
        print(f"3. feladat--első 2-vel és 7-tel osztható szám: ({nums[i]})")
        break



mindparos = True
for i in range(len(nums)):
    if nums[i] % 2 == 1:
        mindparos = False
        break
if mindparos == True:
    print("4. feladat: mindegyik páros")
else:
    print("4. feladat: nem mindegyik páros")



hetvennagy = False
for i in range(len(nums)):
    if nums[i] > 70:
        hetvennagy = True
        break
if hetvennagy == True:
    print(f"5. feladat: van 70-nél nagyobb szám : ({nums[i]})")
else:
    print("5. feladat: nincs 70-nél nagyobb szám")



db = 0
for i in range(len(nums)):
    if nums[i] < 0:
        db += 1
print(f"6. feladat: ({db}) negatív szám van")



negyoszthato =