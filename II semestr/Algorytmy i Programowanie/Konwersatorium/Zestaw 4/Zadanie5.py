import math


def min_max(table):
    niep = len(table) % 2
    for i in range(len(table) // 2):
        if table[i] > table[i + 1]:
            table[i], table[i + 1] = table[i + 1], table[i]
    minimum = table[0]
    maximum = table[1]
    for i in range(1, len(table) // 2):
        if minimum > table[i * 2]:
            minimum = table[i * 2]
        if maximum < table[i * 2 + 1]:
            maximum = table[i * 2 + 1]
    if niep == 1 and maximum < table[-1]:
        maximum = table[-1]
    if niep == 1 and minimum > table[-1]:
        minimum = table[-1]
    return minimum, maximum


def min_max_linear(table):
    min = table[0]
    max = table[0]
    for i in table:
        if min > i:
            min = i
        if max < i:
            max = i
    return min, max


def min_max_rek(table, l, r):
    minimum = 0
    maximum = 0
    if l == r:
        return table[l], table[l]
    if l + 1 == r:
        if table[l] > table[r]:
            return table[r], table[l]
        else:
            return table[l], table[r]
    m = math.ceil((l + r) / 2)
    min1, max1 = min_max_rek(table, l, m)
    min2, max2 = min_max_rek(table, m, r)
    if min1 < min2:
        minimum = min1
    else:
        minimum = min2
    if max1 > max2:
        maximum = max1
    else:
        maximum = max2
    return minimum, maximum


def NWD_rek(a, b):
    if b == 0:
        return a
    else:
        return NWD_rek(b, a % b)


table = [5, 1, 2, 65, 7, 23, 1, 6, 12, 4]
print(NWD_rek(56, 72))

# (56,72), (72,56), (56,16), (16,8) , (8,0)