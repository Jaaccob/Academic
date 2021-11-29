def nwd_rek(a, b):
    if b > 0:
        return nwd_rek(b, a % b)
    return a


def nwd_iter(a, b):
    while b:
        a, b = b, a % b
    return a


def nwd_tab(tab, n):
    nwdv = tab[0]
    for i in range(1, n):
        nwdv = nwd_rek(nwdv, tab[i])
    return nwdv

