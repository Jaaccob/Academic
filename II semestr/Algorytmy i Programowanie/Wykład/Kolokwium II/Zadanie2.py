import random


def pesel(dd, mm, rr, sex):
    """
    Funkcja pesel ma zwracać pesel dla podanej daty oraz płci. Funkcja posiada  zabezpieczeń jeśli chodzi o
    złą datę bądź źle podaną płeć.

    ...

    Attributes
    ----------
    dd: str
        Dzień urodzenia
    mm: int
        Miesiąc urodzenia
    rr: str
        Rok urodzenia
    sex: str
        Płeć

    Returns
    ---------
    Zwraca pesel użytkownika

    """
    try:
        if isinstance(dd, str) and isinstance(mm, str) and isinstance(rr, str) and isinstance(sex, str):
            if len(dd) > 1 or len(dd) < 0:
                raise ValueError()
            if len(mm) > 1 or len(mm) < 0:
                raise ValueError()
            if len(rr) > 1 or len(rr) < 0:
                raise ValueError()
            if sex != "m" or sex != "k":
                raise ValueError()
            pes = ""
            man = [1, 3, 5, 7, 9]
            female = [0, 2, 4, 6, 8]
            key = [1, 3, 7, 9]
            if sex == "m":
                while True:
                    if len(rr) > 2:
                        pes = rr[1:3]
                    else:
                        pes = rr
                    pes += mm + dd
                    ran = random.randint(0, 4)
                    pes += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                        man[int(ran)])
                    k_ = 0
                    k = 0
                    for i in pes:
                        j = 0
                        k_ += int(i) * key[j]
                        if len(str(k_)) > 1:
                            k += int(str(k_)[1])
                        else:
                            k += k_
                        j += 1
                    if len(str(k)) > 1:
                        k = 10 - int(str(k)[1])
                    if k == 10:
                        k = 1
                    pes += str(k)
                    yield pes
            if sex == "k":
                while True:
                    if len(rr) > 2:
                        pes = rr[1:3]
                    else:
                        pes = rr
                    pes += mm + dd
                    ran = random.randint(0, 4)
                    pes += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                        female[int(ran)])
                    k_ = 0
                    k = 0
                    for i in pes:
                        j = 0
                        k_ += int(i) * key[j]
                        if len(str(k_)) > 1:
                            k += int(str(k_)[1])
                        else:
                            k += k_
                        j += 1
                    if len(str(k)) > 1:
                        k = 10 - int(str(k)[1])
                    if k == 10:
                        k = 1
                    pes += str(k)
                    yield pes
        else:
            raise ValueError("Dana jest niepoprawna, ma być str")
    except:
        ValueError("Niepoprawna dana")


class pesel_class:
    """
    Klasa pesel_class ma zwracać pesel dla podanej daty oraz płci. Klasa nie posiada żadnych zabezpieczeń jeśli chodzi o
    złą datę bądź źle podaną płeć.

    ...

    Attributes
    ----------
    dd : str
        Dzień urodzenia
    mm : str
        Miesiąc urodzenia
    rr : str
        Rok urodzenia
    sex: str
        Płeć
    Methods
    -------

    __next(self):
        Generator nowych wartości pesel

    __str__(self):
        Opis funkcji print

    """

    def __init__(self, dd, mm, rr, sex):
        self.dd = dd
        self.mm = mm
        self.rr = rr
        self.sex = sex

    def __str__(self):
        return self.dd + self.mm + self.rr

    def __iter__(self):
        return self

    def __next__(self):
        pes = ""
        man = [1, 3, 5, 7, 9]
        female = [0, 2, 4, 6, 8]
        key = [1, 3, 7, 9]
        if self.sex == "m":
            while True:
                if len(self.rr) > 1:
                    pes = self.rr[1:3]
                else:
                    pes = self.rr
                pes += self.mm + self.dd
                ran = random.randint(0, 4)
                pes += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                    man[int(ran)])
                k_ = 0
                k = 0
                for i in pes:
                    j = 0
                    k_ += int(i) * key[j]
                    if len(str(k_)) > 1:
                        k += int(str(k_)[1])
                    else:
                        k += k_
                    j += 1
                if len(str(k)) > 1:
                    k = 10 - int(str(k)[1])
                if k == 10:
                    k = 1
                pes += str(k)
                return pes
        if self.sex == "k":
            while True:
                if len(self.rr) > 2:
                    pes = self.rr[1:3]
                else:
                    pes = self.rr
                pes += self.mm + self.dd
                ran = random.randint(0, 4)
                pes += str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(random.randint(0, 9)) + str(
                    female[int(ran)])
                k_ = 0
                k = 0
                for i in pes:
                    j = 0
                    k_ += int(i) * key[j]
                    if len(str(k_)) > 1:
                        k += int(str(k_)[1])
                    else:
                        k += k_
                    j += 1
                if len(str(k)) > 1:
                    k = 10 - int(str(k)[1])
                if k == 10:
                    k = 1
                pes += str(k)
                return pes


print(pesel("11", "07", "1999", "m").__next__())
print(pesel("11", "07", "1999", "m").__next__())
print(pesel("11", "07", "1999", "m").__next__())
print(pesel("11", "07", "1999", "m").__next__())

pesel_cl = pesel_class("11", "07", "1999", "m")
print(next(pesel_cl))
