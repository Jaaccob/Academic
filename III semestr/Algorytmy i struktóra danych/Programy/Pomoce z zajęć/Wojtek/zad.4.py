def Skojarzone(liczbaa):
    wynik = []
    wynik2 = []
    for i in range (1,liczbaa // 2 + 1):
        if (liczbaa % i == 0):
            wynik.append (i)
    liczbab = sum (wynik)  #Sumuje wynik numer1
    liczbab -= 1
    for j in range (1,liczbab // 2 + 1):
        if (liczbab % j == 0):
            wynik2.append (j)
    sumawynikow = sum (wynik2)  #sumuje wynik numer 2
    sumawynikow -= 1
    if sumawynikow == liczbaa:
        return (liczbaa,"jest skojarzona z liczba",liczbab)
    else:
        return "Nie znaleziono liczby skojarzonej"


print (Skojarzone(120))
print(Skojarzone)