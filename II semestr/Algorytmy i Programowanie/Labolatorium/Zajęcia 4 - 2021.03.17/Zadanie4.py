def bubbleSortFlag(table):
    for i in range(len(table) - 1):
        flag = False;
        for j in range(len(table) - 1):
            if (table[j] > table[j + 1]):
                table[j], table[j + 1] = table[j + 1], table[j]
                flag = True;
        if flag == False:
            break
    return table


table = [4, 1, 2, 4, 6, 1, 2, 3]
bubbleSortFlag(table)
