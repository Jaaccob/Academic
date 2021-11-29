def parzysta(n):
    amount = 0
    while n != 1:
        amount += 1
        if n % 2 == 0:
            n /= 2
            continue
        if n != 1:
            n = (n * 3) + 1
            n /= 2
    return amount + 1


print(parzysta(12))
