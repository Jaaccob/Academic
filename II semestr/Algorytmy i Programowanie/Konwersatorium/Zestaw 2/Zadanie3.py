def dodawanieMacierzy(tableA, tableB):
    #złożoność n^2
    for i in range(len(tableA)):
        for j in range(len(tableA[i])):
            tableA[i][j] += tableB[i][j]
    return tableA


def odejmowanieMacierzy(tableA, tableB):
    #złożoność n^2
    for i in range(len(tableA)):
        for j in range(len(tableA[i])):
            tableA[i][j] -= tableB[i][j]
    return tableA


def mnorzenieMacierzy(tableA, tableB):
    #złożoność n^3
    tableC = [[0 for j in range(len(tableA[i]))] for i in range(len(tableA))]
    for i in range(len(tableC)):
        for j in range(len(tableC[i])):
            suma = 0
            for k in range(len(tableA[i])):
                suma += tableA[i][k] * tableB[k][j]
            tableC[i][j] = suma
    return tableC


macierzA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
macierzB = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

print(dodawanieMacierzy(macierzA, macierzB))

macierzA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
macierzB = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(odejmowanieMacierzy(macierzA, macierzB))

macierzA = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
macierzB = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
print(mnorzenieMacierzy(macierzA, macierzB))
