def gen_cj(y, n):
    iteration = 1
    cj = 1
    while iteration <= n:
        if iteration == 0:
            iteration += 1
            yield cj
        else:
            cj = -cj * ((y ** 2) / (2 * iteration * (2 * iteration - 1)))
            iteration += 1
            yield cj


def cos(y, n=0):
    iteration = 1
    c = 0
    while iteration <= n:
        c += next(gen_cj(y, n))
        iteration += 1
    return c


print(cos(1))
