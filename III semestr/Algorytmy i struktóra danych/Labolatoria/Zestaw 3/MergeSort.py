def merge(table, left, centre, right):
    start = left
    middle = centre + 1

    # Tablica pomocnicza
    auxiliary = []

    # Wybieranie mniejszego elementów z tablic
    while (start <= centre) and (middle <= right):
        if table[middle] < table[start]:
            auxiliary.append(table[middle])
            middle += 1
        else:
            auxiliary.append(table[start])
            start += 1

    # Dopisanie pozostałych elementów
    if start <= centre:
        while start <= centre :
            auxiliary.append(table[start])
            start += 1
    else:
        while middle <= right:
            auxiliary.append(table[middle])
            middle += 1

    # Przepisywanie wyniku
    suma = right - left + 1
    i = 0
    while i < suma:
        table[left + i] = auxiliary[i]
        i += 1
    return table


def mergeSort(table, left, right):
    if left != right:
        # Sprawdzamy gdzie znajduje się środek tablicy
        centre = int((left + right) / 2)
        # //2
        # Wywołujemy funkcje rekurencyjną lewej części tablicy
        mergeSort(table, left, centre)
        # Wywołujemy funkcje rekurencyjną prawej części tablicy
        mergeSort(table, centre + 1, right)
        # Scalamy lewą część z prawą częścią sortując ją
        merge(table, left, centre, right)
    # Posortowaną tablice zwracamy
    return table


table = [1, 5, 3, 1, 0, 2, 1]
mergeSort(table, 0, len(table) - 1)
print(table)

