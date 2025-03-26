print ("szialex")

felh = int(input("valassza vmit kocsog! (1)kavics (2)szalvéta (3)körfűrész:"))
if felh == 1:
    print("kavicsot valasztottad")
if felh == 2:
    print("szalvétát valasztottad")
if felh == 3:
    print("körfűrészt valasztottad")

import random
szg = random.randint(1,3)
if szg == 1:
    print("kavicsot valasztotta a mesterseges inteligencia")
if szg == 2:
    print("szalvétát valasztotta a mesterseges inteligencia")
if szg == 3:
    print("körfűrészt valasztotta a mesterseges inteligencia")


if felh == szg:
    print("draw")
elif felh == 1 and szg == 3:
    print("winneltel!!!")
elif felh == 2 and szg == 1:
    print("winneltel!!!")
elif felh == 3 and szg == 2:
    print("winneltel!!!")

else:
    print("loseoltal!")

