# Zad 1
def selectionSort(table):
    for i in range(0, len(table) - 1):
        min = i
        for j in range(i + 1, len(table)):
            if table[j] < table[min]:
                min = j
        tmp = table[i]
        table[i] = table[min]
        table[min] = tmp


# Zad 4
def bubbleSort(table):
    for i in range(1, len(table) - 1):
        for j in range(len(table) - 1, i - 1, -1):
            if table[j] < table[j - 1]:
                table[j], table[j - 1] = table[j - 1], table[j]


# Zad 7
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


# Zad 2
table = [14, 40, 31, 28, 3, 15, 17, 51]
selectionSort(table)
table = [3, 14, 15, 17, 28, 31, 50, 60]
selectionSort(table)
table = [51, 40, 31, 28, 17, 15, 14, 3]
selectionSort(table)
table = [23, 23, 23, 23, 23, 23, 23, 23]
selectionSort(table)
table = [14, 40, 31, 28, 3, 15, 17, 51]
# Zad 5
bubbleSort(table)
# Zad 8
table = [14, 40, 31, 28, 3, 15, 17, 51]
insertionSort(table)
table = [3, 14, 15, 17, 28, 31, 50, 60]
insertionSort(table)
table = [51, 40, 31, 28, 17, 15, 14, 3]
insertionSort(table)
table = [23, 23, 23, 23, 23, 23, 23, 23]
insertionSort(table)
table = [14, 40, 31, 28, 3, 15, 17, 51]
