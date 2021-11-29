def linearSearch(table, key):
    i = 0
    table.append(key)
    while table[i] != key:
        i += 1
    if i <= len(table):
        return i
    else:
        return 0


test01 = [1, 7, 4, 2, 8]
print(linearSearch(test01, 2))
