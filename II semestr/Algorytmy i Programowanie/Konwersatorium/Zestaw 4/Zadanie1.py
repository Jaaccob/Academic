"""
table - tablica
n - długość tablicy
Wybieramy ostatni element z listy i porównujemy go z resztą, jeśeli jest większy od innego danego elementu, skraca
tablicę o ten ostatni element i wysyła ją ponownie do funkcji sprawdzającej

Funkcja minimum(table):
n = dlugość table
    if n = 1:
        return table[n]
    for i to n - 1:
        if table[n - 1] > table[i]:
            Funkcja minimum(table[n - 1])
        else:
            return table[n]
"""
def zad_1(table):
    n = len(table)
    if n == 1:
        return table[n]
    for i in range(n - 1):
        if table[n - 1] > table[i]:
            zad_1(table[:n - 1])
        else:
            return table[n]


"""
table - tablica
n - długość tablicy
Wybieramy ostatni element z listy i porównujemy go z resztą, jeśeli jest większy od innego danego elementu, skraca
tablicę o ten ostatni element i wysyła ją ponownie do funkcji sprawdzającej

Funkcja minimum(table):
n = dlugość table
    if n = 1:
        return table[n]
    for i to n - 1:
        if table[0] > table[i]:
            Funkcja minimum(table[n - 1])
        else:
            return table[n]
"""
def zad_2(table):
    n = len(table)
    if n == 1:
        return table[n]
    for i in range(n - 1):
        if table[0] > table[i]:
            zad_1(table[:n - 1])
        else:
            return table[n]


"""
table - tablica
n - długość tablicy
Jeżeli długość tablicy = 1 to zwróć ten element, jeśeli nie to sprawdź czy środek tej tablicy jest większy od prawej
strony , jeżelijest to odwołaj się do funkcji z tablicą od połowy listy w prawo, jeśeli jest większe od lewej strony 
to odwołaj się do funkcji z tablicą od początku do połowy listy

Funkcja_minimum_dziel(table):
    n = dlugość table
    b = 1/2 dlugosc table
    x = table[n]
    if n=1:
        return table[n]
    if table[n]>table[n+1]:
        Funkcja_minimum_dziel(table[b:n])
    if table[n]>table[n-1]:
        Funkcja_minimum_dziel(table[1:b])
"""
def zad_3(table):
    n = len(table)
    b = 1 / 2 * n
    x = table[n]
    if n == 1:
        return table[n]
    if table[n] > table[n + 1]:
        zad_3(table[b:n])
    if table[n] > table[n - 1]:
        zad_3(table[1:b])


"""
table - tablica
n - długość tablicy
x - minimum
y - maximum
x,y = table[1]
table[i] - dodajemy ostatni element jakikolwiek

for i to n:
    if i = n:
        break
    if table[i] > table[i+1]:
        if table[i]>y:
            y=table[i]
    else:
        if table[i]<x:
            x=table[i]
return "Minimum to x a maksimum to y"
"""
def zad_4(table):
    n = len(table)
    x = 0
    y = 0
    for i in range(n):
        if i == n:
            break
        if table[i] > table[i + 1]:
            if table[i] > y:
                y = table[i]
        else:
            if table[i] < x:
                x = table[i]
    return f"Minimum to {x} a maksimum to {y}"

