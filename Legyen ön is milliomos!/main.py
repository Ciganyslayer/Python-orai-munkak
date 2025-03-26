#"LEGYEN ÖN IS MILLIOMOS"---Pácsatron Alexinátor; Kovács Kapitány; Kis Marcella-aki nem elfogadható magatartást gyakorol az angol órák során
print("LEGYEN ÖN IS MILLIOMOS!")
print("Játékszabály:")
print(f"\t         #A játékosnak 10 kérdésre kell helyesen válaszolnia, hogy elérje a főnyereményt.")
print(f"\t         #A játékosnak az alábbi lehetséges válaszok közül kell választania, amiket A, B, C, vagy D betű beírásával tud megtenni. A kérdések közül mindig csak egy a helyes válasz.")
print(f"\t         #A játékos minden teljesített kérdés után kap +1 pontot (1.000.000 Ft) és eldöntheti, hogy kiszáll-e (stop parancs beírásával) (elviszi az addigi money-t) vagy folytatja a játékot a következö szintre.")
print(f"\t         #Amennyiben a játékos úgy dönt hogy folytatja a játékot és (ha) elveszíti a következő szinet, azzal elveszíti az addig szerzett pénzösszeget is.")
print(f"\t         #A játékos kérhet a játék során (1db!!!) hintet egy telefonhíváson keresztül az alábbi számot hívva:06 30 484 7308")

scoreboard = 0
while True:
    elso = input("1. Ki írta a Rómeó és Júlia című művet? a) Charles Dickens, b) William Shakespeare, c) Jane Austen, d) Mark Twain:")
    if elso == "stop":
        print(f"A játékot befejezted! Nyereményed: {scoreboard *1000000}")
        break
    if elso == "06304847308":
        print("Villám McQueen shake")
        continue
    if elso == "a" or elso == "c" or elso == "c":
        print("Helytelen válasz! A játék véget ért számodra!")
        exit()
    if elso == "b":
        print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
        scoreboard += 1
        print(f"A pézzzed: {scoreboard * 1000000}-Ft")


        masodik = input("2. Melyik bolygót ismerjük Vörös Bolygó néven? a) Vénusz, b) Mars, c) Jupiter, d) Szaturnusz:")
        if masodik == "stop":
            print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
            break
        if masodik == "06304847308":
            print("Csoki")
            continue
        if masodik == "a" or masodik == "c" or masodik == "c":
            print("Helytelen válasz! A játék véget ért számodra!")
            exit()
        if masodik == "b":
            print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
            scoreboard += 1
            print(f"A pézzzed: {scoreboard * 1000000}-Ft")


            harmadik = input("3. Mi Japán fővárosa? a) Peking, b) Tokió, c) Szöul, d) Bangkok:")
            if harmadik == "stop":
                print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                break
            if harmadik == "06304847308":
                print("pontos j-vel írjuk")
                continue
            if harmadik == "a" or harmadik == "c" or harmadik == "c":
                print("Helytelen válasz! A játék véget ért számodra!")
                exit()
            if harmadik == "b":
                print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                scoreboard += 1
                print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                negyedik = input("4. Melyik a legnagyobb óceán a Földön? a) Indiai-óceán, b) Atlanti-óceán, c) Csendes-óceán, d) Jeges-tenger:")
                if negyedik == "stop":
                    print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                    break
                if negyedik == "06304847308":
                    print("kussba van")
                    continue
                if negyedik == "a" or negyedik == "b" or negyedik == "d":
                    print("Helytelen válasz! A játék véget ért számodra!")
                    exit()
                if negyedik == "c":
                    print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                    scoreboard += 1
                    print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                    ototdik = input("5. Ki játszotta Jack Dawson szerepét a Titanic című filmben? a) Leonardo DiCaprio, b) Tom Hanks, c) Brad Pitt, d) Matt Damon:")
                    if ototdik == "stop":
                        print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                        break
                    if ototdik == "06304847308":
                        print("dik cabrio")
                        continue
                    if ototdik == "c" or ototdik == "b" or ototdik == "d":
                        print("Helytelen válasz! A játék véget ért számodra!")
                        exit()
                    if ototdik == "a":
                        print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                        scoreboard += 1
                        print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                        hatodik = input("6. Melyik a Föld legnagyobb emlőse? a) Elefánt, b) Kék bálna, c) Zsiráf, d) Jegesmedve:")
                        if hatodik == "stop":
                            print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                            break
                        if hatodik == "06304847308":
                            print("kék")
                            continue
                        if hatodik == "c" or hatodik == "a" or hatodik == "d":
                            print("Helytelen válasz! A játék véget ért számodra!")
                            exit()
                        if hatodik == "b":
                            print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                            scoreboard += 1
                            print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                            hetedik = input("7. Mi Kanada fővárosa? a) Vancouver, b) Ottawa, c) Toronto, d) Montreal:")
                            if hetedik == "stop":
                                print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                                break
                            if hetedik == "06304847308":
                                print("ott van a")
                                continue
                            if hetedik == "a" or hetedik == "c" or hetedik == "d":
                                print("Helytelen válasz! A játék véget ért számodra!")
                                exit()
                            if hetedik == "b":
                                print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                                scoreboard += 1
                                print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                                nyolc = input("7. Melyik évben kiáltották ki az Egyesült Államok függetlenségét? a) 1765, b) 1776, c) 1789, d) 1800:")
                                if nyolc == "stop":
                                    print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                                    break
                                if nyolc == "06304847308":
                                    print("1775 + 1")
                                    continue
                                if nyolc == "a" or nyolc == "c" or nyolc == "d":
                                    print("Helytelen válasz! A játék véget ért számodra!")
                                    exit()
                                if nyolc == "b":
                                    print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                                    scoreboard += 1
                                    print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                                    kilenc = input("9. Ki rendezte az Inception című filmet? a) Christopher Nolan, b) Quentin Tarantino, c) David Fincher, d) James Cameron")
                                    if kilenc == "stop":
                                        print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                                        break
                                    if kilenc == "06304847308":
                                        print("cigány név")
                                        continue
                                    if kilenc == "b" or kilenc == "c" or kilenc == "d":
                                        print("Helytelen válasz! A játék véget ért számodra!")
                                        exit()
                                    if kilenc == "a":
                                        print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                                        scoreboard += 1
                                        print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                                        tiz = input("10. Mi a kémiai jele az aranynak? a) Au, b) Ag, c) Fe, d) Hg")
                                        if kilenc == "stop":
                                            print(f"A játékot befejezted! Nyereményed: {scoreboard * 1000000}")
                                            break
                                        if kilenc == "06304847308":
                                            print("augusztus")
                                            continue
                                        if kilenc == "b" or kilenc == "c" or kilenc == "d":
                                            print("Helytelen válasz! A játék véget ért számodra!")
                                            exit()
                                        if kilenc == "a":
                                            print("Gratulálok! Eltaláltad a helyes választ! +1ponty")
                                            scoreboard += 1
                                            print(f"A pézzzed: {scoreboard * 1000000}-Ft")


                                            print("Gratulálok! Megnyerted a főnyereményt!")
                                            print(f"A pézzzed: {scoreboard * 1000000}-Ft")
                                            quit()