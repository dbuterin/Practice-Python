broj = 5
broj_pokusaja = 3

while True:
    for i in range(broj_pokusaja):
        print "Pokusaj " + str(i + 1) + "/" + str(broj_pokusaja)

        pokusaj = int(raw_input("Unesite broj: "))
        if pokusaj == broj:
            print "Bravo tocno je"
            break
        elif broj < pokusaj:
            print "Vas unos je veci od trazenog broja"
        elif broj > pokusaj:
            print "Vas unos je manji od trazenog broja"

    jos = ""
    if pokusaj != broj:
        jos = raw_input("Zelite li jos jednom pokusati (y/n): ")
    if jos != "y" or pokusaj == broj:
        break


