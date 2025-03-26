import random

def sorsolas():
    return random.sample(range(1, 91), 5)

def bekeres():
    print("Add meg az 5 számodat 1 és 90 között!")
    felhasznalo_szamok = []
    while len(felhasznalo_szamok) < 5:
        try:
            szam = int(input(f"{len(felhasznalo_szamok) + 1}. szám: "))
            if szam < 1 or szam > 90:
                print("A számnak 1 és 90 között kell lennie!")
            elif szam in felhasznalo_szamok:
                print("Már megadtad ezt a számot, válassz másikat!")
            else:
                felhasznalo_szamok.append(szam)
        except ValueError:
            print("Kérlek, egy egész számot adj meg!")
    return felhasznalo_szamok

def talalatok(sorsolt_szamok, felhasznalo_szamok):
    return set(sorsolt_szamok) & set(felhasznalo_szamok)

def nyeremeny(talalatok_szama):
    nyeremeny_lista = {
        5: "Jackpot!",
        4: "Nagyon nagy nyeremény!",
        3: "Közepes nyeremény!",
        2: "Kisebb nyeremény!",
        1: "Vigaszdíj!",
        0: "Sajnos nem nyertél."
    }
    return nyeremeny_lista.get(talalatok_szama, "Ismeretlen nyeremény")

def main():
    print("Üdvözlünk a lottójátékban!")

    # Sorsolás
    sorsolt_szamok = sorsolas()
    print("A számok kisorsolva! Játssz velünk!")

    # Felhasználói számok bekérése
    felhasznalo_szamok = bekeres()

    # Találatok meghatározása
    talalatok_set = talalatok(sorsolt_szamok, felhasznalo_szamok)
    talalatok_szama = len(talalatok_set)

    # Eredmények kiírása
    print("\nA sorsolt számok: ", sorsolt_szamok)
    print("A te számaid: ", felhasznalo_szamok)
    print(f"Találatok száma: {talalatok_szama}")
    print(f"Nyeremény: {nyeremeny(talalatok_szama)}")

if __name__ == "__main__":
    main()
