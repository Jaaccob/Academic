from random import randint


def liczba(n, table):
    tableC = [i for i in range(n)]
    for i in range(0, n):
        tableC[i] = 1
        for j in range(0, i):
            if table[j] < table[i] and tableC[j] + 1 > tableC[i]:
                tableC[i] = tableC[j] + 1
    return table, tableC


print(liczba(5, table=[4, 2, 3, 1, 5]))
print(liczba(4, table=[3, 3, 3, 3]))
print(liczba(4, table=[1, 2, 3, 4]))
print(liczba(4, table=[1, 3, 2, 5]))
print(liczba(10, table=[3, 5, 1, 4, 6, 7, 2, 10, 9, 11]))
print(liczba(7, table=[3, 1, 4, 2, 6, 5, 7]))
print(liczba(8, table=[3, 5, 10, 4, 6, 7, 9, 11]))
