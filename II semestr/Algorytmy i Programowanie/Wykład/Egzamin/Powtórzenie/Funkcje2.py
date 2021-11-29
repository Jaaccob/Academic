def my_decor(fun):
    def wrapper(a1, q):
        ciag = fun(a1, q)
        parzyste = []
        for i in ciag:
            if i % 2 == 0:
                parzyste.append(i)
        print(parzyste)
        return wrapper2(ciag)

    def wrapper2(ciag):
        przechowac = []
        for i in ciag:
            przechowac.append(i)
        print(przechowac)
        return ciag

    return wrapper


@my_decor
def ciag_geometryczny(a1, q):
    ciag = [a1]
    for i in range(1, 100):
        ciag.append(a1 * q ** i)
    print(ciag)
    return ciag


print(ciag_geometryczny(1, 2))
