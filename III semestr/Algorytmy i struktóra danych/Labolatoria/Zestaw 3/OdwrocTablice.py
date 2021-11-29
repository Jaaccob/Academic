def reverseTable(table):
    if len(table) == 1:
        return table
    return reverseTable(table[1:]) + [table[0]]


table = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverseTable(table))
