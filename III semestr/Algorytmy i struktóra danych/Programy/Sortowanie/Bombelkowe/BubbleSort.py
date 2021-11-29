def bubbleSort(table):
    for x in range(len(table) - 1):
        for y in range(0, len(table) - x - 1):
            if table[y] > table[y + 1]:
                table[y], table[y + 1] = table[y + 1], table[y]


table = [64, 34, 25, 12, 22, 11, 90]
bubbleSort(table)
print(table)
