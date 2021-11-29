def min(table):
    """
    Funkcja <code>min</code> jest rekurencyjną funkcją znajdującą element minimalny talbicy
    Złożoność algorytmiczna algorytmu wynosi O(log n)
    :param table:   Tablica nieposortowanych liczb
    :return:    Zwraca element minimalny
    """
    if len(table) == 1:
        return table[0]
    else:
        middle = len(table) // 2    #Podłoga liczby (len(table)/2)
        m1 = min(table[0:middle])   #Podłoga z n/2
        m2 = min(table[middle:])    #Sufit z n/2
        return m2 if m1 > m2 else m1


table = [3, 6, 7, 6, 2]
print(min(table))
