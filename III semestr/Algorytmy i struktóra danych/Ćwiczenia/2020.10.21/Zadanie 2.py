def HornerUogulniony(n, table, c):
    for i in range(0, n):
        for j in range(1, n + 1 - i):
            table[j] = table[j - 1] * c + table[j]


table = [1, 2, -3, 0, 2]
HornerUogulniony(4, table, 2)
print(table)