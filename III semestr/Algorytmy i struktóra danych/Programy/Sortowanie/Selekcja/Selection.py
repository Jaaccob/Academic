def Selekcja(table, left, right, k):
    if left == right:
        return table[left]
    j = divide(table, left, right)
    m = j - left + 1
    if k == m:
        return table[j]
    else:
        if k < m:
            return Selekcja(table, left, j - 1, k)
        else:
            return Selekcja(table, j + 1, right, k - m)


def divide(table, left, right):
    x = table[right]
    i = left - 1
    for j in range(left, right):
        if table[j] <= x:
            i += 1
            change(table, i, j)
    change(table, i + 1, right)
    return i + 1


def change(table, first, second):
    current = table[first]
    table[first] = table[second]
    table[second] = current


table = [14, 40, 31, 28, 3, 15, 17, 51]
print(Selekcja(table, 0, 7, 4))
