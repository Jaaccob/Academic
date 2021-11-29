from time import time
from random import randint


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


N = (10, 100, 300, 500, 700)

###Optymistyczny
for element in N:
    nList = list(range(element))

    start = time()
    insertionSort(nList)
    stop = time()
    print("Długość = {}, time = {}".format(element, stop - start))

###Pesymistyczny
for element in N[::-1]:
    nList = list(range(element))
    start = time()
    insertionSort(nList)
    stop = time()
    print("Długość = {}, time = {}".format(element, stop - start))


def mean(A):
    return sum(A) / len(A)


N = (10, 100, 300, 500, 700)

###Średni

for element in N:
    Time = []
    for j in range(10):
        List = [randint(1, 1000) for i in range(element)]
        print(List)
        start = time()
        insertionSort(List)
        stop = time()
        Time.append(stop - start)
    print("Długość = {}, time = {}".format(element, mean(Time)))
