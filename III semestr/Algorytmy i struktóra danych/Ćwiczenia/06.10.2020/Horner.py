def Horner(table, number):
    a = table[0]
    for i in range(1, len(table)):
        a = number * a + table[i]
    return a


table = [3, -2, 0, 3, 0, -5]
print(Horner(table, 2))
