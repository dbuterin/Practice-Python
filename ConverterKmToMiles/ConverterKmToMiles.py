print "Dobrodosli u converter kilometar u milje"
while True:
    for i in range(2):
        unos = int(raw_input("unesite kilometre: "))
        milja= 0.621371
        print unos*milja
        jos = raw_input("Zelite li jos jednom pokusati(y/n): ")
        if jos != "y":
            print "Hvala"
            break
