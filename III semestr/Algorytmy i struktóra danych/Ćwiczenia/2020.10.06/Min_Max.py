def min_max(tabela):
    min = tabela[0]
    max = tabela[0]
    for i in range(1, len(tabela)):
        if min > tabela[i]:
            min = tabela[i]
        if max < tabela[i]:
            max = tabela[i]
    return min, max