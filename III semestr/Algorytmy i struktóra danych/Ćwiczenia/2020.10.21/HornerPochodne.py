def Horner(table, c):
    a = table[0]
    for i in range(1, len(table)):
        a = a * c + table[i]
    return a


def HornerU(table, c):
    for i in range(0, len(table) - 1):
        for j in range(1, len(table) - i):
            table[j] = table[j - 1] * c + table[j]


def HornerRekurencja(n, table, c):
    if n == 0:
        return table[0]
    return c * HornerRekurencja(n - 1, table, c) + table[n]


# table = [1, 2, -3, 0, 2]
def HornerUogulniony(n, table, c):
    for i in range(0, n):
        for j in range(1, n + 1 - i):
            table[j] = table[j - 1] * c + table[j]


# table = [2, 0, -3, 2, 1]
def HornerUogulnionyReverse(n, table, c):
    for i in range(n, -1, -1):
        for j in range(n - 1, n - i - 1, -1):
            table[j] = table[j + 1] * c + table[j]


# table = [1, 2, -3, 0, 2]
# HornerU(table, 2)
# print(table)
table = [1, 2, -3, 0, 2]
HornerUogulniony(4, table, 2)
print(table)
table = [2, 0, -3, 2, 1]
HornerUogulnionyReverse(4, table, 2)
print(table)

# print("Zwykły Horner")
# table2 = [3, 3, -2, 11]
# print(Horner(table2, 2))
# print(HornerRekurencja(3, table2, 2))
