import random
db1 = 0
db2 = 0
db3 = 0
db4 = 0
db5 = 0
db6 = 0
for i in range(300):
    dobas = random.randint(1,6)
    if dobas == 1:
        db1 += 1
    if dobas == 2:
        db2 += 1
    if dobas == 3:
        db3 += 1
    if dobas == 4:
        db4 += 1
    if dobas == 5:
        db5 += 1
    if dobas == 6:
        db6 += 1

print(f"1-est dobtal {db1}-szer")
print(f"2-est dobtal {db2}-szer")
print(f"3-est dobtal {db3}-szer")
print(f"4-est dobtal {db4}-szer")
print(f"5-est dobtal {db5}-szer")
print(f"6-est dobtal {db6}-szer")
