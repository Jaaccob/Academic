class dekorklasa:
    def __init__(self, fun):
        # print("init"+str(fun))
        self.fun = fun

    def __call__(self, *args):
        napis = ""
        for i in range(len(args[0])):
            napis += str(args[0][i]) + f"x^{len(args[0]) - i - 1}"
            if i + 2 < len(args[0]):
                if args[0][i + 1] >= 0:
                    napis += "+"
        print(napis)
        print(f"st-{len(table)}")
        print(f"Argumenty {args}")
        return self.fun(*args)


@dekorklasa
def hornerVer2(table, x):
    value = table[0]
    for i in range(len(table)):
        value = value * x + table[i]
    return value

table = [2, -5, 4, -1]
x = 4

print(hornerVer2(table, x))
#2x^3-5x^2+4x^1-1x^0
#st-4
#575