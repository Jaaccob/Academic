def insertionSort(table):
    i = 1
    while i in range(1, len(table)):
        key = table[i]
        j = i - 1
        while j >= 0 and key < table[j]:
            table[j + 1] = table[j]
            j -= 1
        table[j + 1] = key
        i += 1


"""Algorytm <code>insertionSort</code> odpowiada za sortowanie tablicy przez wstawianie
Algorytm ma złożoność:
 -w wersji optymistycznej O(n)
 -w wersji pesymistycznej O(n^2)
 -w wersji średniej O(n^2)
 
 Algorytm jest stabilny 
 Algorytm jest wydajny dla zbiorów o niewielkiej liczebności
 Liczba wykonanych porównań jest zależna od liczby inwersji w permutacji, dlatego algorytm jest wydajny dla danych wstępnie posortowanych
"""

table = [5, 1, 2, 5, 1, 2, 3, 3, 65, 7, 6, 5, 2, 1, 3]
insertionSort(table)
print(table)
