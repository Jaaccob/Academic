def dzielenie(a, b):
    q = 0
    r = a
    while r >= b:
        q += 1
        r = r - b
    return q, r




print(dzielenie(17,24))
