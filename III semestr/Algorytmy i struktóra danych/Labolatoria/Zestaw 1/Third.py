def min_max(table):
    min = table[0]
    max = table[0]
    indexMin = 0
    indexMax = 0
    for i in range(1, len(table)):
        if min > table[i]:
            min = table[i]
            indexMin = i
        if max < table[i]:
            max = table[i]
            indexMax = i
    return indexMin+1, indexMax+1


table = [3, 6, 1, 2, 3, 6, 87, 1, 2, 5, 2]
print(min_max(table))
