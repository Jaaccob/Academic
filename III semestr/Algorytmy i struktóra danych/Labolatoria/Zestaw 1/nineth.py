class Ulamek:
    def __init__(self, nominator, denominator):
        self.nominator = nominator
        self.denominator = denominator

    def __str__(self):
        print("Licznik = {}/ Mianownik = {}".format(self.nominator, self.denominator))

    def __add__(self, otherFraction):
        if self.denominator == otherFraction.denominator:
            return Ulamek(self.nominator + otherFraction.nominator, self.denominator)
        else:
            return Ulamek((self.nominator * otherFraction.denominator) + (otherFraction.nominator * self.denominator),
                          self.denominator * otherFraction.denominator)

    def __eq__(self, otherFraction):
        if (self.nominator * otherFraction.denominator == self.denominator * otherFraction.nominator):
            return True
        else:
            return False


ulamek1 = Ulamek(2, 4)
ulamek2 = Ulamek(5, 5)
ulamek3 = ulamek1 + ulamek2
print(ulamek3.nominator)
print(ulamek3.denominator)
print(ulamek1.__eq__(ulamek2))
ulamek4 = Ulamek(4, 8)
print(ulamek1.__eq__(ulamek4))