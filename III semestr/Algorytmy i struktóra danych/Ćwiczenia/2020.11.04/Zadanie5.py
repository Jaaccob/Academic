def minMax(array, start=0, end=None):
    """
    Funkcja <code>minMax</code> jest rekurencyjną funkcją znajdującą jednocześnie element minimalny i maksymalny talbicy
    Złożoność algorytmiczna algorytmu wynosi O(log n)
    :param array:   Tablica nieposortowanych liczb
    :param start:   Index początkowy tablicy
    :param end:     Index końcowy tablicy
    :return:    Zwraca element minimalny i maksymalny
    """
    if end is None:
        end = len(array) - 1
    if start >= end - 1:
        left, right = array[start], array[end]
        return (left, right) if left < right else (right, left)
    # Jeśli tablica zawiera 2 elementy to zwracamy element minimalny i maksymalny
    middle = (start + end) >> 1
    # Wyszukiwanie środkowego indeksu tablicy
    # W rozwiązaniu zadania przesówam bit o 1 w lewo gdyż da mi to połowę początkowej wartości tzn. 12 - 1100 ; 6 - 0110
    leftMin, leftMax = minMax(array, start, middle)
    # Dzielimy tablice na pół żeby znaleźć element minimalny i maksymalny z lewej strony tablicy
    rightMin, rightMax = minMax(array, middle + 1, end)
    # Dzielimy tablice na pół żeby znaleźć element minimalny i maksymalny z prawej strony tablicy
    return (leftMin if leftMin < rightMin else rightMin), (leftMax if leftMax > rightMax else rightMax)
    # Jeśli leftMin < rightMin zwróć leftMin, w przeciwnym razie zwróć rightMin
    # Jeśli leftMax > rightMax zwróć leftMax, w przeciwnym razie zwróć rightMax


table = [3, 6, 1, 2, 6, 8, 2, 51, 2, 3, 6, -21, 3]
print(minMax(table))
