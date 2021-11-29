def sort(table, method, order):
    if method == "insertion":
        insertionSort(table, order)
    elif method == "selection":
        selectionSort(table, order)
    else:
        return False


def insertionSort(table, order):
    if order == "ascending":
        i = 1
        while i in range(1, len(table)):
            key = table[i]
            j = i - 1
            while j >= 0 and key < table[j]:
                table[j + 1] = table[j]
                j -= 1
            table[j + 1] = key
            i += 1

    elif order == "descending":
        i = 1
        while i in range(1, len(table)):
            key = table[i]
            j = i - 1
            while j >= 0 and key > table[j]:
                table[j + 1] = table[j]
                j -= 1
            table[j + 1] = key
            i += 1
    else:
        return False


def selectionSort(table, order):
    if order == "ascending":
        for i in range(0, len(table) - 1):
            minIndex = i
            for j in range(i + 1, len(table)):
                if table[j] < table[minIndex]:
                    minIndex = j
            table[i], table[minIndex] = table[minIndex], table[i]

    elif order == "descending":
        for i in range(0, len(table) - 1):
            minIndex = i
            for j in range(i + 1, len(table)):
                if table[j] > table[minIndex]:
                    minIndex = j
            table[i], table[minIndex] = table[minIndex], table[i]
    else:
        return False


table1 = [3, 6, 1, 2, 45, 1, 2, 3]
sort(table1, "insertion", "descending")
print(table1)
table2 = [3, 6, 1, 2, 45, 1, 2, 3]
sort(table2, "selection", "descending")
print(table2)
