def pyramid(n):
    for i in range(n):
        for j in range(n-i):
            print("*", end="")
        print()


pyramid(12)