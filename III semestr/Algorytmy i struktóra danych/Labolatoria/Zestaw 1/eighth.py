def dzielIRzadz(table, key):
    left = 0
    right = len(table)
    while left <= right:
        middle = int((left + right) / 2)
        if table[middle] == key:
            return middle
        elif table[middle] > key:
            right = middle - 1
        else:
            left = middle + 1
    return None


table = [-17, -11, -5, -3, 0, 1, 3, 5, 7, 12, 15, 32, 33, 47, 91]
print(dzielIRzadz(table, 6))
