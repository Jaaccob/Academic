def HornerNewton(tableA, tableX, number):
    a = tableA[len(tableA) - 1]
    for i in range(len(tableA) - 2, -1, -1):
        a = a * (number - tableX[i]) + tableA[i]
    return a


tableA = [1, -5, 3, 2]
tableX = [0, 1, 2]
print(HornerNewton(tableA, tableX, -2))
