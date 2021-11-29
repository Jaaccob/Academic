def maxmin(lista):
    dlugosc=len(lista)
    lista2=lista.copy()
    if dlugosc<3 and licznik==0:
        return "Nie ma takich liczb"

    maksimum=lista[0]
    minimum = lista[0]

    for i in range(3):  #W tej petli wyszukuję 3 maksimum i minimum
        maksimum = lista [0]
        minimum = lista [0]
        for i in lista[1:len(lista)]:
            if maksimum<i:
                maksimum=i
            if minimum>i:
                minimum=i
        lista.remove (minimum)
        lista.remove (maksimum)
    print(lista2)

    for i in range(len(lista2)):  #Tutaj po wyszukanym minimum i maksimum szukamy jego indeksu
        if minimum== lista2[i]:
            minimumidx=i
        if maksimum == lista2[i]:
            maksimumidx=i
    return minimumidx,maksimumidx

x=[1,2,3,4,5,6]

print(maxmin(x))

