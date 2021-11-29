from time import time
from random import randint


def selectionSort(table):
    for i in range(0, len(table) - 1):
        min = i
        for j in range(i + 1, len(table)):
            if table[j] < table[min]:
                min = j
        tmp = table[i]
        table[i] = table[min]
        table[min] = tmp


"""Algorytm <code>selectionSort</code> odpowiada za sortowanie tablicy przez wybor najmniejszego elementu i wstawienie go w 1 miescu tablicy
Algorytm ma złożoność:
- w wersji optymistycznej O(n^2)
- w wersji pesymistycznej O(n^2)
- w wersji średniej O(n^2)

Algorytm jest niestabilny """


N = [10, 100, 300, 500, 700]

###Optymistyczny
print("### Optymistyczny ")
for element in N:
    nList = list(range(element))
    print(len(nList))
    start = time()
    selectionSort(nList)
    stop = time()
    print("Długość = {}, time = {}".format(element, stop - start))

###Pesymistycznych
print("### Pesymistycznych ")
for element in N[::-1]:
    nList = list(range(element))
    start = time()
    selectionSort(nList)
    stop = time()
    print("Długość = {}, time = {}".format(element, stop - start))


def mean(A):
    return sum(A) / len(A)


###Średni

print("### Średni ")
for element in N:
    Time = []
    for j in range(10):
        List = [randint(1, 1000) for i in range(element)]
        start = time()
        selectionSort(List)
        stop = time()
        Time.append(stop - start)
    print("Długość = {}, time = {}".format(element, mean(Time)))
