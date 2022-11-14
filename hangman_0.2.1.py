# właściwy kod gry
print("hangman game by frogmaker")
print("Kontakt z autorem: gg:5043515 ; serwis@hupla.pl ")
print("")

# zmienne
ver2 = "______"
hor6 = "|"
hor5 = "|"
hor4 = "|"
hor3 = "|"
hor2 = "|"
hor1 = "|"
head = "o"
korp = "/|\ "
legs = "/ \ "
err = 0
endgame = ""
ukryte = ""
win = 0
# definicje/funkcje

def hangman(ver2, hor5, hor4, hor3, hor2, hor1, legs, korp, head, hor6):
    print("")
    print("     #################     ")
    print("     #  ", ver2, "     #")
    print("     #  ", hor5, "  ", hor6, "     #")
    print("     #  ", hor4, "  ", head, "     #")
    print("     #  ", hor3, " ", korp, "   #")
    print("     #  ", hor2, " ", legs, "   #")
    print("     #  ", hor1, "________  #")
    print("     #################     ")
    print("")
    print("        ", " ".join(ukryte))
    print(endgame)
    return

hangman(ver2, hor5, hor4, hor3, hor2, hor1, legs, korp, head, hor6)

def wynik(err, ver2, hor5, hor4, hor3, hor2, hor1, legs, korp, head, hor6):
    if err == 0:
        ver2 = "      "
        hor5 = hor4 = "  "
        hor3 = hor2 = hor1 = " "
        legs = "    "
        korp = "    "
        head = hor6 = ""

    elif err == 1:

        hor1 = hor2 = hor3 = "|"
        ver2 = "      "
        hor5 = hor4 = "  "
        legs = "    "
        korp = "    "
        head = hor6 = ""

    elif err == 2:
        hor1 = hor2 = hor5 = hor4 = hor3 = "|"
        ver2 = "      "
        legs = "    "
        korp = "    "
        head = hor6 = " "

    elif err == 3:
        head = hor6 = " "
        hor1 = hor5 = hor2 = hor3 = hor4 = "|"
        ver2 = "______"
        legs = "    "
        korp = "    "
    elif err == 4:
        head = " "
        hor1 = hor5 = hor2 = hor3 = hor4 = hor6 = "|"
        ver2 = "______"
        legs = "    "
        korp = "    "
    elif err == 5:
        legs = korp = "    "
        hor1 = hor5 = hor2 = hor3 = hor4 = hor6 = "|"
        ver2 = "______"
        head = "o"
    elif err == 6:
        legs = "    "
        hor1 = hor5 = hor2 = hor3 = hor4 = hor6 = "|"
        ver2 = "______"
        head = "o"
        korp = "/|\ "
    elif err == 7:
        legs = ""
        hor1 = hor5 = hor2 = hor3 = hor4 = hor6 = "|"
        ver2 = "______"
        head = "o"
        korp = "/|\ "
        legs = "/ \ "
        endgame = "Porażka!"
    else:
        print("Błąd programu - liczba błędów przekracza dopuszczalną liczbę")

    return hangman(ver2, hor5, hor4, hor3, hor2, hor1, legs, korp, head, hor6)

c = float(1)
while c == 1:
    print("Dostępne opcje:")
    print("1 - wylosuj słowo o dowolnej długości")
    print("2 - wybór długości słowa /jeszcze nie działa/")
    print("3 - wsparzyj autora")
    print("dowolny znak by zakończyć")
    tryb = input("Wybierz opcję: ")

    if tryb == "1":
        filepath = "slowa.txt"
        f = open(filepath, "r+", encoding="utf-8")
        # zliczanie ilości wierszy
        Counter = 0
        Content = f.read()
        CoList = Content.split("\n")

        for i in CoList:
            if i:
                Counter += 1
        f.close()
        wiersze = Counter - 1
        import random
        nrwiersza = random.randint(0, wiersze)

        f = open(filepath, "r+", encoding="utf-8")
        linie = f.readlines()
        tabela = []
        for line in linie:
            line = line.split()
            tabela.append(line)

        wiersz = tabela[nrwiersza]
        # liczba słów w wierszu 'sww'

        sww = len(wiersz) - 1

        f.close()
        lp = random.randint(0, sww)

        word = tabela[nrwiersza][lp]
        # print(word)


        ii = 0
        end = len(word)
        end1 = end - 1
        ukryte = []
        while ii != end:
            ukryte.append("_")
            ii += 1

        while err != 7:
            errslowo = 0
            print("")
            litera = input("podaj literę: ")
            ii = 0

            while ii != end:
                if word[ii] == litera:
                    ukryte[ii] = litera
                else:
                    errslowo += 1

                ii += 1
            if errslowo == end:
                err += 1
                print()
                print("        Błąd!")

            wynik(err, ver2, hor5, hor4, hor3, hor2, hor1, legs, korp, head, hor6)


            znaki = " ".join(ukryte)
            kondyszyn = znaki.find("_")
            if kondyszyn == -1:
                err = 7
                win = 1
        if win != 1:
            print("Zbyt dużo błędów - gra skończona!")
            odkryte = " ".join(word)
            print("Szukane słowo to:", odkryte)
        else:
            print("Gratulacje! Udało Ci sie odgadnąć szukane słowo!")

        input("Press ENTER to contiune...")
        err = 0
        win = 0
    elif tryb == "2":

        input("Press ENTER to contiune...")

    elif tryb == "3":
        print("")
        print("Bitcoin (BTC): 17dgi8g3XyT2JcuHp76R4He8Yp28iJvbyB")
        print("Bitcoin Cash (BCC): qp92jhsqa6dqt0enffsmjmrh953gff3rxufe2c2vyw")
        print("Litecoin (LTC): LcUr5bWoTDwUsFfTdME62zSMJYcCQpCV3H")
        print("Iridium (ird): ir47aGcna4jaUn8tk9s8tBFT9uuFncDG8T8SZn78nd4kN4eUhYtzeFMFdSXT8G43AsELZf48PzFwoUGKQGRWjZK414NSu1PCq")
        print("Scala (xla): SvjvQckKCqic8qhHgREnY5ScSgigqAt5o2cEDrPcCPn72idRsooW2HJdMYUJqJSULuLAFHfKbhKFCC9xgU2Fkqg71BpmuANbe")
        print("")
        input("Press ENTER to contiune...")
    else:
        c = 0, input("Press ENTER to exit")

# input("Press ENTER to exit")