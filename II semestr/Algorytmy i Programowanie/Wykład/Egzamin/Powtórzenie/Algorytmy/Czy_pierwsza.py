def pierwsza(a):
    for i in range(2, a - 1):
        if a % i == 0:
            return False
    return True


for i in range(40):
    print(pierwsza(i))
