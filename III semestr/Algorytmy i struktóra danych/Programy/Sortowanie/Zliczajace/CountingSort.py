def countingSort(tableA, m):
    tableB = [0 for k in range(len(tableA) + 1)]
    tableC = []
    for i in range(0, len(tableA) - 1):
        tableC.append(0)
    for i in range(0, len(tableC) + 1):
        tableC[tableA[i]] = tableC[tableA[i]] + 1
    for i in range(1, len(tableA) - 1):
        tableC[i] = tableC[i] + tableC[i - 1]
    for i in range(len(tableA) - 1, 0, -1):
        print("i {}".format(i))
        tableB[tableC[tableA[i]]] = tableA[i]
        tableC[tableA[i]] = tableC[tableA[i]] - 1
        print("table C {}".format(tableC))
        print("table B {}".format(tableB))
    for i in range(0, len(tableA)):
        tableA[i] = tableB[i + 1]
    return tableA


tableA = [3, 6, 4, 1, 3, 4, 1, 4]
table = [5, 1, 2, 5, 6, 1, 2, 3, 3, 3, 3, 1, 54, 1, 2, 6, 8, 23, 76, 112]
countingSort(table, 112)
print(tableA)
