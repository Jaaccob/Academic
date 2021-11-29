def my_decorator(function):
    def wrapper_a(table, x):
        napis = ""
        for i in range(len(table)):
            napis += str(table[i]) + f"x^{len(table) - i - 1}"
            if i + 2 < len(table):
                if table[i + 1] >= 0:
                    napis += "+"
        print(napis)
        print(f"st-{len(table)}")
        return round(function(table, x), 2)

    return wrapper_a


def my_decorator2(function):
    def wrapper(table, x):
        return function(table, x + 3)

    return wrapper


def hornerVer1(table, st, x):
    if (st == 0):
        return table[0]
    return x * hornerVer1(table, st - 1, x) + table[st]


@my_decorator
#@my_decorator2
def hornerVer2(table, x):
    value = table[0]
    for i in range(len(table)):
        value = value * x + table[i]
    return value


table = [2, -5, 4, -1]
x = 4

print(hornerVer2(table, x))
