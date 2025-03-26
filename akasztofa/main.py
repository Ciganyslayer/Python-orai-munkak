f = open("szavak.txt", "r", encoding="utf-8")
lines = f.readlines()
f.close()

stages = [
    """
    +---+
    |   |
        |
        |
        |
        |
=========
    """,
    """
    +---+
    |   |
    O   |
        |
        |
        |
=========
    """,
    """
    +---+
    |   |
    O   |
    |   |
        |
        |
=========
    """,
    """
    +---+
    |   |
    O   |
   /|   |
        |
        |
=========
    """,
    """
    +---+
    |   |
    O   |
   /|\  |
        |
        |
=========
    """,
    """
    +---+
    |   |
    O   |
   /|\ |
   /    |
        |
=========
    """,
    """
    +---+
    |   |
    O   |
   /|\ |
   / \ |
        |
=========
    """
]


import random
melyik = random.randint(0, len(lines) -1)
feladvany = lines[melyik]

tipp = "_" * len(feladvany)
level = 0
while True:
    print(f"A tippelt szó: {tipp}")
    print(stages[level])
    betu = input("Írj be egy betűt!: ").lower()
    if feladvany.find(betu) > -1:
        elozo = tipp
        tipp = ""
        for i in range(len(feladvany)):
            if feladvany[i] == betu:
                tipp += betu
            else:
                tipp += elozo[i]
    else:
        level += 1

    if level == 6:
        print("Megdöglöttél!!!")
        print(stages[level])
        print(f"A szó a {feladvany} volt.")
        break
    if tipp == feladvany:
        print("Kitaláltad (TE PANCSER)")



