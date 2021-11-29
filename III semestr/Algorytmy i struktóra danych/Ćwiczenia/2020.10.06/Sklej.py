def sklej(length):
    table = [0]
    for i in range(length - 1):
        table.append(0)
    for i in range(2, length, ++1):
        if i % 2 == 0:
            table[i] = (i - 1 + 2 * table[int(i / 2)])
        else:
            table[i] = (i - 1 + table[int((i - 1) / 2)] + table[int((i + 1) / 2)])
    print(table)


sklej(7)
