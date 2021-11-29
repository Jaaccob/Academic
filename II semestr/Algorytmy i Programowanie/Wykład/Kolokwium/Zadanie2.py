def pig_polish(we='in.txt', wy='out.txt'):
    with open(we, 'r', encoding='utf8', errors='ignore') as file:
        linijka = file.read().replace(" ", "\n").split("\n")
        print(linijka)


pig_polish("A_TEKST_DO_ZADANIA2.txt")
