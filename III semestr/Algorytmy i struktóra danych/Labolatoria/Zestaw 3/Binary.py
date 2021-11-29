def numberBinary(n):
    if n > 0:
        numberBinary(int(n / 2))
        print(n % 2, end="")


numberBinary(8)
