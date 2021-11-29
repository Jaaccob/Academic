def pierwsza(n):
    ile_pierwszych = 0
    p = 2
    while ile_pierwszych <= n:
        t = True
        for i in range(2, p):
            if p % i == 0:
                t = False
                break
        if t:
            ile_pierwszych += 1
            with open("Liczby_pierwsze", "a") as file:
                file.write(str(p) + " ")
        p += 1


pierwsza(10)
