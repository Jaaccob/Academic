def linearSerch(table, number):
    for i in range(0, len(table)):
        if table[i] == number:
            return i


def linearSerchWithSentry(table, number):
    table.append(number)
    length = len(table) - 1
    i = 0
    while table[i] != number:
        i += 1
    if length > i:
        return i
    else:
        return False
    ##Złożoność algorytmu wynosi O(n)
    ##Zastosowanie wartownika pozwala algorytmowni nie sprawdzać czy przekroczył index tablicy za każdym kolejnym elementem tablicy co znacznie przyśpiesza czas działania
    ##Algorytm tylko raz sprawdza czy przekroczył index tablicy w momencie gdy znajdzie szukana liczbę (bądz wartownik)


table = [3, 5, 1, 2, 3, 6, 8, 1, 2, 4, 7, 1, 2, 5]
print(linearSerch(table, 8))
print(linearSerchWithSentry(table, 11))
