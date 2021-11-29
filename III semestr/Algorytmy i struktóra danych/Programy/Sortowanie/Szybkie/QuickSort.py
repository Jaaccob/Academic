def quickSort(table, left, right):
    if left < right:
        i = divide(table, left, right)
        quickSort(table, left, i - 1)
        quickSort(table, i + 1, right)


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


table = [3, 41, 52, 26, 38, 57, 9]
quickSort(table, 0, 6)
print(table)
