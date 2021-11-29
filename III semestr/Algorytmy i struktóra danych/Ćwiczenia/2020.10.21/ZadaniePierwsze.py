def HornerPochodne(n, table, c):
    for i in range(n, -1, -1):
        for j in range(n - 1, n - i - 1, -1):
            table[j] = table[j + 1] * c + table[j]


table = [-9, -4, 0, -6, 3]
HornerPochodne(4, table, 3)
print(table)

table1 = [-1, 2, -6, 2]
HornerPochodne(3, table1, 3)
print(table1)
