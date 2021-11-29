import random


class Bank:
    """
    Klasa Bank odpowiedzialna jest za system kolejkowy w banku. W zależności od wartości customer wywoływany jest
    albo iterator nazwany iterator albo generator tej klasy.

    Attributes:
    ----------
    customer: str
        Przechowuje informacje na temat czy dany klient jest firmą czy klientem indywidualnym

    Methods
    -------
    __next__():
        Generator klasy

    drukuj_numer():
        Funkcja odpowiedzialna za tworzenie nowego

    """

    def __init__(self, customer):
        self.customer = customer

    def __iter__(self):
        return self

    def __next__(self):
        return str(random.randint(0, 9))

    def drukuj_numer(self):
        try:
            if self.customer.lower() == "i":
                returner = "I"
                for i in range(4):
                    returner += next(iterator(4))
                print(returner)
                return returner
            elif self.customer.lower() == "f":
                returner = "F"
                for i in range(4):
                    returner += self.__next__()
                print(returner)
                return returner
            else:
                print("Podany string nie pasuje do żadnego z klientów")
                raise ValueError("Zła dana")
        except:
            ValueError()


def iterator(n):
    for i in range(n):
        yield str(random.randint(0, 9))


bank = Bank("f")
for i in range(5):
    bank.drukuj_numer()

bank = Bank("i")
for i in range(5):
    bank.drukuj_numer()
