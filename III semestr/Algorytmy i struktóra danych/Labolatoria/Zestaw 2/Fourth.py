def insertionSort(table, order):
    i = 1
    while i in range(1, len(table)):
        key = table[i]
        j = i - 1

        if order == "ascending":
            while j >= 0 and key < table[j]:
                table[j + 1] = table[j]
                j -= 1
            table[j + 1] = key
            i += 1
        elif order == "descending":
            while j >= 0 and key > table[j]:
                table[j + 1] = table[j]
                j -= 1
            table[j + 1] = key
            i += 1
        else:
            print("Błąd w określeniu sortowania")


table = [5, 1, 2, 5, 1, 2, 3, 3, 65, 7, 6, 5, 2, 1, 3]
insertionSort(table, "descending")
print(table)
