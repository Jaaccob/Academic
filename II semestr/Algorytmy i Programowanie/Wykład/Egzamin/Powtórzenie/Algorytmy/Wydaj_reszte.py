def reszta(reszta):
    iloscMonet = 3
    monety = [1, 2, 5]
    historia = []
    licznik = 0
    while reszta > 0:
        nominal = 0
        for i in range(iloscMonet):
            if monety[i] <= reszta and monety[i] > nominal:
                nominal = monety[i]
        reszta = reszta - nominal
        historia.append(nominal)
        licznik += 1
    return licznik, historia


print(reszta(6))
