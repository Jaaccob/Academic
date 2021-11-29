def sumA(table):
    # Złożoność teta = n
    sumTab = 0
    for i in range(len(table)):
        sumTab += table[i]
    return sumTab


def productB(table):
    # Złożoność teta = n
    productTab = 1
    for i in range(len(table)):
        productTab *= table[i]
    return productTab


def arithmeticSequenceC(table):
    # Złożoność teta = n+1
    sumTab = 0
    for i in range(len(table)):
        sumTab += table[i]
    return sumTab / len(table)


def arithmeticSequenceD(table):
    # Złożoność teta = n+1
    sumTab = 0
    amount = 0
    for i in range(len(table)):
        if table[i] >= 0:
            sumTab += table[i]
            amount += 1
    return sumTab / amount


def sumProductE(table):
    # Złożoność teta = n^2
    sumTab = 0
    for i in range(len(table)):
        iloczyn = 1
        for j in range(i):
            iloczyn *= table[j]
        sumTab += iloczyn
    return sumTab


def sumProductF(table):
    # Złożoność teta = n^2x`
    sumTab = 0
    for i in range(len(table)):
        iloczyn = 1
        for j in range(i, len(table)):
            iloczyn *= table[j]
        sumTab += iloczyn
    return sumTab


table = [1, 2, 3]
print(sumA(table))
print(productB(table))
print(arithmeticSequenceC(table))
print(arithmeticSequenceD(table))
print(sumProductE(table))
print(sumProductF(table))
