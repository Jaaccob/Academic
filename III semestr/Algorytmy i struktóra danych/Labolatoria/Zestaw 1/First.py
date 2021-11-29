def min_max(tabela):
    min = tabela[0]
    max = tabela[0]
    for i in range(1, len(tabela)):
        if min > tabela[i]:
            min = tabela[i]
        if max < tabela[i]:
            max = tabela[i]
    return min, max


"""
    min = tabela[0] - pierwsze przypisanie
    max = tabela[0] - drugie przypisanie 
    pętla for - n przypisań
    Więc złożoność algorytmu wynosi 2n-2 
    
"""

tabela = [3, 1, 5, 6, 8, 2, 3]
print(min_max(tabela))



