def natural_number(n):
    for i in range(n):
        yield i


class natural_number_class:
    def __init__(self):
        self.number = 0

    def __str__(self):
        return str(self.number)

    def __iter__(self):
        return self

    def __next__(self):
        num = self.number
        self.number += 1
        return num


def negative_number(n):
    for i in range(n):
        yield i * (-10)


class negative_number_class:
    def __init__(self):
        self.number = 0

    def __str__(self):
        return str(self.number)

    def __iter__(self):
        return self

    def __next__(self):
        num = self.number
        self.number -= 10
        return num


def series_sum(n):
    num = 1
    while num <= n:
        if num == 1:
            yield 1
        if num < 0:
            num -= 1
        num *= -1
        yield num


class serial_sum_class:
    def __init__(self):
        self.number = 1

    def __str__(self):
        return str(self.number)

    def __iter__(self):
        return self

    def __next__(self):
        num = self.number
        if self.number < 0:
            self.number -= 1
        self.number *= -1
        return num


def fib(n):
    fib1 = 0
    fib2 = 1
    for i in range(n):
        if i == 0:
            yield 0
        elif i == 1:
            yield 1
        fib3 = fib1 + fib2
        fib2, fib1 = fib3, fib2
        yield fib3


class fib_class:
    def __init__(self):
        self.number = 1
        self.previous = 0

    def __str__(self):
        return str(self.number)

    def __iter__(self):
        return self

    def __next__(self):
        num = self.number + self.previous
        self.number, self.previous = self.previous, num
        return num


def pattern(n):
    previous = 4
    number = 0
    for i in range(1, n + 1):
        if i == 1:
            yield previous
        else:
            number = 1 / (1 - previous)
            previous = number
            yield number


class pattern_class:
    def __init__(self):
        self.number = 0.75

    def __str__(self):
        return str(self.number)

    def __iter__(self):
        return self

    def __next__(self):
        num = 1 / (1 - self.number)
        self.number = num
        return self.number


def bell(n):
    wiersz = [1]
    for i in range(1, n + 1):
        nowy_wiersz = []
        nowy_wiersz.append(wiersz[-1])
        for j in range(1, i):
            nowy_wiersz.append(wiersz[j - 1] + nowy_wiersz[j - 1])

        wiersz = nowy_wiersz
        yield wiersz[0]


class bell_class:
    def __init__(self):
        self.line = [1]

    def __str__(self):
        return self.line

    def __iter__(self):
        return self

    def __next__(self):
        num = self.line[0]
        new_line = [self.line[-1]]
        for i in range(0, len(self.line)):
            new_line.append((self.line[i] + new_line[-1]))
        self.line = new_line
        return num


N = natural_number(20)
N_C = natural_number_class()
NN = negative_number(10)
NN_C = negative_number_class()
SS = series_sum(10)
SS_C = serial_sum_class()
FIB = fib(10)
FIB_C = fib_class()
P = pattern(10)
P_C = pattern_class()
B = bell(10)
B_C = bell_class()
for i in range(10):
    # print(next(N))
    # print(next(N_C))
    # print(next(NN))
    # print(next(NN_C))
    # print(next(SS))
    # print(next(SS_C))
    # print(next(FIB))
    # print(next(FIB_C))
    # print(next(P))
    # print(next(P_C))
    print(next(B))
    print(next(B_C))
