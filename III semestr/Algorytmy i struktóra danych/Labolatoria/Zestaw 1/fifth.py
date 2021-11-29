def suma(tableA):
    sum = tableA[0]
    for i in range(1, len(tableA)):
        sum += tableA[i]
    return sum


def iloraz(tableA):
    quotient = tableA[0]
    for i in range(1, len(tableA)):
        quotient *= tableA[i]
    return quotient


def sredniaArytmetyczna(tableA):
    avg = tableA[0]
    for i in range(1, len(tableA)):
        avg += tableA[i]
    return avg / len(tableA)


def sredniaArytmetycznaDodatnia(tableA):
    avg = 0
    for i in range(0, len(tableA)):
        if tableA[i] > 0:
            avg += tableA[i]
    return avg / len(tableA)


def sumaIloczynow(tableA):
    sum = 0
    for i in range(0, len(tableA)):
        quotient = 1
        for j in range(0, len(tableA)):
            quotient *= tableA[j]
        sum += quotient
    return sum


def Horner(tableA, c):
    a = tableA[0]
    for i in range(1, len(tableA)):
        a = c * a + tableA[i]
    return a


tableA = [3, -2, 0, 3, 0, -5]
print(suma(tableA))  # 12
print(iloraz(tableA))  # -113400
print(sredniaArytmetyczna(tableA))  # 1.2
print(sredniaArytmetycznaDodatnia(tableA))  # 2.7
print(sumaIloczynow(tableA))  # -113400
print(Horner(tableA, 2))
