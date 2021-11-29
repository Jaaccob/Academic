def wyszukiwanie_bin(table, n):
    """
    Funkcja wyszukiwanie_bin odpowiedzialna jest za wyszukiwaine binarne w talblicy

    ...

    Attribute
    ---------
    table: list
        Lista posortowana w której mamy szukać danego elelementu
    n: int
        Liczba szukana w liście

    Return
    ------
    Funkcja zwraca indeks jeśli element znajduje się w liście, w przeciwnym przypadku zwraca None
    """
    low = 0
    high = len(table) - 1
    mid = 0

    while low <= high:
        mid = (high + low) // 2
        if table[mid] < n:
            low = mid + 1
        elif table[mid] > n:
            high = mid - 1
        else:
            return mid
    return None


lista1 = [11, 17, 20, 39, 44, 65]
n = 44

wynik = wyszukiwanie_bin(lista1, n)

if wynik != None:
    print("Element jest obecny na indeksie: ", str(wynik))
else:
    print("Elementu nie ma w liście")
