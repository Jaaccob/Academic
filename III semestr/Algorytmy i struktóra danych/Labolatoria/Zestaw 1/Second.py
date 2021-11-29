def min_max(table):
    min = table[0]
    max = table[0]
    i = 1
    while i < len(table):
        if min > table[i]:
            min = table[i]
        if max < table[i]:
            max = table[i]
        i += 1
    return min, max


table = [3, 8, 1, 3, 12, 5, 1, 2]
print(min_max(table))
